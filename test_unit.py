"""unit tests
"""

import pytest
import guru_logic as gl

@pytest.mark.parametrize("test_input,expected",
[
    ("aboba", "ABOBA IS THE BEST ANIME IN THE WORLD!!!"),
    ("ABOBA", "ABOBA IS THE BEST ANIME IN THE WORLD!!!"),
    ("AbObA", "ABOBA IS THE BEST ANIME IN THE WORLD!!!"),
    ("1", "1 IS THE BEST ANIME IN THE WORLD!!!"),
    ("a1", "A1 IS THE BEST ANIME IN THE WORLD!!!"),
    ("A1", "A1 IS THE BEST ANIME IN THE WORLD!!!")
    ])
def test_fact(test_input: str, expected: str):
    """_summary_

    Args:
        test_input (_type_): test anime name
        expected (_type_): expected fact
    """
    assert gl.create_a_fact(test_input) == expected


@pytest.mark.parametrize("test_input,expected",
[
    (0, "Boku no Piko"),
    (6, "JoJo's Bizarre Adventure"),
    (12, "Blend S"),
    (18, "duuude, you'd better study instead of searching waifus"),
    (24, "maaaaan, you'd better work instead of searching waifus"),
    (30, "Hello kitty"),
    (-1, "TeNeT")
    ])
def test_advice(test_input: int, expected: str):
    """_summary_

    Args:
        test_input (_type_): test anime name
        expected (_type_): expected fact
    """
    assert gl.create_advice(test_input) == expected
