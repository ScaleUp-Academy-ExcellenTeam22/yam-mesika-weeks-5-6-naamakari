from functools import reduce


def add_floats(number1, number2):
    """Sum 2 floats- the function sum() working with 2 iterables"""
    return number1+number2


def get_recipe_price(prices, optionals=None, **ingredients_and_amounts):
    """Return the price of all the ingredients in the recipe according the prices and per 100 gram"""
    if optionals is None:
        optionals = []
    #  export list that contain all the ingredients for the recipe and the price for the specific amount
    ingredients = [price*(amount/100) for ingredient1, price in prices.items() if ingredient1 not in optionals for
                   ingredient2, amount in ingredients_and_amounts.items() if ingredient1 == ingredient2]
    if not ingredients:  # if there is no ingredients for the recipe
        return 0
    return reduce(add_floats, ingredients)  # sum all the prices to total price


""" for ingredient1, price in prices.items():
        if ingredient1 not in optionals:
            for ingredient2, amount in ingredients_and_amounts.items():
                if ingredient1 == ingredient2:
                    total_price += price*(amount/100)
"""


if __name__ == "__main__":
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['chocolate'], milk=300))
    print(get_recipe_price({}))
