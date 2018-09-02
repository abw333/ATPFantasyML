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
