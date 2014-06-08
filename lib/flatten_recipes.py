import itertools
import logging
import copy


def combine_flag_and_option(flag, options):
    for index, option in enumerate(options):
        flag_plus_option = flag + " " + str(option)
        options[index] = flag_plus_option
    return options


def flatten_recipe(recipe):
    flattened_recipe_commands = []
    flattened_recipe = copy.deepcopy(recipe)
    if not isinstance(flattened_recipe, dict):
        raise Exception('Recipe %s is not a dictionary' % flattened_recipe)

    recipe_flag_options = []

    flags = flattened_recipe.get('recipe_flags')
    for flag in flags:
        options_plus_flag = combine_flag_and_option(flag, flags.get(flag))
        recipe_flag_options.append(options_plus_flag)

    # https://docs.python.org/2/tutorial/controlflow.html#unpacking-argument-lists
    flag_options_combinations = itertools.product(*recipe_flag_options)
    for combination in flag_options_combinations:
        command_string = flattened_recipe.get('recipe_binary')
        for flag_option in combination:
            command_string = command_string + " " + flag_option
        flattened_recipe_commands.append(command_string)
    flattened_recipe['recipe_weight'] = flattened_recipe.get('recipe_weight')
    flattened_recipe['recipe_binary'] = flattened_recipe.get('recipe_binary')
    flattened_recipe['flattened_commands'] = flattened_recipe_commands
    logging.debug('flattened recipe is %s' % flattened_recipe)
    return flattened_recipe


def flatten_recipes(recipes_raw):
    flattened_recipes = {}
    for recipe_raw in recipes_raw.keys():
        flattened_recipe = flatten_recipe(recipes_raw[recipe_raw])
        flattened_recipes[flattened_recipe.get('recipe_name')] = flattened_recipe
    logging.debug('flattened recipes are %s' % flattened_recipes)
    return flattened_recipes
