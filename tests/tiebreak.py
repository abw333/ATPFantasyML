import unittest

import tennis

class Tiebreak(unittest.TestCase):
  def test_init_no_args(self):
    tiebreak = tennis.Tiebreak()

    self.assertEqual(tiebreak.first_server_points, 0)
    self.assertEqual(tiebreak.first_returner_points, 0)

  def test_init_args(self):
    with self.assertRaises(
      TypeError,
      msg='__init__() takes 1 positional argument but 2 were given'
    ):
      tennis.Tiebreak(1)

  def test_init_kwargs(self):
    tiebreak = tennis.Tiebreak(first_returner_points=4, first_server_points=3)

    self.assertEqual(tiebreak.first_server_points, 3)
    self.assertEqual(tiebreak.first_returner_points, 4)

  def test_init_negative_points(self):
    with self.assertRaises(RuntimeError, msg='Point scores must be non-negative.'):
      tennis.Tiebreak(first_server_points=-1, first_returner_points=0, target_points=0)

    with self.assertRaises(RuntimeError, msg='Point scores must be non-negative.'):
      tennis.Tiebreak(first_server_points=0, first_returner_points=-1, target_points=0)

    with self.assertRaises(RuntimeError, msg='Point scores must be non-negative.'):
      tennis.Tiebreak(first_server_points=0, first_returner_points=0, target_points=-1)

  def test_init_unreachable_points(self):
    with self.assertRaises(RuntimeError, msg='Point scores must be reachable.'):
      tennis.Tiebreak(first_server_points=6, first_returner_points=3, target_points=5)

    with self.assertRaises(RuntimeError, msg='Point scores must be reachable.'):
      tennis.Tiebreak(first_server_points=3, first_returner_points=6, target_points=5)

    tennis.Tiebreak(first_server_points=6, first_returner_points=4, target_points=5)
    tennis.Tiebreak(first_server_points=4, first_returner_points=6, target_points=5)
    tennis.Tiebreak(first_server_points=5, first_returner_points=2, target_points=5)
    tennis.Tiebreak(first_server_points=2, first_returner_points=5, target_points=5)

  def test_winner(self):
    self.assertIsNone(tennis.Tiebreak(first_server_points=0, first_returner_points=0).winner())
    self.assertIsNone(tennis.Tiebreak(first_server_points=7, first_returner_points=6).winner())
    self.assertIsNone(tennis.Tiebreak(first_server_points=6, first_returner_points=7).winner())

    self.assertTrue(tennis.Tiebreak(first_server_points=7, first_returner_points=0).winner())
    self.assertTrue(tennis.Tiebreak(first_server_points=7, first_returner_points=5).winner())
    self.assertTrue(tennis.Tiebreak(first_server_points=8, first_returner_points=6).winner())

    self.assertFalse(tennis.Tiebreak(first_server_points=0, first_returner_points=7).winner())
    self.assertFalse(tennis.Tiebreak(first_server_points=5, first_returner_points=7).winner())
    self.assertFalse(tennis.Tiebreak(first_server_points=6, first_returner_points=8).winner())

  def test_point(self):
    with self.assertRaises(
      RuntimeError,
      msg='Cannot advance this tiebreak\'s score because the tiebreak is over.'
    ):
      tennis.Tiebreak(
        first_server_points=3,
        first_returner_points=1,
        target_points=3
      ).point(first_server=True)

    tiebreak = tennis.Tiebreak()
    self.assertIsNone(tiebreak.point(first_server=True))
    self.assertEqual(tiebreak, tennis.Tiebreak(first_server_points=1, first_returner_points=0))
    self.assertIsNone(tiebreak.point(first_server=False))
    self.assertEqual(tiebreak, tennis.Tiebreak(first_server_points=1, first_returner_points=1))
    self.assertIsNone(tiebreak.point(first_server=True))
    self.assertEqual(tiebreak, tennis.Tiebreak(first_server_points=2, first_returner_points=1))
    self.assertIsNone(tiebreak.point(first_server=True))
    self.assertEqual(tiebreak, tennis.Tiebreak(first_server_points=3, first_returner_points=1))
    self.assertIsNone(tiebreak.point(first_server=True))
    self.assertEqual(tiebreak, tennis.Tiebreak(first_server_points=4, first_returner_points=1))
    self.assertIsNone(tiebreak.point(first_server=True))
    self.assertEqual(tiebreak, tennis.Tiebreak(first_server_points=5, first_returner_points=1))
    self.assertIsNone(tiebreak.point(first_server=True))
    self.assertEqual(tiebreak, tennis.Tiebreak(first_server_points=6, first_returner_points=1))
    self.assertTrue(tiebreak.point(first_server=True))
    self.assertEqual(tiebreak, tennis.Tiebreak(first_server_points=7, first_returner_points=1))

    tiebreak = tennis.Tiebreak(first_server_points=0, first_returner_points=1, target_points=3)
    self.assertIsNone(tiebreak.point(first_server=True))
    self.assertEqual(
      tiebreak,
      tennis.Tiebreak(first_server_points=1, first_returner_points=1, target_points=3)
    )
    self.assertIsNone(tiebreak.point(first_server=False))
    self.assertEqual(
      tiebreak,
      tennis.Tiebreak(first_server_points=1, first_returner_points=2, target_points=3)
    )
    self.assertFalse(tiebreak.point(first_server=False))
    self.assertEqual(
      tiebreak,
      tennis.Tiebreak(first_server_points=1, first_returner_points=3, target_points=3)
    )

  def test_str(self):
    self.assertEqual(
      str(tennis.Tiebreak(first_server_points=1, first_returner_points=2, target_points=3)),
      'Tiebreak(first_server_points=1, first_returner_points=2, target_points=3)'
    )

  def test_repr(self):
    self.assertEqual(
      repr(tennis.Tiebreak(first_server_points=1, first_returner_points=2, target_points=3)),
      'Tiebreak(first_server_points=1, first_returner_points=2, target_points=3)'
    )

  def test_eq(self):
    self.assertEqual(
      tennis.Tiebreak(first_server_points=1, first_returner_points=2),
      tennis.Tiebreak(first_server_points=1, first_returner_points=2)
    )
    self.assertNotEqual(
      tennis.Tiebreak(first_server_points=1, first_returner_points=2),
      tennis.Tiebreak(first_server_points=2, first_returner_points=1)
    )

if __name__ == '__main__':
  unittest.main()
