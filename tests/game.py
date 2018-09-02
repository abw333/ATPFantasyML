import unittest

import tennis

class Game(unittest.TestCase):
  def test_init_no_args(self):
    game = tennis.Game()

    self.assertEqual(game.server_points, 0)
    self.assertEqual(game.returner_points, 0)

  def test_init_args(self):
    game = tennis.Game(1, 2)

    self.assertEqual(game.server_points, 1)
    self.assertEqual(game.returner_points, 2)

  def test_init_kwargs(self):
    game = tennis.Game(returner_points=4, server_points=3)

    self.assertEqual(game.server_points, 3)
    self.assertEqual(game.returner_points, 4)

if __name__ == '__main__':
  unittest.main()
