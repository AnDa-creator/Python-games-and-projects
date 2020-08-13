class Player(object):

    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives cannot be negative")
    lives = property(_get_lives, _set_lives)

    def _get_level(self):
        return self._level

    def _set_level(self,level):
        if self._level + level >= 1:
            self._level += level
            self._score += 1000*level
        else:
            print("Level cannot be less than one")

    level = property(_get_level,_set_level)

    @property
    def score(self):
        """Get the current voltage."""
        return self.score

    @score.setter
    def score(self, score):
        self._score = score

    def __str__(self, score):
        self._score = score



    def __str__(self):
        return "Name: {0.name}, Lives:{0.lives}, Level: {0.level}, Score: {0._score}".format(self)
