import logging
import itertools


def build_recipe_lists(flattened_recipes):
    # ever "flattened recipe" in "flattened recipes" has a "flattened commands", we
    # need to build a list of all those lists of flattened commands.

    assert isinstance(flattened_recipes, dict), 'incorrect data type for flattened_recipes'

    recipe_commands = []

    for flattened_recipe in flattened_recipes.keys():
        recipe_commands.append(flattened_recipes[flattened_recipe].get('flattened_commands'))

    logging.debug('recipe_commands are %s' % recipe_commands)
    return recipe_commands


def build_command_lists(recipe_commands):
    # with a list of list of commands, use itertools.product to build a combination of all items
    # in each of the list of commands
    assert isinstance(recipe_commands, list), 'recipe_commands is not a list, can never happen'
    assert len(recipe_commands) > 0, 'recipe_commands is empty, can never happen'
    unordered_comand_list = []

    # https://docs.python.org/2/tutorial/controlflow.html#unpacking-argument-lists
    command_lists = itertools.product(*recipe_commands)
    for command_list in command_lists:
        unordered_comand_list.append(command_list)
    logging.debug('unordered_comand_list is %s' % unordered_comand_list)
    return unordered_comand_list


def order_command_lists(flattened_recipes, unordered_command_list):
    # takes an unordered list of unordered lists of commands
    # retunrs an underoder list or ordered lists of commands, ordered by recipe weight
    ordered_command_lists = []
    command_weight_ceiling = get_command_weight_ceiling(flattened_recipes)
    for command_list in unordered_command_list:
        command_weight_ceiling = get_command_weight_ceiling(flattened_recipes)
        ordered_command_list = []
        while command_weight_ceiling > 0:
            for command in command_list:
                command_weight = get_weight_of_command(flattened_recipes, command)
                if command_weight is command_weight_ceiling:
                    ordered_command_list.insert(0, command)
            command_weight_ceiling -= 1
        ordered_command_lists.append(ordered_command_list)

    logging.debug('ordered_command_lists is %s' % ordered_command_lists)
    return ordered_command_lists


def get_command_weight_ceiling(flattened_recipes):
    counter = 0
    for recipe in flattened_recipes.keys():
        if flattened_recipes[recipe].get('recipe_weight') >= counter:
            counter = flattened_recipes[recipe].get('recipe_weight')
    return counter


def get_weight_of_command(flattened_recipes, command):
    for recipe in flattened_recipes.keys():
        if command in flattened_recipes[recipe].get('flattened_commands'):
            return flattened_recipes[recipe].get('recipe_weight')
        

def get_ordered_command_lists(flattened_recipes):
    recipe_commands = build_recipe_lists(flattened_recipes)
    unordered_command_list = build_command_lists(recipe_commands)
    ordered_command_lists = order_command_lists(flattened_recipes, unordered_command_list)
    return ordered_command_lists
