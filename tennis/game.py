class Game:
  '''
  Python class for objects that represent tennis games.

  :param int server_points: number of points scored by the server
  :param int returner_points: number of points scored by the returner
  :param bool deciding_point: whether to play a deciding point at deuce
  :var server_points: number of points scored by the server
  :var returner_points: number of points scored by the returner
  :var deciding_point: whether to play a deciding point at deuce
  '''
  def __init__(self, *, server_points=0, returner_points=0, deciding_point=False):
    if min(server_points, returner_points) < 0:
      raise RuntimeError('Point scores must be non-negative.')

    if deciding_point and max(server_points, returner_points) > 4:
      raise RuntimeError('Point scores must be reachable.')

    if deciding_point and min(server_points, returner_points) > 3:
      raise RuntimeError('Point scores must be reachable.')

    if abs(server_points - returner_points) > 2 and max(server_points, returner_points) > 4:
      raise RuntimeError('Point scores must be reachable.')

    self.server_points = server_points
    self.returner_points = returner_points
    self.deciding_point = deciding_point

  '''
  :return: True if the server won the game, False if the returner won the game, and None
           otherwise
  '''
  def winner(self):
    if self.deciding_point and self.server_points == 4:
      return True

    if self.deciding_point and self.returner_points == 4:
      return False

    if self.server_points >= 4 and self.server_points - self.returner_points >= 2:
      return True

    if self.returner_points >= 4 and self.returner_points - self.server_points >= 2:
      return False

  '''
  Advances the game's score by a point.

  :param bool first_server: True if the server won the point, and False otherwise
  :return: True if the server won the game, False if the returner won the game, and None
           otherwise
  :raises RuntimeError: if the game's score cannot be advanced because the game is over
  '''
  def point(self, *, first_server):
    if self.winner() is not None:
      raise RuntimeError('Cannot advance this game\'s score because the game is over.')

    if first_server:
      self.server_points += 1
    else:
      self.returner_points += 1

    return self.winner()

  '''
  :return: a string representation of the game
  '''
  def __str__(self):
    return '{}(server_points={}, returner_points={}, deciding_point={})'.format(
      type(self).__name__,
      self.server_points,
      self.returner_points,
      self.deciding_point
    )

  '''
  :return: a string representation of the game
  '''
  def __repr__(self):
    return str(self)

  '''
  :param object other: object to compare to the game
  :return: True if the input object is equal to the game, and False otherwise
  '''
  def __eq__(self, other):
    return isinstance(other, type(self)) and self.__dict__ == other.__dict__
