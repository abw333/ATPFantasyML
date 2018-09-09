import tennis

class Set:
  '''
  Python class for objects that represent tennis sets.

  :param list games: list of games played in the set
  :param bool tiebreak: whether a tiebreak is played at 6-6
  :var games: list of games played in the set
  :var tiebreak: whether a tiebreak is played at 6-6
  '''
  def __init__(self, games=None, tiebreak=True):
    self.games = \
      [tennis.Game(server_points=0, returner_points=0)] if games is None else games
    self.tiebreak = tiebreak
