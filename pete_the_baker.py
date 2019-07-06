from codewars_test import Test


def cakes(recipe, available):
    return min([available.get(k, 0) // v for k, v in recipe.items()])


recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
Test.assert_equals(cakes(recipe, available), 2)

recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available = {"sugar": 500, "flour": 2000, "milk": 2000}
Test.assert_equals(cakes(recipe, available), 0)
