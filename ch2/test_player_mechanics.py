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
