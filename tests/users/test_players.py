import pytest

from src.generators.player_localization import PlayerLocalization


@pytest.mark.parametrize('status', [
    'ACTIVE',
    'BANNED',
    'DELETED',
    'INACTIVE'
])
def test_something(status, get_player_generator):
    print(get_player_generator.set_status(status).build())


@pytest.mark.parametrize('balance', [
    '100',
    '1',
    '-1',
    'some'
])
def test_something(balance, get_player_generator):
    print(get_player_generator.set_balance(balance).build())


@pytest.mark.parametrize('detelete_key', [
    'account_status',
    'balance',
    'localize',
    'avatar'
])
def test_something(detelete_key, get_player_generator):
    object = get_player_generator.build()
    del object[detelete_key]
    print(object)


def test_update_inner_generator(get_player_generator):
    object = get_player_generator.update_inner_generator(
        'localize', PlayerLocalization('fr_FR')
    ).build()
    print(object)
