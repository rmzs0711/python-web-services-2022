"""business logic
"""

def create_a_fact(anime_name: str) -> str:
    """ create a fact according to title's name

    Args:
        anime_name (str): title's name

    Returns:
        str: fact
    """
    return anime_name.upper() + " IS THE BEST ANIME IN THE WORLD!!!"

def create_advice(age: int) -> str:
    """create the best advice you can even get in this world

    Args:
        age (int): your age

    Returns:
        str: advice
    """
    advice = "Hello kitty"
    if age < 0:
        advice = "TeNeT"
    elif age < 6:
        advice = "Boku no Piko"
    elif 6 <= age < 12:
        advice = "JoJo's Bizarre Adventure"
    elif 12 <= age < 18:
        advice = "Blend S"
    elif 18 <= age < 24:
        advice = "duuude, you'd better study instead of searching waifus"
    elif 24 <= age < 30:
        advice = "maaaaan, you'd better work instead of searching waifus"
    return advice
