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

  '''
  :return: the number of games won by the player who served first
  '''
  def first_server_games(self):
    return len([i for i, g in enumerate(self.games) if (i % 2 == 0) == g.winner()])

  '''
  :return: the number of games won by the player who returned first
  '''
  def first_returner_games(self):
    return len([i for i, g in enumerate(self.games) if (i % 2 == 1) == g.winner()])

  '''
  :return: True if the first server won the set, False if the first returner won the
           set, and None otherwise
  '''
  def winner(self):
    first_server_games = self.first_server_games()
    if self.tiebreak and first_server_games == 7:
      return True

    first_returner_games = self.first_returner_games()
    if self.tiebreak and first_returner_games == 7:
      return False

    if first_server_games >= 6 and first_server_games - first_returner_games >= 2:
      return True

    if first_returner_games >= 6 and first_returner_games - first_server_games >= 2:
      return False

  '''
  :return: a string representation of the set
  '''
  def __str__(self):
    return '{}(games={}, tiebreak={})'.format(
      type(self).__name__,
      self.games,
      self.tiebreak
    )

  '''
  :param object other: object to compare to the set
  :return: True if the input object is equal to the set, and False otherwise
  '''
  def __eq__(self, other):
    return isinstance(other, type(self)) and self.__dict__ == other.__dict__
