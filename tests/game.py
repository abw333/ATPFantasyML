import re
import unittest

import tennis

class Game(unittest.TestCase):
  def test_init_no_args(self):
    game = tennis.Game()

    self.assertEqual(game.server_points, 0)
    self.assertEqual(game.returner_points, 0)
    self.assertFalse(game.deciding_point)

  def test_init_args(self):
    with self.assertRaisesRegex(
      TypeError,
      '^{}$'.format(re.escape('__init__() takes 1 positional argument but 2 were given'))
    ):
      tennis.Game(1)

  def test_init_kwargs(self):
    game = tennis.Game(deciding_point=True, returner_points=4, server_points=3)

    self.assertEqual(game.server_points, 3)
    self.assertEqual(game.returner_points, 4)
    self.assertTrue(game.deciding_point)

  def test_init_negative_points(self):
    with self.assertRaisesRegex(
      RuntimeError,
      '^{}$'.format(re.escape('Point scores must be non-negative.'))
    ):
      tennis.Game(server_points=0, returner_points=-1)

    with self.assertRaisesRegex(
      RuntimeError,
      '^{}$'.format(re.escape('Point scores must be non-negative.'))
    ):
      tennis.Game(server_points=-1, returner_points=0)

  def test_init_unreachable_points(self):
    with self.assertRaisesRegex(
      RuntimeError,
      '^{}$'.format(re.escape('Point scores must be reachable.'))
    ):
      tennis.Game(server_points=5, returner_points=2)

    with self.assertRaisesRegex(
      RuntimeError,
      '^{}$'.format(re.escape('Point scores must be reachable.'))
    ):
      tennis.Game(server_points=2, returner_points=5)

    with self.assertRaisesRegex(
      RuntimeError,
      '^{}$'.format(re.escape('Point scores must be reachable.'))
    ):
      tennis.Game(server_points=4, returner_points=4, deciding_point=True)

    with self.assertRaisesRegex(
      RuntimeError,
      '^{}$'.format(re.escape('Point scores must be reachable.'))
    ):
      tennis.Game(server_points=5, returner_points=3, deciding_point=True)

    with self.assertRaisesRegex(
      RuntimeError,
      '^{}$'.format(re.escape('Point scores must be reachable.'))
    ):
      tennis.Game(server_points=3, returner_points=5, deciding_point=True)

    tennis.Game(server_points=5, returner_points=3)
    tennis.Game(server_points=3, returner_points=5)
    tennis.Game(server_points=4, returner_points=1)
    tennis.Game(server_points=1, returner_points=4)
    tennis.Game(server_points=4, returner_points=4)

  def test_winner(self):
    self.assertIsNone(tennis.Game(server_points=0, returner_points=0).winner())
    self.assertIsNone(tennis.Game(server_points=4, returner_points=3).winner())
    self.assertIsNone(tennis.Game(server_points=3, returner_points=4).winner())

    self.assertTrue(tennis.Game(server_points=4, returner_points=0).winner())
    self.assertTrue(tennis.Game(server_points=4, returner_points=2).winner())
    self.assertTrue(tennis.Game(server_points=5, returner_points=3).winner())
    self.assertTrue(tennis.Game(server_points=4, returner_points=3, deciding_point=True).winner())

    self.assertFalse(tennis.Game(server_points=0, returner_points=4).winner())
    self.assertFalse(tennis.Game(server_points=2, returner_points=4).winner())
    self.assertFalse(tennis.Game(server_points=3, returner_points=5).winner())
    self.assertFalse(tennis.Game(server_points=3, returner_points=4, deciding_point=True).winner())

  def test_point(self):
    with self.assertRaisesRegex(
      RuntimeError,
      '^{}$'.format(re.escape('Cannot advance this game\'s score because the game is over.'))
    ):
      tennis.Game(server_points=4, returner_points=0).point(first_server=True)

    game = tennis.Game(server_points=0, returner_points=0)
    self.assertIsNone(game.point(first_server=True))
    self.assertEqual(game.server_points, 1)
    self.assertEqual(game.returner_points, 0)
    self.assertIsNone(game.point(first_server=False))
    self.assertEqual(game.server_points, 1)
    self.assertEqual(game.returner_points, 1)

    self.assertTrue(tennis.Game(server_points=3, returner_points=0).point(first_server=True))
    self.assertFalse(tennis.Game(server_points=0, returner_points=3).point(first_server=False))

  def test_str(self):
    self.assertEqual(
      str(tennis.Game(server_points=1, returner_points=2, deciding_point=True)),
      'Game(server_points=1, returner_points=2, deciding_point=True)'
    )

  def test_repr(self):
    self.assertEqual(
      repr(tennis.Game(server_points=1, returner_points=2, deciding_point=True)),
      'Game(server_points=1, returner_points=2, deciding_point=True)'
    )

  def test_eq(self):
    self.assertEqual(
      tennis.Game(server_points=1, returner_points=2),
      tennis.Game(server_points=1, returner_points=2)
    )
    self.assertNotEqual(
      tennis.Game(server_points=1, returner_points=2),
      tennis.Game(server_points=2, returner_points=1)
    )

if __name__ == '__main__':
  unittest.main()
