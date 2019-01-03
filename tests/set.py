import unittest

import tennis

class Set(unittest.TestCase):
  def test_init_no_args(self):
    zet = tennis.Set()

    self.assertEqual(zet.games, [tennis.Game(server_points=0, returner_points=0)])
    self.assertEqual(zet.tiebreak_games, 6)
    self.assertEqual(zet.tiebreak_points, 7)

  def test_init_args(self):
    zet = tennis.Set([tennis.Game(server_points=1, returner_points=2)], 3, 4)

    self.assertEqual(zet.games, [tennis.Game(server_points=1, returner_points=2)])
    self.assertEqual(zet.tiebreak_games, 3)
    self.assertEqual(zet.tiebreak_points, 4)

  def test_init_kwargs(self):
    zet = tennis.Set(
      tiebreak_points=1,
      tiebreak_games=2,
      games=[tennis.Game(server_points=3, returner_points=4)]
    )

    self.assertEqual(zet.games, [tennis.Game(server_points=3, returner_points=4)])
    self.assertEqual(zet.tiebreak_games, 2)
    self.assertEqual(zet.tiebreak_points, 1)

  def test_init_inconsistent_tiebreak_args(self):
    with self.assertRaises(
      RuntimeError,
      msg='tiebreak_games and tiebreak_points must both be None or non-None.'
    ):
      tennis.Set(tiebreak_games=1, tiebreak_points=None)

    with self.assertRaises(
      RuntimeError,
      msg='tiebreak_games and tiebreak_points must both be None or non-None.'
    ):
      tennis.Set(tiebreak_games=None, tiebreak_points=1)

  def test_init_negative_points(self):
    with self.assertRaises(RuntimeError, msg='Point scores must be non-negative.'):
      tennis.Set(tiebreak_games=-1, tiebreak_points=1)

    with self.assertRaises(RuntimeError, msg='Point scores must be non-negative.'):
      tennis.Set(tiebreak_games=1, tiebreak_points=-1)

  def test_init_first_game(self):
    zet = tennis.Set(games=None, tiebreak_games=1, tiebreak_points=2)

    self.assertEqual(zet.games, [tennis.Game()])
    self.assertEqual(zet.tiebreak_games, 1)
    self.assertEqual(zet.tiebreak_points, 2)

    zet = tennis.Set(games=None, tiebreak_games=None, tiebreak_points=None)

    self.assertEqual(zet.games, [tennis.Game()])
    self.assertIsNone(zet.tiebreak_games)
    self.assertIsNone(zet.tiebreak_points)

  def test_test_init_first_tiebreak(self):
    zet = tennis.Set(games=None, tiebreak_games=0, tiebreak_points=3)

    self.assertEqual(zet.games, [tennis.Tiebreak(0, 0, 3)])
    self.assertEqual(zet.tiebreak_games, 0)
    self.assertEqual(zet.tiebreak_points, 3)

  def test_first_server_games(self):
    self.assertEqual(tennis.Set([]).first_server_games(), 0)

    self.assertEqual(tennis.Set().first_server_games(), 0)
    self.assertEqual(
      tennis.Set([tennis.Game(server_points=0, returner_points=4)]).first_server_games(),
      0
    )
    self.assertEqual(
      tennis.Set([tennis.Game(server_points=4, returner_points=0)]).first_server_games(),
      1
    )

    self.assertEqual(
      tennis.Set(
        [tennis.Game(server_points=0, returner_points=4), tennis.Game()]
      ).first_server_games(),
      0
    )
    self.assertEqual(
      tennis.Set(
        [
          tennis.Game(server_points=0, returner_points=4),
          tennis.Game(server_points=0, returner_points=4)
        ]
      ).first_server_games(),
      1
    )
    self.assertEqual(
      tennis.Set(
        [
          tennis.Game(server_points=0, returner_points=4),
          tennis.Game(server_points=4, returner_points=0)
        ]
      ).first_server_games(),
      0
    )

    self.assertEqual(
      tennis.Set(
        [
          tennis.Game(server_points=0, returner_points=4),
          tennis.Game(server_points=4, returner_points=0),
          tennis.Tiebreak(0, 0, 7)
        ]
      ).first_server_games(),
      0
    )
    self.assertEqual(
      tennis.Set(
        [
          tennis.Game(server_points=0, returner_points=4),
          tennis.Game(server_points=4, returner_points=0),
          tennis.Tiebreak(0, 7, 7)
        ]
      ).first_server_games(),
      0
    )
    self.assertEqual(
      tennis.Set(
        [
          tennis.Game(server_points=0, returner_points=4),
          tennis.Game(server_points=4, returner_points=0),
          tennis.Tiebreak(7, 0, 7)
        ]
      ).first_server_games(),
      1
    )

    self.assertEqual(
      tennis.Set(
        [tennis.Game(server_points=4, returner_points=0), tennis.Game()]
      ).first_server_games(),
      1
    )
    self.assertEqual(
      tennis.Set(
        [
          tennis.Game(server_points=4, returner_points=0),
          tennis.Game(server_points=0, returner_points=4)
        ]
      ).first_server_games(),
      2
    )
    self.assertEqual(
      tennis.Set(
        [
          tennis.Game(server_points=4, returner_points=0),
          tennis.Game(server_points=4, returner_points=0)
        ]
      ).first_server_games(),
      1
    )

    self.assertEqual(
      tennis.Set(
        [
          tennis.Game(server_points=4, returner_points=0),
          tennis.Game(server_points=4, returner_points=0),
          tennis.Tiebreak(0, 0, 7)
        ]
      ).first_server_games(),
      1
    )
    self.assertEqual(
      tennis.Set(
        [
          tennis.Game(server_points=4, returner_points=0),
          tennis.Game(server_points=4, returner_points=0),
          tennis.Tiebreak(0, 7, 7)
        ]
      ).first_server_games(),
      1
    )
    self.assertEqual(
      tennis.Set(
        [
          tennis.Game(server_points=4, returner_points=0),
          tennis.Game(server_points=4, returner_points=0),
          tennis.Tiebreak(7, 0, 7)
        ]
      ).first_server_games(),
      2
    )

  def test_first_returner_games(self):
    self.assertEqual(tennis.Set([]).first_returner_games(), 0)

    self.assertEqual(tennis.Set().first_returner_games(), 0)
    self.assertEqual(
      tennis.Set([tennis.Game(server_points=0, returner_points=4)]).first_returner_games(),
      1
    )
    self.assertEqual(
      tennis.Set([tennis.Game(server_points=4, returner_points=0)]).first_returner_games(),
      0
    )

    self.assertEqual(
      tennis.Set(
        [tennis.Game(server_points=0, returner_points=4), tennis.Game()]
      ).first_returner_games(),
      1
    )
    self.assertEqual(
      tennis.Set(
        [
          tennis.Game(server_points=0, returner_points=4),
          tennis.Game(server_points=0, returner_points=4)
        ]
      ).first_returner_games(),
      1
    )
    self.assertEqual(
      tennis.Set(
        [
          tennis.Game(server_points=0, returner_points=4),
          tennis.Game(server_points=4, returner_points=0)
        ]
      ).first_returner_games(),
      2
    )

    self.assertEqual(
      tennis.Set(
        [
          tennis.Game(server_points=0, returner_points=4),
          tennis.Game(server_points=4, returner_points=0),
          tennis.Tiebreak(0, 0, 7)
        ]
      ).first_returner_games(),
      2
    )
    self.assertEqual(
      tennis.Set(
        [
          tennis.Game(server_points=0, returner_points=4),
          tennis.Game(server_points=4, returner_points=0),
          tennis.Tiebreak(0, 7, 7)
        ]
      ).first_returner_games(),
      3
    )
    self.assertEqual(
      tennis.Set(
        [
          tennis.Game(server_points=0, returner_points=4),
          tennis.Game(server_points=4, returner_points=0),
          tennis.Tiebreak(7, 0, 7)
        ]
      ).first_returner_games(),
      2
    )

    self.assertEqual(
      tennis.Set(
        [tennis.Game(server_points=4, returner_points=0), tennis.Game()]
      ).first_returner_games(),
      0
    )
    self.assertEqual(
      tennis.Set(
        [
          tennis.Game(server_points=4, returner_points=0),
          tennis.Game(server_points=0, returner_points=4)
        ]
      ).first_returner_games(),
      0
    )
    self.assertEqual(
      tennis.Set(
        [
          tennis.Game(server_points=4, returner_points=0),
          tennis.Game(server_points=4, returner_points=0)
        ]
      ).first_returner_games(),
      1
    )

    self.assertEqual(
      tennis.Set(
        [
          tennis.Game(server_points=4, returner_points=0),
          tennis.Game(server_points=4, returner_points=0),
          tennis.Tiebreak(0, 0, 7)
        ]
      ).first_returner_games(),
      1
    )
    self.assertEqual(
      tennis.Set(
        [
          tennis.Game(server_points=4, returner_points=0),
          tennis.Game(server_points=4, returner_points=0),
          tennis.Tiebreak(0, 7, 7)
        ]
      ).first_returner_games(),
      2
    )
    self.assertEqual(
      tennis.Set(
        [
          tennis.Game(server_points=4, returner_points=0),
          tennis.Game(server_points=4, returner_points=0),
          tennis.Tiebreak(7, 0, 7)
        ]
      ).first_returner_games(),
      1
    )

  def test_winner(self):
    self.assertIsNone(tennis.Set(
      games=[tennis.Game(server_points=4, returner_points=0)] * 2 + [tennis.Tiebreak(0, 0, 2)],
      tiebreak_games=1,
      tiebreak_points=2
    ).winner())

    self.assertTrue(tennis.Set(
      games=[tennis.Tiebreak(2, 0, 0)],
      tiebreak_games=0,
      tiebreak_points=0
    ).winner())

    self.assertFalse(tennis.Set(
      games=[tennis.Game(server_points=4, returner_points=0)] * 4 + [tennis.Tiebreak(0, 4, 4)],
      tiebreak_games=2,
      tiebreak_points=4
    ).winner())

    self.assertIsNone(tennis.Set(
      [tennis.Game(server_points=4, returner_points=0)] * 10 + [tennis.Game()],
      False
    ).winner())

    self.assertIsNone(tennis.Set(
      [tennis.Game(server_points=4, returner_points=0)] * 11 + [tennis.Game()],
      False
    ).winner())

    self.assertIsNone(tennis.Set(
      [tennis.Game(server_points=4, returner_points=0)] * 12 + [tennis.Game()],
      False
    ).winner())

    self.assertIsNone(tennis.Set(
      [tennis.Game(server_points=4, returner_points=0)] * 13 + [tennis.Game()],
      False
    ).winner())

    self.assertTrue(tennis.Set(
      [tennis.Game(server_points=4, returner_points=0)] * 13 + \
        [tennis.Game(server_points=0, returner_points=4)],
      False
    ).winner())

    self.assertIsNone(tennis.Set(
      [tennis.Game(server_points=4, returner_points=0)] * 12 + \
        [tennis.Game(server_points=0, returner_points=4), tennis.Game()],
      False
    ).winner())

    self.assertFalse(tennis.Set(
      [tennis.Game(server_points=4, returner_points=0)] * 12 + [
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0)
      ],
      False
    ).winner())

  def test_point(self):
    with self.assertRaises(
      RuntimeError,
      msg='Cannot advance this set\'s score because the set is over.'
    ):
      tennis.Set([
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4)
      ] * 3).point(True)

    zet = tennis.Set()
    self.assertIsNone(zet.point(True))
    self.assertEqual(zet, tennis.Set([tennis.Game(server_points=1, returner_points=0)]))
    self.assertIsNone(zet.point(True))
    self.assertEqual(zet, tennis.Set([tennis.Game(server_points=2, returner_points=0)]))
    self.assertIsNone(zet.point(True))
    self.assertEqual(zet, tennis.Set([tennis.Game(server_points=3, returner_points=0)]))
    self.assertIsNone(zet.point(True))
    self.assertEqual(
      zet,
      tennis.Set([tennis.Game(server_points=4, returner_points=0), tennis.Game()])
    )
    self.assertIsNone(zet.point(True))
    self.assertEqual(
      zet,
      tennis.Set([
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=1)
      ])
    )
    self.assertIsNone(zet.point(True))
    self.assertEqual(
      zet,
      tennis.Set([
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=2)
      ])
    )
    self.assertIsNone(zet.point(True))
    self.assertEqual(
      zet,
      tennis.Set([
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=3)
      ])
    )
    self.assertIsNone(zet.point(True))
    self.assertEqual(
      zet,
      tennis.Set([
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game()
      ])
    )
    self.assertIsNone(zet.point(True))
    self.assertEqual(
      zet,
      tennis.Set([
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=1, returner_points=0)
      ])
    )
    self.assertIsNone(zet.point(True))
    self.assertEqual(
      zet,
      tennis.Set([
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=2, returner_points=0)
      ])
    )
    self.assertIsNone(zet.point(True))
    self.assertEqual(
      zet,
      tennis.Set([
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=3, returner_points=0)
      ])
    )
    self.assertIsNone(zet.point(True))
    self.assertEqual(
      zet,
      tennis.Set([
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game()
      ])
    )
    self.assertIsNone(zet.point(True))
    self.assertEqual(
      zet,
      tennis.Set([
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=1)
      ])
    )
    self.assertIsNone(zet.point(True))
    self.assertEqual(
      zet,
      tennis.Set([
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=2)
      ])
    )
    self.assertIsNone(zet.point(True))
    self.assertEqual(
      zet,
      tennis.Set([
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=3)
      ])
    )
    self.assertIsNone(zet.point(True))
    self.assertEqual(
      zet,
      tennis.Set([
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game()
      ])
    )
    self.assertIsNone(zet.point(True))
    self.assertEqual(
      zet,
      tennis.Set([
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=1, returner_points=0)
      ])
    )
    self.assertIsNone(zet.point(True))
    self.assertEqual(
      zet,
      tennis.Set([
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=2, returner_points=0)
      ])
    )
    self.assertIsNone(zet.point(True))
    self.assertEqual(
      zet,
      tennis.Set([
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=3, returner_points=0)
      ])
    )
    self.assertIsNone(zet.point(True))
    self.assertEqual(
      zet,
      tennis.Set([
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game()
      ])
    )
    self.assertIsNone(zet.point(True))
    self.assertEqual(
      zet,
      tennis.Set([
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=1)
      ])
    )
    self.assertIsNone(zet.point(True))
    self.assertEqual(
      zet,
      tennis.Set([
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=2)
      ])
    )
    self.assertIsNone(zet.point(True))
    self.assertEqual(
      zet,
      tennis.Set([
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=3)
      ])
    )
    self.assertTrue(zet.point(True))
    self.assertEqual(
      zet,
      tennis.Set([
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4)
      ])
    )

    zet = tennis.Set()
    self.assertIsNone(zet.point(False))
    self.assertEqual(zet, tennis.Set([tennis.Game(server_points=0, returner_points=1)]))
    self.assertIsNone(zet.point(False))
    self.assertEqual(zet, tennis.Set([tennis.Game(server_points=0, returner_points=2)]))
    self.assertIsNone(zet.point(False))
    self.assertEqual(zet, tennis.Set([tennis.Game(server_points=0, returner_points=3)]))
    self.assertIsNone(zet.point(False))
    self.assertEqual(
      zet,
      tennis.Set([tennis.Game(server_points=0, returner_points=4), tennis.Game()])
    )
    self.assertIsNone(zet.point(False))
    self.assertEqual(
      zet,
      tennis.Set([
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=1, returner_points=0)
      ])
    )
    self.assertIsNone(zet.point(False))
    self.assertEqual(
      zet,
      tennis.Set([
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=2, returner_points=0)
      ])
    )
    self.assertIsNone(zet.point(False))
    self.assertEqual(
      zet,
      tennis.Set([
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=3, returner_points=0)
      ])
    )
    self.assertIsNone(zet.point(False))
    self.assertEqual(
      zet,
      tennis.Set([
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game()
      ])
    )
    self.assertIsNone(zet.point(False))
    self.assertEqual(
      zet,
      tennis.Set([
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=1)
      ])
    )
    self.assertIsNone(zet.point(False))
    self.assertEqual(
      zet,
      tennis.Set([
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=2)
      ])
    )
    self.assertIsNone(zet.point(False))
    self.assertEqual(
      zet,
      tennis.Set([
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=3)
      ])
    )
    self.assertIsNone(zet.point(False))
    self.assertEqual(
      zet,
      tennis.Set([
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game()
      ])
    )
    self.assertIsNone(zet.point(False))
    self.assertEqual(
      zet,
      tennis.Set([
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=1, returner_points=0)
      ])
    )
    self.assertIsNone(zet.point(False))
    self.assertEqual(
      zet,
      tennis.Set([
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=2, returner_points=0)
      ])
    )
    self.assertIsNone(zet.point(False))
    self.assertEqual(
      zet,
      tennis.Set([
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=3, returner_points=0)
      ])
    )
    self.assertIsNone(zet.point(False))
    self.assertEqual(
      zet,
      tennis.Set([
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game()
      ])
    )
    self.assertIsNone(zet.point(False))
    self.assertEqual(
      zet,
      tennis.Set([
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=1)
      ])
    )
    self.assertIsNone(zet.point(False))
    self.assertEqual(
      zet,
      tennis.Set([
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=2)
      ])
    )
    self.assertIsNone(zet.point(False))
    self.assertEqual(
      zet,
      tennis.Set([
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=3)
      ])
    )
    self.assertIsNone(zet.point(False))
    self.assertEqual(
      zet,
      tennis.Set([
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game()
      ])
    )
    self.assertIsNone(zet.point(False))
    self.assertEqual(
      zet,
      tennis.Set([
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=1, returner_points=0)
      ])
    )
    self.assertIsNone(zet.point(False))
    self.assertEqual(
      zet,
      tennis.Set([
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=2, returner_points=0)
      ])
    )
    self.assertIsNone(zet.point(False))
    self.assertEqual(
      zet,
      tennis.Set([
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=3, returner_points=0)
      ])
    )
    self.assertFalse(zet.point(False))
    self.assertEqual(
      zet,
      tennis.Set([
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0)
      ])
    )

    zet = tennis.Set(
      [tennis.Game(server_points=4, returner_points=0)] * 3 + \
        [tennis.Game(server_points=3, returner_points=0)],
      2,
      3
    )
    self.assertIsNone(zet.point(False))
    self.assertEqual(
      zet,
      tennis.Set(
        [tennis.Game(server_points=4, returner_points=0)] * 4 + [tennis.Tiebreak(0, 0, 3)],
        2,
        3
      )
    )
    self.assertIsNone(zet.point(True))
    self.assertEqual(
      zet,
      tennis.Set(
        [tennis.Game(server_points=4, returner_points=0)] * 4 + [tennis.Tiebreak(1, 0, 3)],
        2,
        3
      )
    )
    self.assertIsNone(zet.point(True))
    self.assertEqual(
      zet,
      tennis.Set(
        [tennis.Game(server_points=4, returner_points=0)] * 4 + [tennis.Tiebreak(2, 0, 3)],
        2,
        3
      )
    )
    self.assertTrue(zet.point(True))
    self.assertEqual(
      zet,
      tennis.Set(
        [tennis.Game(server_points=4, returner_points=0)] * 4 + [tennis.Tiebreak(3, 0, 3)],
        2,
        3
      )
    )

    zet = tennis.Set(
      [
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=3, returner_points=0)
      ],
      1,
      2
    )
    self.assertIsNone(zet.point(False))
    self.assertEqual(
      zet,
      tennis.Set(
        [tennis.Game(server_points=4, returner_points=0)] * 2 + [tennis.Tiebreak(0, 0, 2)],
        1,
        2
      )
    )
    self.assertIsNone(zet.point(False))
    self.assertEqual(
      zet,
      tennis.Set(
        [tennis.Game(server_points=4, returner_points=0)] * 2 + [tennis.Tiebreak(0, 1, 2)],
        1,
        2
      )
    )
    self.assertFalse(zet.point(False))
    self.assertEqual(
      zet,
      tennis.Set(
        [tennis.Game(server_points=4, returner_points=0)] * 2 + [tennis.Tiebreak(0, 2, 2)],
        1,
        2
      )
    )

  def test_str(self):
    self.assertEqual(
      str(tennis.Set([], 1, 2)),
      'Set(games=[], tiebreak_games=1, tiebreak_points=2)'
    )
    self.assertEqual(
      str(tennis.Set([tennis.Game(server_points=1, returner_points=2)], 3, 4)),
      'Set('
        'games=[Game(server_points=1, returner_points=2, deciding_point=False)], '
        'tiebreak_games=3, '
        'tiebreak_points=4'
      ')'
    )
    self.assertEqual(
      str(tennis.Set(
        [tennis.Game(server_points=1, returner_points=2), tennis.Tiebreak(3, 4, 7)],
        5,
        7
      )),
      'Set('
        'games=['
          'Game(server_points=1, returner_points=2, deciding_point=False), '
          'Tiebreak(first_server_points=3, first_returner_points=4, target_points=7)'
        '], '
        'tiebreak_games=5, '
        'tiebreak_points=7'
      ')'
    )

  def test_repr(self):
    self.assertEqual(
      repr(tennis.Set([], 1, 2)),
      'Set(games=[], tiebreak_games=1, tiebreak_points=2)'
    )
    self.assertEqual(
      repr(tennis.Set([tennis.Game(server_points=1, returner_points=2)], 3, 4)),
      'Set('
        'games=[Game(server_points=1, returner_points=2, deciding_point=False)], '
        'tiebreak_games=3, '
        'tiebreak_points=4'
      ')'
    )
    self.assertEqual(
      repr(tennis.Set(
        [tennis.Game(server_points=1, returner_points=2), tennis.Tiebreak(3, 4, 7)],
        5,
        7
      )),
      'Set('
        'games=['
          'Game(server_points=1, returner_points=2, deciding_point=False), '
          'Tiebreak(first_server_points=3, first_returner_points=4, target_points=7)'
        '], '
        'tiebreak_games=5, '
        'tiebreak_points=7'
      ')'
    )

  def test_eq(self):
    self.assertEqual(tennis.Set([], True), tennis.Set([], True))
    self.assertEqual(
      tennis.Set([tennis.Game(server_points=1, returner_points=2)], False),
      tennis.Set([tennis.Game(server_points=1, returner_points=2)], False)
    )
    self.assertNotEqual(tennis.Set([], True), tennis.Set([], False))
    self.assertNotEqual(
      tennis.Set([], True),
      tennis.Set([tennis.Game(server_points=1, returner_points=2)], True)
    )

if __name__ == '__main__':
  unittest.main()
