#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    total_batches = 0
    if(len(recipe) != len(ingredients)):
        return 0
    for key, value in recipe.items():
        for k, v in ingredients.items():
            if key == k:
                batches = v // value
                if batches == 0:
                    return 0
                if batches > 0:
                    if total_batches == 0:
                        total_batches = batches
                    if total_batches > batches:
                        total_batches = batches
    print(total_batches)
    return total_batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
