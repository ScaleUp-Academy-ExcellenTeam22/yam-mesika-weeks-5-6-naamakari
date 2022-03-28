from functools import reduce


def add_floats(number1: float, number2: float) -> float:
    """
    Sum 2 floats- the function sum() working with 2 iterables.
    :param number1: First float number.
    :param number2: Second float number.
    :return: The sum of the two numbers.
    """
    return number1 + number2


def get_recipe_price(prices: dict, optionals: list = None, **ingredients_and_amounts: int) -> float:
    """
    Return the price of all the ingredients in the recipe according the prices and per 100 gram.
    :param prices: The ingredients for the recipe and their costs per 100 gram.
    :param optionals: Ingredients to ignore for, in the recipe.
    :param ingredients_and_amounts: The ingredients to use at the recipe and the amounts of each one.
    :return: The sum of the ingredients for the recipe.
    """
    if optionals is None:
        optionals = []
    # Extract list that contain all the ingredients for the recipe and the price for the specific amount.
    ingredients = [price * (amount / 100) for ingredient1, price in prices.items() if ingredient1 not in optionals for
                   ingredient2, amount in ingredients_and_amounts.items() if ingredient1 == ingredient2]
    # If there is no ingredients for the recipe, the reduce is not working on empty sequence
    if not ingredients:
        return 0
    # Sum all the prices to total price.
    return reduce(add_floats, ingredients)


if __name__ == "__main__":
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['chocolate'], milk=300))
    print(get_recipe_price({}))
