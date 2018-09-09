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

  def test_first_server_games(self):
    self.assertEqual(tennis.Set([]).first_server_games(), 0)

    self.assertEqual(tennis.Set().first_server_games(), 0)
    self.assertEqual(tennis.Set([tennis.Game(0, 4)]).first_server_games(), 0)
    self.assertEqual(tennis.Set([tennis.Game(4, 0)]).first_server_games(), 1)

    self.assertEqual(
      tennis.Set([tennis.Game(0, 4), tennis.Game()]).first_server_games(),
      0
    )
    self.assertEqual(
      tennis.Set([tennis.Game(0, 4), tennis.Game(0, 4)]).first_server_games(),
      1
    )
    self.assertEqual(
      tennis.Set([tennis.Game(0, 4), tennis.Game(4, 0)]).first_server_games(),
      0
    )

    self.assertEqual(
      tennis.Set(
        [tennis.Game(0, 4), tennis.Game(4, 0), tennis.Tiebreak()]
      ).first_server_games(),
      0
    )
    self.assertEqual(
      tennis.Set(
        [tennis.Game(0, 4), tennis.Game(4, 0), tennis.Tiebreak(0, 7)]
      ).first_server_games(),
      0
    )
    self.assertEqual(
      tennis.Set(
        [tennis.Game(0, 4), tennis.Game(4, 0), tennis.Tiebreak(7, 0)]
      ).first_server_games(),
      1
    )

    self.assertEqual(
      tennis.Set([tennis.Game(4, 0), tennis.Game()]).first_server_games(),
      1
    )
    self.assertEqual(
      tennis.Set([tennis.Game(4, 0), tennis.Game(0, 4)]).first_server_games(),
      2
    )
    self.assertEqual(
      tennis.Set([tennis.Game(4, 0), tennis.Game(4, 0)]).first_server_games(),
      1
    )

    self.assertEqual(
      tennis.Set(
        [tennis.Game(4, 0), tennis.Game(4, 0), tennis.Tiebreak()]
      ).first_server_games(),
      1
    )
    self.assertEqual(
      tennis.Set(
        [tennis.Game(4, 0), tennis.Game(4, 0), tennis.Tiebreak(0, 7)]
      ).first_server_games(),
      1
    )
    self.assertEqual(
      tennis.Set(
        [tennis.Game(4, 0), tennis.Game(4, 0), tennis.Tiebreak(7, 0)]
      ).first_server_games(),
      2
    )

  def test_first_returner_games(self):
    self.assertEqual(tennis.Set([]).first_returner_games(), 0)

    self.assertEqual(tennis.Set().first_returner_games(), 0)
    self.assertEqual(tennis.Set([tennis.Game(0, 4)]).first_returner_games(), 1)
    self.assertEqual(tennis.Set([tennis.Game(4, 0)]).first_returner_games(), 0)

    self.assertEqual(
      tennis.Set([tennis.Game(0, 4), tennis.Game()]).first_returner_games(),
      1
    )
    self.assertEqual(
      tennis.Set([tennis.Game(0, 4), tennis.Game(0, 4)]).first_returner_games(),
      1
    )
    self.assertEqual(
      tennis.Set([tennis.Game(0, 4), tennis.Game(4, 0)]).first_returner_games(),
      2
    )

    self.assertEqual(
      tennis.Set(
        [tennis.Game(0, 4), tennis.Game(4, 0), tennis.Tiebreak()]
      ).first_returner_games(),
      2
    )
    self.assertEqual(
      tennis.Set(
        [tennis.Game(0, 4), tennis.Game(4, 0), tennis.Tiebreak(0, 7)]
      ).first_returner_games(),
      3
    )
    self.assertEqual(
      tennis.Set(
        [tennis.Game(0, 4), tennis.Game(4, 0), tennis.Tiebreak(7, 0)]
      ).first_returner_games(),
      2
    )

    self.assertEqual(
      tennis.Set([tennis.Game(4, 0), tennis.Game()]).first_returner_games(),
      0
    )
    self.assertEqual(
      tennis.Set([tennis.Game(4, 0), tennis.Game(0, 4)]).first_returner_games(),
      0
    )
    self.assertEqual(
      tennis.Set([tennis.Game(4, 0), tennis.Game(4, 0)]).first_returner_games(),
      1
    )

    self.assertEqual(
      tennis.Set(
        [tennis.Game(4, 0), tennis.Game(4, 0), tennis.Tiebreak()]
      ).first_returner_games(),
      1
    )
    self.assertEqual(
      tennis.Set(
        [tennis.Game(4, 0), tennis.Game(4, 0), tennis.Tiebreak(0, 7)]
      ).first_returner_games(),
      2
    )
    self.assertEqual(
      tennis.Set(
        [tennis.Game(4, 0), tennis.Game(4, 0), tennis.Tiebreak(7, 0)]
      ).first_returner_games(),
      1
    )

if __name__ == '__main__':
  unittest.main()
