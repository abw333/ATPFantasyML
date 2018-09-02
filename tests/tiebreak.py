import unittest

import tennis

class Tiebreak(unittest.TestCase):
  def test_init_no_args(self):
    tiebreak = tennis.Tiebreak()

    self.assertEqual(tiebreak.first_server_points, 0)
    self.assertEqual(tiebreak.first_returner_points, 0)

  def test_init_args(self):
    tiebreak = tennis.Tiebreak(1, 2)

    self.assertEqual(tiebreak.first_server_points, 1)
    self.assertEqual(tiebreak.first_returner_points, 2)

  def test_init_kwargs(self):
    tiebreak = tennis.Tiebreak(first_returner_points=4, first_server_points=3)

    self.assertEqual(tiebreak.first_server_points, 3)
    self.assertEqual(tiebreak.first_returner_points, 4)

  def test_winner(self):
    self.assertIsNone(tennis.Tiebreak(0, 0).winner())
    self.assertIsNone(tennis.Tiebreak(7, 6).winner())
    self.assertIsNone(tennis.Tiebreak(6, 7).winner())

    self.assertTrue(tennis.Tiebreak(7, 0).winner())
    self.assertTrue(tennis.Tiebreak(7, 5).winner())
    self.assertTrue(tennis.Tiebreak(8, 6).winner())

    self.assertFalse(tennis.Tiebreak(0, 7).winner())
    self.assertFalse(tennis.Tiebreak(5, 7).winner())
    self.assertFalse(tennis.Tiebreak(6, 8).winner())

  def test_point(self):
    with self.assertRaises(
      RuntimeError,
      msg='Cannot advance this tiebreak\'s score because the tiebreak is over.'
    ):
      tennis.Tiebreak(7, 0).point(True)

    tiebreak = tennis.Tiebreak(0, 0)
    self.assertIsNone(tiebreak.point(True))
    self.assertEqual(tiebreak.first_server_points, 1)
    self.assertEqual(tiebreak.first_returner_points, 0)
    self.assertIsNone(tiebreak.point(False))
    self.assertEqual(tiebreak.first_server_points, 1)
    self.assertEqual(tiebreak.first_returner_points, 1)

    self.assertTrue(tennis.Tiebreak(6, 0).point(True))
    self.assertFalse(tennis.Tiebreak(0, 6).point(False))

  def test_str(self):
    self.assertEqual(
      str(tennis.Tiebreak(1, 2)),
      'Tiebreak(first_server_points=1, first_returner_points=2)'
    )

if __name__ == '__main__':
  unittest.main()
