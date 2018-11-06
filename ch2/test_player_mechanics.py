import textwrap
from .player import player


def test_player_hit():
    kartoon = player('warrior')
    assert kartoon.health == 100
    glug = player('undead')
    glug.hit(kartoon)
    assert kartoon.health == 80


def test_default_health():
    kartoon = player('warrior')
    health = kartoon.get_default_health()
    assert health == 100


def test_default_player_class():
    munch = player('undead')
    x = munch.get_default_player_class()
    assert x == 'warrior'


def test_get_player_class():
    munch = player("undead")
    x = munch.get_player_class()
    assert x == "undead"


def test_warrior_short_description():
    kartoon = player('warrior')
    desc = kartoon.get_short_class_description()
    assert desc == "A battle-hardened veteran; can equip heavy armor and weapons."


def test_warrior_long_description():
    kartoon = player('warrior')
    desc = kartoon.get_long_class_description()
    assert desc == textwrap.dedent('''\
        A seasoned veteran of many battles.  High Strength and Dexterity
        allow him or her to yield heavy armor and weapons, as well as carry
        more equipment while keeping a light roll.  Weak in magic
        ''')

def test_get_warrior_starting_equipment():
    kartoon = player('warrior')
    expected = ['long sword', 'warrior set', 'shield']
    assert kartoon.get_player_starting_equipment() == expected
