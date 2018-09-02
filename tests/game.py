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

  def test_winner(self):
    self.assertIsNone(tennis.Game(0, 0).winner())
    self.assertIsNone(tennis.Game(4, 3).winner())
    self.assertIsNone(tennis.Game(3, 4).winner())

    self.assertTrue(tennis.Game(4, 0).winner())
    self.assertTrue(tennis.Game(4, 2).winner())
    self.assertTrue(tennis.Game(5, 3).winner())

    self.assertFalse(tennis.Game(0, 4).winner())
    self.assertFalse(tennis.Game(2, 4).winner())
    self.assertFalse(tennis.Game(3, 5).winner())

  def test_point(self):
    with self.assertRaises(
      RuntimeError,
      msg='Cannot advance this game\'s score because the game is over.'
    ):
      tennis.Game(4, 0).point(True)

    game = tennis.Game(0, 0)
    self.assertIsNone(game.point(True))
    self.assertEqual(game.server_points, 1)
    self.assertEqual(game.returner_points, 0)
    self.assertIsNone(game.point(False))
    self.assertEqual(game.server_points, 1)
    self.assertEqual(game.returner_points, 1)

    self.assertTrue(tennis.Game(3, 0).point(True))
    self.assertFalse(tennis.Game(0, 3).point(False))

  def test_str(self):
    self.assertEqual(str(tennis.Game(1, 2)), 'Game(server_points=1, returner_points=2)')

if __name__ == '__main__':
  unittest.main()
