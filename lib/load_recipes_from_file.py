import json
import glob
import logging


def get_recipe_files():
    recipe_files = glob.glob('recipes/*')
    if len(recipe_files) is 0:
        raise Exception('Could not identify list of files in the recipes/ directory')
    logging.debug('recipe files are: %s' % recipe_files)
    return recipe_files


def load_recipes_from_recipe_files(recipe_files):
    recipes_raw = {}
    for recipe_file in recipe_files:
        try:
            f_recipe_file = open(recipe_file, 'r')
            recipe_raw = json.load(f_recipe_file)
        except:
            raise Exception('Could not open and parse json file %s' % recipe_file)

        if len(recipe_raw) is 0:
            raise Exception('Recipe %s must not be empty' % recipe_file)
        recipe_raw_name = recipe_raw.get('recipe_name')
        recipes_raw[recipe_raw_name] = recipe_raw

    logging.debug('recipe raw data is: %s' % recipes_raw)
    return recipes_raw


def recipe_files_handler():
    recipe_files = get_recipe_files()
    recipes_raw = load_recipes_from_recipe_files(recipe_files)
    return recipes_raw
