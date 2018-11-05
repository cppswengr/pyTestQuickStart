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

    def hit( self, player ):
        player.get_hit()

