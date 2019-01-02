import tennis

class Set:
  '''
  Python class for objects that represent tennis sets.

  :param list games: list of games played in the set
  :param int tiebreak_games: number of games each player must have before a tiebreak is played,
                             or None if a tiebreak is not to be played
  :param int tiebreak_points: number of points required to win the tiebreak, or None if a tiebreak
                              is not to be played
  :var games: list of games played in the set
  :var tiebreak_games: number of games each player must have before a tiebreak is played, or None
                       if a tiebreak is not to be played
  :var tiebreak_points: number of points required to win the tiebreak, or None if a tiebreak is not
                        to be played
  '''
  def __init__(self, games=None, tiebreak_games=6, tiebreak_points=7):
    # TODO(abw333): validate games

    if (tiebreak_games is None) != (tiebreak_points is None):
      raise RuntimeError('tiebreak_games and tiebreak_points must both be None or non-None.')

    if tiebreak_games is not None and min(tiebreak_games, tiebreak_points) < 0:
      raise RuntimeError('Point scores must be non-negative.')

    if games is not None:
      self.games = games
    elif tiebreak_games != 0:
      self.games = [tennis.Game(server_points=0, returner_points=0)]
    else:
      self.games = [tennis.Tiebreak(
        first_server_points=0,
        first_returner_points=0,
        target_points=tiebreak_points
      )]

    self.tiebreak_games = tiebreak_games
    self.tiebreak_points = tiebreak_points

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
    if self.tiebreak_games is not None and first_server_games == self.tiebreak_games + 1:
      return True

    first_returner_games = self.first_returner_games()
    if self.tiebreak_games is not None and first_returner_games == self.tiebreak_games + 1:
      return False

    if first_server_games >= 6 and first_server_games - first_returner_games >= 2:
      return True

    if first_returner_games >= 6 and first_returner_games - first_server_games >= 2:
      return False

  '''
  Advances the set's score by a point.

  :param bool first_server: True if the first server won the point, and False otherwise
  :return: True if the first server won the set, False if the first returner won the
           set, and None otherwise
  :raises RuntimeError: if the set's score cannot be advanced because the set is over
  '''
  def point(self, first_server):
    if self.winner() is not None:
      raise RuntimeError('Cannot advance this set\'s score because the set is over.')

    game_winner = self.games[-1].point((len(self.games) % 2 == 1) == first_server)
    if game_winner is None:
      return None

    set_winner = self.winner()
    if set_winner is not None:
      return set_winner

    if self.tiebreak_games is not None and \
      self.first_server_games() == self.tiebreak_games and \
      self.first_returner_games() == self.tiebreak_games:
      self.games.append(tennis.Tiebreak(
        first_server_points=0,
        first_returner_points=0,
        target_points=self.tiebreak_points
      ))
    else:
      self.games.append(tennis.Game(server_points=0, returner_points=0))

  '''
  :return: a string representation of the set
  '''
  def __str__(self):
    return '{}(games={}, tiebreak_games={}, tiebreak_points={})'.format(
      type(self).__name__,
      self.games,
      self.tiebreak_games,
      self.tiebreak_points
    )

  '''
  :return: a string representation of the set
  '''
  def __repr__(self):
    return str(self)

  '''
  :param object other: object to compare to the set
  :return: True if the input object is equal to the set, and False otherwise
  '''
  def __eq__(self, other):
    return isinstance(other, type(self)) and self.__dict__ == other.__dict__
