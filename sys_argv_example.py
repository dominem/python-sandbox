import sys


RECIPE_ARGV_INDEX = 1

INGREDIENTS_ARGV_START_INDEX = 2

EXIT_CODE_ERROR = 1


def is_list_empty(ingredients):
    return len(ingredients) == 0


def print_recipe(recipe, ingredients):
    print(f'{recipe}:')

    for i, ingredient in enumerate(ingredients, start=1):
        print(f'{i}. {ingredient}.')


try:
    recipe = sys.argv[RECIPE_ARGV_INDEX]
except IndexError:
    print("First argument missing - a recipe's name!")
    sys.exit(EXIT_CODE_ERROR)


ingredients = sys.argv[INGREDIENTS_ARGV_START_INDEX:]


if is_list_empty(ingredients):
    print(
        "Put some ingredients as next arguments, for example:\n"
        "  python sys_argv_example.py Sandwich 'Slice of bread' "
        "'Some butter' '2 slices of ham'"
    )
    sys.exit(EXIT_CODE_ERROR)


print_recipe(recipe, ingredients)
