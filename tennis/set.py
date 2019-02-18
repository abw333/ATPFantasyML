import tennis

class Set:
  '''
  Python class for objects that represent tennis sets.

  :param list games: list of games played in the set
  :param int target_games: number of games required to win the set
  :param bool deciding_point: whether to play a deciding point at deuce
  :param int tiebreak_games: number of games each player must have before a tiebreak is played, or
                             None if a tiebreak is not to be played
  :param int tiebreak_points: number of points required to win the tiebreak, or None if a tiebreak
                              is not to be played
  :var games: list of games played in the set
  :var target_games: number of games required to win the set
  :var deciding_point: whether to play a deciding point at deuce
  :var tiebreak_games: number of games each player must have before a tiebreak is played, or None if
                       a tiebreak is not to be played
  :var tiebreak_points: number of points required to win the tiebreak, or None if a tiebreak is not
                        to be played
  '''
  def __init__(
    self,
    *,
    games=None,
    target_games=6,
    deciding_point=False,
    tiebreak_games=6,
    tiebreak_points=7
  ):
    # TODO(abw333): validate games

    if target_games < 0:
      raise RuntimeError('Point scores must be non-negative.')

    if (tiebreak_games is None) != (tiebreak_points is None):
      raise RuntimeError('tiebreak_games and tiebreak_points must both be None or non-None.')

    if tiebreak_games is not None and min(tiebreak_games, tiebreak_points) < 0:
      raise RuntimeError('Point scores must be non-negative.')

    if games is not None:
      self.games = games
    elif tiebreak_games != 0:
      self.games = [tennis.Game(server_points=0, returner_points=0, deciding_point=deciding_point)]
    else:
      self.games = [tennis.Tiebreak(
        first_server_points=0,
        first_returner_points=0,
        target_points=tiebreak_points
      )]

    self.target_games = target_games
    self.deciding_point = deciding_point
    self.tiebreak_games = tiebreak_games
    self.tiebreak_points = tiebreak_points
    self._winner = self._compute_winner()
    self._first_server_to_serve = self._compute_first_server_to_serve()

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
  :return: True if the first server won the set, False if the first returner won the set, and None
           otherwise
  '''
  def _compute_winner(self):
    first_server_games = self.first_server_games()
    if self.tiebreak_games is not None and first_server_games == self.tiebreak_games + 1:
      return True

    first_returner_games = self.first_returner_games()
    if self.tiebreak_games is not None and first_returner_games == self.tiebreak_games + 1:
      return False

    if first_server_games >= self.target_games and first_server_games - first_returner_games >= 2:
      return True

    if first_returner_games >= self.target_games and first_returner_games - first_server_games >= 2:
      return False

  '''
  :return: True if the first server won the set, False if the first returner won the set, and None
           otherwise
  '''
  def winner(self):
    return self._winner

  '''
  :return: None if the set is currently in a tiebreak; otherwise, True if the first server is to
           serve the next point, and False if the first returner is to serve the next point
  '''
  def _compute_first_server_to_serve(self):
    if type(self.games[-1]) is tennis.Tiebreak:
      return None

    return bool(len(self.games) % 2)

  '''
  :return: True if the first server is to serve the next point, and False if the first returner
           is to serve the next point
  :raises RuntimeError: if no server is to serve the next point because the set is over
  '''
  def first_server_to_serve(self):
    if self.winner() is not None:
      raise RuntimeError('No server is to serve the next point because the set is over.')

    if self._first_server_to_serve is None:
      return self.games[-1].first_server_to_serve()

    return self._first_server_to_serve

  '''
  Advances the set's score by a point.

  :param bool first_server: True if the first server won the point, and False otherwise
  :return: True if the first server won the set, False if the first returner won the set, and None
           otherwise
  :raises RuntimeError: if the set's score cannot be advanced because the set is over
  '''
  def point(self, *, first_server):
    if self.winner() is not None:
      raise RuntimeError('Cannot advance this set\'s score because the set is over.')

    game_winner = self.games[-1].point(first_server=(len(self.games) % 2 == 1) == first_server)
    if game_winner is None:
      return None

    self._winner = self._compute_winner()

    if self._winner is not None:
      return self._winner

    if self.tiebreak_games is not None and \
      self.first_server_games() == self.tiebreak_games and \
      self.first_returner_games() == self.tiebreak_games:
      self.games.append(tennis.Tiebreak(
        first_server_points=0,
        first_returner_points=0,
        target_points=self.tiebreak_points
      ))
      self._first_server_to_serve = None
    else:
      self.games.append(tennis.Game(
        server_points=0,
        returner_points=0,
        deciding_point=self.deciding_point
      ))
      self._first_server_to_serve = not self._first_server_to_serve

  '''
  :return: a string representation of the set
  '''
  def __str__(self):
    return ('{}('
      'games={}, '
      'target_games={}, '
      'deciding_point={}, '
      'tiebreak_games={}, '
      'tiebreak_points={}'
    ')').format(
      type(self).__name__,
      self.games,
      self.target_games,
      self.deciding_point,
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
