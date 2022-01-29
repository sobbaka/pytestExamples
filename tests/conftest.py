# file for fixtures
import pytest
from random import randrange

from src.generators.players import Player


@pytest.fixture
def get_player_generator():
    return Player()

@pytest.fixture
def say_hello():
    # print('hello!')
    return 14

@pytest.fixture
def get_number():
    return randrange(1, 1000, 5)


def _calculate(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    return None


@pytest.fixture
def calculate():
    return _calculate

@pytest.fixture
def make_number():
    # print('I`m getting number')
    number = randrange(1, 1000, 5)
    yield number
    # print(f'Number is here {number}')
