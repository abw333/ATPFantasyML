class Tiebreak:
  '''
  Python class for objects that represent tennis tiebreaks.

  :param int first_server_points: number of points scored by the player who served first
  :param int first_returner_points: number of points scored by the player who returned
                                    first
  :var first_server_points: number of points scored by the player who served first
  :var first_returner_points: number of points scored by the player who returned first
  '''
  def __init__(self, first_server_points=0, first_returner_points=0):
    self.first_server_points = first_server_points
    self.first_returner_points = first_returner_points

  '''
  :return: True if the first server won the tiebreak, False if the first returner won
           the tiebreak, and None otherwise
  '''
  def winner(self):
    if self.first_server_points >= 7:
      if self.first_server_points - self.first_returner_points >= 2:
        return True

    if self.first_returner_points >= 7:
      if self.first_returner_points - self.first_server_points >= 2:
        return False

  '''
  Advances the tiebreak's score by a point.

  :param bool first_server: True if the first server won the point, and False otherwise
  :return: True if the first server won the tiebreak, False if the first returner won
           the tiebreak, and None otherwise
  :raises RuntimeError: if the tiebreak's score cannot be advanced because the tiebreak
                        is over
  '''
  def point(self, first_server):
    if self.winner() is not None:
      raise RuntimeError(
        'Cannot advance this tiebreak\'s score because the tiebreak is over.'
      )

    if first_server:
      self.first_server_points += 1
    else:
      self.first_returner_points += 1

    return self.winner()

  '''
  :return: a string representation of the tiebreak
  '''
  def __str__(self):
    return '{}(first_server_points={}, first_returner_points={})'.format(
      type(self).__name__,
      self.first_server_points,
      self.first_returner_points
    )

  '''
  :return: a string representation of the tiebreak
  '''
  def __repr__(self):
    return str(self)
