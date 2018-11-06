import textwrap

class player(object):

    default_player_class = 'warrior'
    default_healths = {'warrior': 100,
                       'sorcerer': 100,
                       'undead':   200,
                       }

    player_classes = {'warrior':  'warrior',
                      'sorcerer': 'sorcerer',
                      'undead':   'undead',
                       }

    player_short_class_descriptions = {
        'warrior':
            'A battle-hardened veteran; can equip heavy armor and weapons.',
         'sorcerer':
            'sorcerer',
         'undead':
             'undead',
    }

    player_long_class_descriptions = {
        'warrior':
           '''\
           A seasoned veteran of many battles.  High Strength and Dexterity
           allow him or her to yield heavy armor and weapons, as well as carry
           more equipment while keeping a light roll.  Weak in magic
           ''',
        'sorcerer':
            'sorcerer',
        'undead':
            'undead',
    }

    player_starting_equipment = {
        'warrior': ['long sword', 'warrior set', 'shield'],
        'sorcerer': ['wand'],
        'undead': [],
    }

    def __init__(self, player_class):
        self.health = self.set_default_health( player_class )
        self.player_class = self.player_classes[ player_class]

    def get_hit(self):
        self.health -= 20

    def get_default_health(self):
        return self.default_healths[self.player_class]

    def set_default_health(self, player_class):
        return self.default_healths[player_class]

    def get_default_player_class(self):
        return self.default_player_class

    def get_player_class(self):
        return self.player_class

    def get_short_class_description(self):
        return self.player_short_class_descriptions[ self.get_player_class() ]

    def get_long_class_description(self):
        return textwrap.dedent(
            self.player_long_class_descriptions[ self.get_player_class() ]
        )

    def get_player_starting_equipment(self):
        return self.player_starting_equipment[ self.get_player_class() ]

    def hit( self, player ):
        player.get_hit()

