class Game:
  '''
  Python class for objects that represent tennis games.

  :param int server_points: number of points scored by the server
  :param int returner_points: number of points scored by the returner
  :var server_points: number of points scored by the server
  :var returner_points: number of points scored by the returner
  '''
  def __init__(self, server_points=0, returner_points=0):
    self.server_points = server_points
    self.returner_points = returner_points
