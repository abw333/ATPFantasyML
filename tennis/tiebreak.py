class Tiebreak:
  '''
  Python class for objects that represent tennis tiebreaks.

  :param int first_server_points: number of points scored by the player who served first
  :param int first_returner_points: number of points scored by the player who returned first
  :param int target_points: number of points required to win the tiebreak
  :var first_server_points: number of points scored by the player who served first
  :var first_returner_points: number of points scored by the player who returned first
  :var target_points: number of points required to win the tiebreak
  :var winner: True if the first server won the tiebreak, False if the first returner won the
               tiebreak, and None otherwise
  '''
  def __init__(self, *, first_server_points=0, first_returner_points=0, target_points=7):
    if min(first_server_points, first_returner_points, target_points) < 0:
      raise RuntimeError('Point scores must be non-negative.')

    if abs(first_server_points - first_returner_points) > 2:
      if max(first_server_points, first_returner_points) > target_points:
        raise RuntimeError('Point score must be reachable.')

    self.first_server_points = first_server_points
    self.first_returner_points = first_returner_points
    self.target_points = target_points
    self.winner = self._compute_winner()

  '''
  :return: True if the first server won the tiebreak, False if the first returner won the tiebreak,
           and None otherwise
  '''
  def _compute_winner(self):
    if self.first_server_points >= self.target_points:
      if self.first_server_points - self.first_returner_points >= 2:
        return True

    if self.first_returner_points >= self.target_points:
      if self.first_returner_points - self.first_server_points >= 2:
        return False

  '''
  :return: True if the first server is to serve the next point, and False if the first returner
           is to serve the next point
  :raises RuntimeError: if no server is to serve the next point because the tiebreak is over
  '''
  def first_server_to_serve(self):
    if self.winner is not None:
      raise RuntimeError('No server is to serve the next point because the tiebreak is over.')

    return (self.first_server_points + self.first_returner_points) % 4 in (0, 3)

  '''
  Advances the tiebreak's score by a point.

  :param bool first_server: True if the first server won the point, and False otherwise
  :return: True if the first server won the tiebreak, False if the first returner won the tiebreak,
           and None otherwise
  :raises RuntimeError: if the tiebreak's score cannot be advanced because the tiebreak is over
  '''
  def point(self, *, first_server):
    if self.winner is not None:
      raise RuntimeError('Cannot advance this tiebreak\'s score because the tiebreak is over.')

    if first_server:
      self.first_server_points += 1
    else:
      self.first_returner_points += 1

    self.winner = self._compute_winner()

    return self.winner

  '''
  :return: a string representation of the tiebreak
  '''
  def __str__(self):
    return '{}(first_server_points={}, first_returner_points={}, target_points={})'.format(
      type(self).__name__,
      self.first_server_points,
      self.first_returner_points,
      self.target_points
    )

  '''
  :return: a string representation of the tiebreak
  '''
  def __repr__(self):
    return str(self)

  '''
  :param object other: object to compare to the tiebreak
  :return: True if the input object is equal to the tiebreak, and False otherwise
  '''
  def __eq__(self, other):
    return isinstance(other, type(self)) and self.__dict__ == other.__dict__
