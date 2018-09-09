import unittest

import tennis

class Set(unittest.TestCase):
  def test_init_no_args(self):
    zet = tennis.Set()

    self.assertEqual(zet.games, [tennis.Game(0, 0)])
    self.assertEqual(zet.tiebreak, True)

  def test_init_args(self):
    zet = tennis.Set([tennis.Game(1, 2)], False)

    self.assertEqual(zet.games, [tennis.Game(1, 2)])
    self.assertEqual(zet.tiebreak, False)

  def test_init_kwargs(self):
    zet = tennis.Set(tiebreak=False, games=[tennis.Game(3, 4)])

    self.assertEqual(zet.games, [tennis.Game(3, 4)])
    self.assertEqual(zet.tiebreak, False)

if __name__ == '__main__':
  unittest.main()
