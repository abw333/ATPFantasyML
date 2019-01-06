import unittest

import tennis

class Set(unittest.TestCase):
  def test_init_no_args(self):
    zet = tennis.Set()

    self.assertEqual(zet.games, [tennis.Game(server_points=0, returner_points=0)])
    self.assertEqual(zet.target_games, 6)
    self.assertFalse(zet.deciding_point)
    self.assertEqual(zet.tiebreak_games, 6)
    self.assertEqual(zet.tiebreak_points, 7)

  def test_init_args(self):
    with self.assertRaises(
      TypeError,
      msg='__init__() takes 1 positional argument but 2 were given'
    ):
      tennis.Set([tennis.Game(server_points=1, returner_points=2)])

  def test_init_kwargs(self):
    zet = tennis.Set(
      tiebreak_points=1,
      tiebreak_games=2,
      deciding_point=True,
      target_games=3,
      games=[tennis.Game(server_points=3, returner_points=4)]
    )

    self.assertEqual(zet.games, [tennis.Game(server_points=3, returner_points=4)])
    self.assertEqual(zet.target_games, 3)
    self.assertTrue(zet.deciding_point)
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
      tennis.Set(target_games=-1)

    with self.assertRaises(RuntimeError, msg='Point scores must be non-negative.'):
      tennis.Set(tiebreak_games=-1, tiebreak_points=1)

    with self.assertRaises(RuntimeError, msg='Point scores must be non-negative.'):
      tennis.Set(tiebreak_games=1, tiebreak_points=-1)

  def test_init_first_game(self):
    zet = tennis.Set(games=None, deciding_point=False, tiebreak_games=1, tiebreak_points=2)

    self.assertEqual(zet.games, [tennis.Game(deciding_point=False)])
    self.assertEqual(zet.tiebreak_games, 1)
    self.assertEqual(zet.tiebreak_points, 2)

    zet = tennis.Set(games=None, deciding_point=True, tiebreak_games=None, tiebreak_points=None)

    self.assertEqual(zet.games, [tennis.Game(deciding_point=True)])
    self.assertIsNone(zet.tiebreak_games)
    self.assertIsNone(zet.tiebreak_points)

  def test_test_init_first_tiebreak(self):
    zet = tennis.Set(games=None, tiebreak_games=0, tiebreak_points=3)

    self.assertEqual(
      zet.games,
      [tennis.Tiebreak(first_server_points=0, first_returner_points=0, target_points=3)]
    )
    self.assertEqual(zet.tiebreak_games, 0)
    self.assertEqual(zet.tiebreak_points, 3)

  def test_first_server_games(self):
    self.assertEqual(tennis.Set(games=[]).first_server_games(), 0)

    self.assertEqual(tennis.Set().first_server_games(), 0)
    self.assertEqual(
      tennis.Set(games=[tennis.Game(server_points=0, returner_points=4)]).first_server_games(),
      0
    )
    self.assertEqual(
      tennis.Set(games=[tennis.Game(server_points=4, returner_points=0)]).first_server_games(),
      1
    )

    self.assertEqual(
      tennis.Set(
        games=[tennis.Game(server_points=0, returner_points=4), tennis.Game()]
      ).first_server_games(),
      0
    )
    self.assertEqual(
      tennis.Set(
        games=[
          tennis.Game(server_points=0, returner_points=4),
          tennis.Game(server_points=0, returner_points=4)
        ]
      ).first_server_games(),
      1
    )
    self.assertEqual(
      tennis.Set(
        games=[
          tennis.Game(server_points=0, returner_points=4),
          tennis.Game(server_points=4, returner_points=0)
        ]
      ).first_server_games(),
      0
    )

    self.assertEqual(
      tennis.Set(
        games=[
          tennis.Game(server_points=0, returner_points=4),
          tennis.Game(server_points=4, returner_points=0),
          tennis.Tiebreak(first_server_points=0, first_returner_points=0, target_points=7)
        ]
      ).first_server_games(),
      0
    )
    self.assertEqual(
      tennis.Set(
        games=[
          tennis.Game(server_points=0, returner_points=4),
          tennis.Game(server_points=4, returner_points=0),
          tennis.Tiebreak(first_server_points=0, first_returner_points=7, target_points=7)
        ]
      ).first_server_games(),
      0
    )
    self.assertEqual(
      tennis.Set(
        games=[
          tennis.Game(server_points=0, returner_points=4),
          tennis.Game(server_points=4, returner_points=0),
          tennis.Tiebreak(first_server_points=7, first_returner_points=0, target_points=7)
        ]
      ).first_server_games(),
      1
    )

    self.assertEqual(
      tennis.Set(
        games=[tennis.Game(server_points=4, returner_points=0), tennis.Game()]
      ).first_server_games(),
      1
    )
    self.assertEqual(
      tennis.Set(
        games=[
          tennis.Game(server_points=4, returner_points=0),
          tennis.Game(server_points=0, returner_points=4)
        ]
      ).first_server_games(),
      2
    )
    self.assertEqual(
      tennis.Set(
        games=[
          tennis.Game(server_points=4, returner_points=0),
          tennis.Game(server_points=4, returner_points=0)
        ]
      ).first_server_games(),
      1
    )

    self.assertEqual(
      tennis.Set(
        games=[
          tennis.Game(server_points=4, returner_points=0),
          tennis.Game(server_points=4, returner_points=0),
          tennis.Tiebreak(first_server_points=0, first_returner_points=0, target_points=7)
        ]
      ).first_server_games(),
      1
    )
    self.assertEqual(
      tennis.Set(
        games=[
          tennis.Game(server_points=4, returner_points=0),
          tennis.Game(server_points=4, returner_points=0),
          tennis.Tiebreak(first_server_points=0, first_returner_points=7, target_points=7)
        ]
      ).first_server_games(),
      1
    )
    self.assertEqual(
      tennis.Set(
        games=[
          tennis.Game(server_points=4, returner_points=0),
          tennis.Game(server_points=4, returner_points=0),
          tennis.Tiebreak(first_server_points=7, first_returner_points=0, target_points=7)
        ]
      ).first_server_games(),
      2
    )

  def test_first_returner_games(self):
    self.assertEqual(tennis.Set(games=[]).first_returner_games(), 0)

    self.assertEqual(tennis.Set().first_returner_games(), 0)
    self.assertEqual(
      tennis.Set(games=[tennis.Game(server_points=0, returner_points=4)]).first_returner_games(),
      1
    )
    self.assertEqual(
      tennis.Set(games=[tennis.Game(server_points=4, returner_points=0)]).first_returner_games(),
      0
    )

    self.assertEqual(
      tennis.Set(
        games=[tennis.Game(server_points=0, returner_points=4), tennis.Game()]
      ).first_returner_games(),
      1
    )
    self.assertEqual(
      tennis.Set(
        games=[
          tennis.Game(server_points=0, returner_points=4),
          tennis.Game(server_points=0, returner_points=4)
        ]
      ).first_returner_games(),
      1
    )
    self.assertEqual(
      tennis.Set(
        games=[
          tennis.Game(server_points=0, returner_points=4),
          tennis.Game(server_points=4, returner_points=0)
        ]
      ).first_returner_games(),
      2
    )

    self.assertEqual(
      tennis.Set(
        games=[
          tennis.Game(server_points=0, returner_points=4),
          tennis.Game(server_points=4, returner_points=0),
          tennis.Tiebreak(first_server_points=0, first_returner_points=0, target_points=7)
        ]
      ).first_returner_games(),
      2
    )
    self.assertEqual(
      tennis.Set(
        games=[
          tennis.Game(server_points=0, returner_points=4),
          tennis.Game(server_points=4, returner_points=0),
          tennis.Tiebreak(first_server_points=0, first_returner_points=7, target_points=7)
        ]
      ).first_returner_games(),
      3
    )
    self.assertEqual(
      tennis.Set(
        games=[
          tennis.Game(server_points=0, returner_points=4),
          tennis.Game(server_points=4, returner_points=0),
          tennis.Tiebreak(first_server_points=7, first_returner_points=0, target_points=7)
        ]
      ).first_returner_games(),
      2
    )

    self.assertEqual(
      tennis.Set(
        games=[tennis.Game(server_points=4, returner_points=0), tennis.Game()]
      ).first_returner_games(),
      0
    )
    self.assertEqual(
      tennis.Set(
        games=[
          tennis.Game(server_points=4, returner_points=0),
          tennis.Game(server_points=0, returner_points=4)
        ]
      ).first_returner_games(),
      0
    )
    self.assertEqual(
      tennis.Set(
        games=[
          tennis.Game(server_points=4, returner_points=0),
          tennis.Game(server_points=4, returner_points=0)
        ]
      ).first_returner_games(),
      1
    )

    self.assertEqual(
      tennis.Set(
        games=[
          tennis.Game(server_points=4, returner_points=0),
          tennis.Game(server_points=4, returner_points=0),
          tennis.Tiebreak(first_server_points=0, first_returner_points=0, target_points=7)
        ]
      ).first_returner_games(),
      1
    )
    self.assertEqual(
      tennis.Set(
        games=[
          tennis.Game(server_points=4, returner_points=0),
          tennis.Game(server_points=4, returner_points=0),
          tennis.Tiebreak(first_server_points=0, first_returner_points=7, target_points=7)
        ]
      ).first_returner_games(),
      2
    )
    self.assertEqual(
      tennis.Set(
        games=[
          tennis.Game(server_points=4, returner_points=0),
          tennis.Game(server_points=4, returner_points=0),
          tennis.Tiebreak(first_server_points=7, first_returner_points=0, target_points=7)
        ]
      ).first_returner_games(),
      1
    )

  def test_winner(self):
    self.assertIsNone(tennis.Set(
      games=[tennis.Game(server_points=4, returner_points=0)] * 2 + \
        [tennis.Tiebreak(first_server_points=0, first_returner_points=0, target_points=2)],
      tiebreak_games=1,
      tiebreak_points=2
    ).winner())

    self.assertTrue(tennis.Set(
      games=[tennis.Tiebreak(first_server_points=2, first_returner_points=0, target_points=0)],
      tiebreak_games=0,
      tiebreak_points=0
    ).winner())

    self.assertFalse(tennis.Set(
      games=[tennis.Game(server_points=4, returner_points=0)] * 4 + \
        [tennis.Tiebreak(first_server_points=0, first_returner_points=4, target_points=4)],
      tiebreak_games=2,
      tiebreak_points=4
    ).winner())

    self.assertIsNone(tennis.Set(
      games=[tennis.Game(server_points=4, returner_points=0)] * 10 + [tennis.Game()],
      tiebreak_games=None,
      tiebreak_points=None
    ).winner())

    self.assertIsNone(tennis.Set(
      games=[tennis.Game(server_points=4, returner_points=0)] * 11 + [tennis.Game()],
      tiebreak_games=None,
      tiebreak_points=None
    ).winner())

    self.assertIsNone(tennis.Set(
      games=[tennis.Game(server_points=4, returner_points=0)] * 12 + [tennis.Game()],
      tiebreak_games=None,
      tiebreak_points=None
    ).winner())

    self.assertIsNone(tennis.Set(
      games=[tennis.Game(server_points=4, returner_points=0)] * 13 + [tennis.Game()],
      tiebreak_games=None,
      tiebreak_points=None
    ).winner())

    self.assertTrue(tennis.Set(
      games=[tennis.Game(server_points=4, returner_points=0)] * 13 + \
        [tennis.Game(server_points=0, returner_points=4)],
      tiebreak_games=None,
      tiebreak_points=None
    ).winner())

    self.assertIsNone(tennis.Set(
      games=[tennis.Game(server_points=4, returner_points=0)] * 12 + \
        [tennis.Game(server_points=0, returner_points=4), tennis.Game()],
      tiebreak_games=None,
      tiebreak_points=None
    ).winner())

    self.assertFalse(tennis.Set(
      games=[tennis.Game(server_points=4, returner_points=0)] * 12 + [
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0)
      ],
      tiebreak_games=None,
      tiebreak_points=None
    ).winner())

    self.assertTrue(tennis.Set(
      games=[
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4)
      ],
      target_games=2
    ).winner())

    self.assertFalse(tennis.Set(
      games=[
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0)
      ],
      target_games=2
    ).winner())

  def test_point(self):
    with self.assertRaises(
      RuntimeError,
      msg='Cannot advance this set\'s score because the set is over.'
    ):
      tennis.Set(games=[
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4)
      ] * 3).point(first_server=True)

    zet = tennis.Set(deciding_point=True)
    self.assertIsNone(zet.point(first_server=True))
    self.assertEqual(
      zet,
      tennis.Set(
        games=[tennis.Game(server_points=1, returner_points=0, deciding_point=True)],
        deciding_point=True
      )
    )
    self.assertIsNone(zet.point(first_server=True))
    self.assertEqual(
      zet,
      tennis.Set(
        games=[tennis.Game(server_points=2, returner_points=0, deciding_point=True)],
        deciding_point=True
      )
    )
    self.assertIsNone(zet.point(first_server=True))
    self.assertEqual(
      zet,
      tennis.Set(
        games=[tennis.Game(server_points=3, returner_points=0, deciding_point=True)],
        deciding_point=True
      )
    )
    self.assertIsNone(zet.point(first_server=True))
    self.assertEqual(
      zet,
      tennis.Set(
        games=[
          tennis.Game(server_points=4, returner_points=0, deciding_point=True),
          tennis.Game(deciding_point=True)
        ],
        deciding_point=True
      )
    )
    self.assertIsNone(zet.point(first_server=True))
    self.assertEqual(
      zet,
      tennis.Set(
        games=[
          tennis.Game(server_points=4, returner_points=0, deciding_point=True),
          tennis.Game(server_points=0, returner_points=1, deciding_point=True)
        ],
        deciding_point=True
      )
    )
    self.assertIsNone(zet.point(first_server=True))
    self.assertEqual(
      zet,
      tennis.Set(
        games=[
          tennis.Game(server_points=4, returner_points=0, deciding_point=True),
          tennis.Game(server_points=0, returner_points=2, deciding_point=True)
        ],
        deciding_point=True
      )
    )
    self.assertIsNone(zet.point(first_server=True))
    self.assertEqual(
      zet,
      tennis.Set(
        games=[
          tennis.Game(server_points=4, returner_points=0, deciding_point=True),
          tennis.Game(server_points=0, returner_points=3, deciding_point=True)
        ],
        deciding_point=True
      )
    )
    self.assertIsNone(zet.point(first_server=True))
    self.assertEqual(
      zet,
      tennis.Set(
        games=[
          tennis.Game(server_points=4, returner_points=0, deciding_point=True),
          tennis.Game(server_points=0, returner_points=4, deciding_point=True),
          tennis.Game(deciding_point=True)
        ],
        deciding_point=True
      )
    )
    self.assertIsNone(zet.point(first_server=True))
    self.assertEqual(
      zet,
      tennis.Set(
        games=[
          tennis.Game(server_points=4, returner_points=0, deciding_point=True),
          tennis.Game(server_points=0, returner_points=4, deciding_point=True),
          tennis.Game(server_points=1, returner_points=0, deciding_point=True)
        ],
        deciding_point=True
      )
    )
    self.assertIsNone(zet.point(first_server=True))
    self.assertEqual(
      zet,
      tennis.Set(
        games=[
          tennis.Game(server_points=4, returner_points=0, deciding_point=True),
          tennis.Game(server_points=0, returner_points=4, deciding_point=True),
          tennis.Game(server_points=2, returner_points=0, deciding_point=True)
        ],
        deciding_point=True
      )
    )
    self.assertIsNone(zet.point(first_server=True))
    self.assertEqual(
      zet,
      tennis.Set(
        games=[
          tennis.Game(server_points=4, returner_points=0, deciding_point=True),
          tennis.Game(server_points=0, returner_points=4, deciding_point=True),
          tennis.Game(server_points=3, returner_points=0, deciding_point=True)
        ],
        deciding_point=True
      )
    )
    self.assertIsNone(zet.point(first_server=True))
    self.assertEqual(
      zet,
      tennis.Set(
        games=[
          tennis.Game(server_points=4, returner_points=0, deciding_point=True),
          tennis.Game(server_points=0, returner_points=4, deciding_point=True),
          tennis.Game(server_points=4, returner_points=0, deciding_point=True),
          tennis.Game(deciding_point=True)
        ],
        deciding_point=True
      )
    )
    self.assertIsNone(zet.point(first_server=True))
    self.assertEqual(
      zet,
      tennis.Set(
        games=[
          tennis.Game(server_points=4, returner_points=0, deciding_point=True),
          tennis.Game(server_points=0, returner_points=4, deciding_point=True),
          tennis.Game(server_points=4, returner_points=0, deciding_point=True),
          tennis.Game(server_points=0, returner_points=1, deciding_point=True)
        ],
        deciding_point=True
      )
    )
    self.assertIsNone(zet.point(first_server=True))
    self.assertEqual(
      zet,
      tennis.Set(
        games=[
          tennis.Game(server_points=4, returner_points=0, deciding_point=True),
          tennis.Game(server_points=0, returner_points=4, deciding_point=True),
          tennis.Game(server_points=4, returner_points=0, deciding_point=True),
          tennis.Game(server_points=0, returner_points=2, deciding_point=True)
        ],
        deciding_point=True
      )
    )
    self.assertIsNone(zet.point(first_server=True))
    self.assertEqual(
      zet,
      tennis.Set(
        games=[
          tennis.Game(server_points=4, returner_points=0, deciding_point=True),
          tennis.Game(server_points=0, returner_points=4, deciding_point=True),
          tennis.Game(server_points=4, returner_points=0, deciding_point=True),
          tennis.Game(server_points=0, returner_points=3, deciding_point=True)
        ],
        deciding_point=True
      )
    )
    self.assertIsNone(zet.point(first_server=True))
    self.assertEqual(
      zet,
      tennis.Set(
        games=[
          tennis.Game(server_points=4, returner_points=0, deciding_point=True),
          tennis.Game(server_points=0, returner_points=4, deciding_point=True),
          tennis.Game(server_points=4, returner_points=0, deciding_point=True),
          tennis.Game(server_points=0, returner_points=4, deciding_point=True),
          tennis.Game(deciding_point=True)
        ],
        deciding_point=True
      )
    )
    self.assertIsNone(zet.point(first_server=True))
    self.assertEqual(
      zet,
      tennis.Set(
        games=[
          tennis.Game(server_points=4, returner_points=0, deciding_point=True),
          tennis.Game(server_points=0, returner_points=4, deciding_point=True),
          tennis.Game(server_points=4, returner_points=0, deciding_point=True),
          tennis.Game(server_points=0, returner_points=4, deciding_point=True),
          tennis.Game(server_points=1, returner_points=0, deciding_point=True)
        ],
        deciding_point=True
      )
    )
    self.assertIsNone(zet.point(first_server=True))
    self.assertEqual(
      zet,
      tennis.Set(
        games=[
          tennis.Game(server_points=4, returner_points=0, deciding_point=True),
          tennis.Game(server_points=0, returner_points=4, deciding_point=True),
          tennis.Game(server_points=4, returner_points=0, deciding_point=True),
          tennis.Game(server_points=0, returner_points=4, deciding_point=True),
          tennis.Game(server_points=2, returner_points=0, deciding_point=True)
        ],
        deciding_point=True
      )
    )
    self.assertIsNone(zet.point(first_server=True))
    self.assertEqual(
      zet,
      tennis.Set(
        games=[
          tennis.Game(server_points=4, returner_points=0, deciding_point=True),
          tennis.Game(server_points=0, returner_points=4, deciding_point=True),
          tennis.Game(server_points=4, returner_points=0, deciding_point=True),
          tennis.Game(server_points=0, returner_points=4, deciding_point=True),
          tennis.Game(server_points=3, returner_points=0, deciding_point=True)
        ],
        deciding_point=True
      )
    )
    self.assertIsNone(zet.point(first_server=True))
    self.assertEqual(
      zet,
      tennis.Set(
        games=[
          tennis.Game(server_points=4, returner_points=0, deciding_point=True),
          tennis.Game(server_points=0, returner_points=4, deciding_point=True),
          tennis.Game(server_points=4, returner_points=0, deciding_point=True),
          tennis.Game(server_points=0, returner_points=4, deciding_point=True),
          tennis.Game(server_points=4, returner_points=0, deciding_point=True),
          tennis.Game(deciding_point=True)
        ],
        deciding_point=True
      )
    )
    self.assertIsNone(zet.point(first_server=True))
    self.assertEqual(
      zet,
      tennis.Set(
        games=[
          tennis.Game(server_points=4, returner_points=0, deciding_point=True),
          tennis.Game(server_points=0, returner_points=4, deciding_point=True),
          tennis.Game(server_points=4, returner_points=0, deciding_point=True),
          tennis.Game(server_points=0, returner_points=4, deciding_point=True),
          tennis.Game(server_points=4, returner_points=0, deciding_point=True),
          tennis.Game(server_points=0, returner_points=1, deciding_point=True)
        ],
        deciding_point=True
      )
    )
    self.assertIsNone(zet.point(first_server=True))
    self.assertEqual(
      zet,
      tennis.Set(
        games=[
          tennis.Game(server_points=4, returner_points=0, deciding_point=True),
          tennis.Game(server_points=0, returner_points=4, deciding_point=True),
          tennis.Game(server_points=4, returner_points=0, deciding_point=True),
          tennis.Game(server_points=0, returner_points=4, deciding_point=True),
          tennis.Game(server_points=4, returner_points=0, deciding_point=True),
          tennis.Game(server_points=0, returner_points=2, deciding_point=True)
        ],
        deciding_point=True
      )
    )
    self.assertIsNone(zet.point(first_server=True))
    self.assertEqual(
      zet,
      tennis.Set(
        games=[
          tennis.Game(server_points=4, returner_points=0, deciding_point=True),
          tennis.Game(server_points=0, returner_points=4, deciding_point=True),
          tennis.Game(server_points=4, returner_points=0, deciding_point=True),
          tennis.Game(server_points=0, returner_points=4, deciding_point=True),
          tennis.Game(server_points=4, returner_points=0, deciding_point=True),
          tennis.Game(server_points=0, returner_points=3, deciding_point=True)
        ],
        deciding_point=True
      )
    )
    self.assertTrue(zet.point(first_server=True))
    self.assertEqual(
      zet,
      tennis.Set(
        games=[
          tennis.Game(server_points=4, returner_points=0, deciding_point=True),
          tennis.Game(server_points=0, returner_points=4, deciding_point=True),
          tennis.Game(server_points=4, returner_points=0, deciding_point=True),
          tennis.Game(server_points=0, returner_points=4, deciding_point=True),
          tennis.Game(server_points=4, returner_points=0, deciding_point=True),
          tennis.Game(server_points=0, returner_points=4, deciding_point=True)
        ],
        deciding_point=True
      )
    )

    zet = tennis.Set()
    self.assertIsNone(zet.point(first_server=False))
    self.assertEqual(zet, tennis.Set(games=[tennis.Game(server_points=0, returner_points=1)]))
    self.assertIsNone(zet.point(first_server=False))
    self.assertEqual(zet, tennis.Set(games=[tennis.Game(server_points=0, returner_points=2)]))
    self.assertIsNone(zet.point(first_server=False))
    self.assertEqual(zet, tennis.Set(games=[tennis.Game(server_points=0, returner_points=3)]))
    self.assertIsNone(zet.point(first_server=False))
    self.assertEqual(
      zet,
      tennis.Set(games=[tennis.Game(server_points=0, returner_points=4), tennis.Game()])
    )
    self.assertIsNone(zet.point(first_server=False))
    self.assertEqual(
      zet,
      tennis.Set(games=[
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=1, returner_points=0)
      ])
    )
    self.assertIsNone(zet.point(first_server=False))
    self.assertEqual(
      zet,
      tennis.Set(games=[
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=2, returner_points=0)
      ])
    )
    self.assertIsNone(zet.point(first_server=False))
    self.assertEqual(
      zet,
      tennis.Set(games=[
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=3, returner_points=0)
      ])
    )
    self.assertIsNone(zet.point(first_server=False))
    self.assertEqual(
      zet,
      tennis.Set(games=[
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game()
      ])
    )
    self.assertIsNone(zet.point(first_server=False))
    self.assertEqual(
      zet,
      tennis.Set(games=[
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=1)
      ])
    )
    self.assertIsNone(zet.point(first_server=False))
    self.assertEqual(
      zet,
      tennis.Set(games=[
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=2)
      ])
    )
    self.assertIsNone(zet.point(first_server=False))
    self.assertEqual(
      zet,
      tennis.Set(games=[
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=3)
      ])
    )
    self.assertIsNone(zet.point(first_server=False))
    self.assertEqual(
      zet,
      tennis.Set(games=[
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game()
      ])
    )
    self.assertIsNone(zet.point(first_server=False))
    self.assertEqual(
      zet,
      tennis.Set(games=[
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=1, returner_points=0)
      ])
    )
    self.assertIsNone(zet.point(first_server=False))
    self.assertEqual(
      zet,
      tennis.Set(games=[
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=2, returner_points=0)
      ])
    )
    self.assertIsNone(zet.point(first_server=False))
    self.assertEqual(
      zet,
      tennis.Set(games=[
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=3, returner_points=0)
      ])
    )
    self.assertIsNone(zet.point(first_server=False))
    self.assertEqual(
      zet,
      tennis.Set(games=[
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game()
      ])
    )
    self.assertIsNone(zet.point(first_server=False))
    self.assertEqual(
      zet,
      tennis.Set(games=[
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=1)
      ])
    )
    self.assertIsNone(zet.point(first_server=False))
    self.assertEqual(
      zet,
      tennis.Set(games=[
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=2)
      ])
    )
    self.assertIsNone(zet.point(first_server=False))
    self.assertEqual(
      zet,
      tennis.Set(games=[
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=3)
      ])
    )
    self.assertIsNone(zet.point(first_server=False))
    self.assertEqual(
      zet,
      tennis.Set(games=[
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game()
      ])
    )
    self.assertIsNone(zet.point(first_server=False))
    self.assertEqual(
      zet,
      tennis.Set(games=[
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=1, returner_points=0)
      ])
    )
    self.assertIsNone(zet.point(first_server=False))
    self.assertEqual(
      zet,
      tennis.Set(games=[
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=2, returner_points=0)
      ])
    )
    self.assertIsNone(zet.point(first_server=False))
    self.assertEqual(
      zet,
      tennis.Set(games=[
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=3, returner_points=0)
      ])
    )
    self.assertFalse(zet.point(first_server=False))
    self.assertEqual(
      zet,
      tennis.Set(games=[
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=0, returner_points=4),
        tennis.Game(server_points=4, returner_points=0)
      ])
    )

    zet = tennis.Set(
      games=[tennis.Game(server_points=4, returner_points=0)] * 3 + \
        [tennis.Game(server_points=3, returner_points=0)],
      tiebreak_games=2,
      tiebreak_points=3
    )
    self.assertIsNone(zet.point(first_server=False))
    self.assertEqual(
      zet,
      tennis.Set(
        games=[tennis.Game(server_points=4, returner_points=0)] * 4 + \
          [tennis.Tiebreak(first_server_points=0, first_returner_points=0, target_points=3)],
        tiebreak_games=2,
        tiebreak_points=3
      )
    )
    self.assertIsNone(zet.point(first_server=True))
    self.assertEqual(
      zet,
      tennis.Set(
        games=[tennis.Game(server_points=4, returner_points=0)] * 4 + \
          [tennis.Tiebreak(first_server_points=1, first_returner_points=0, target_points=3)],
        tiebreak_games=2,
        tiebreak_points=3
      )
    )
    self.assertIsNone(zet.point(first_server=True))
    self.assertEqual(
      zet,
      tennis.Set(
        games=[tennis.Game(server_points=4, returner_points=0)] * 4 + \
          [tennis.Tiebreak(first_server_points=2, first_returner_points=0, target_points=3)],
        tiebreak_games=2,
        tiebreak_points=3
      )
    )
    self.assertTrue(zet.point(first_server=True))
    self.assertEqual(
      zet,
      tennis.Set(
        games=[tennis.Game(server_points=4, returner_points=0)] * 4 + \
          [tennis.Tiebreak(first_server_points=3, first_returner_points=0, target_points=3)],
        tiebreak_games=2,
        tiebreak_points=3
      )
    )

    zet = tennis.Set(
      games=[
        tennis.Game(server_points=4, returner_points=0),
        tennis.Game(server_points=3, returner_points=0)
      ],
      tiebreak_games=1,
      tiebreak_points=2
    )
    self.assertIsNone(zet.point(first_server=False))
    self.assertEqual(
      zet,
      tennis.Set(
        games=[tennis.Game(server_points=4, returner_points=0)] * 2 + \
          [tennis.Tiebreak(first_server_points=0, first_returner_points=0, target_points=2)],
        tiebreak_games=1,
        tiebreak_points=2
      )
    )
    self.assertIsNone(zet.point(first_server=False))
    self.assertEqual(
      zet,
      tennis.Set(
        games=[tennis.Game(server_points=4, returner_points=0)] * 2 + \
          [tennis.Tiebreak(first_server_points=0, first_returner_points=1, target_points=2)],
        tiebreak_games=1,
        tiebreak_points=2
      )
    )
    self.assertFalse(zet.point(first_server=False))
    self.assertEqual(
      zet,
      tennis.Set(
        games=[tennis.Game(server_points=4, returner_points=0)] * 2 + \
          [tennis.Tiebreak(first_server_points=0, first_returner_points=2, target_points=2)],
        tiebreak_games=1,
        tiebreak_points=2
      )
    )

  def test_str(self):
    self.assertEqual(
      str(tennis.Set(
        games=[
          tennis.Game(server_points=1, returner_points=2, deciding_point=True),
          tennis.Tiebreak(first_server_points=3, first_returner_points=4, target_points=7)
        ],
        target_games=8,
        deciding_point=True,
        tiebreak_games=5,
        tiebreak_points=7
      )),
      'Set('
        'games=['
          'Game(server_points=1, returner_points=2, deciding_point=True), '
          'Tiebreak(first_server_points=3, first_returner_points=4, target_points=7)'
        '], '
        'target_games=8, '
        'deciding_point=True, '
        'tiebreak_games=5, '
        'tiebreak_points=7'
      ')'
    )

  def test_repr(self):
    self.assertEqual(
      repr(tennis.Set(
        games=[
          tennis.Game(server_points=1, returner_points=2, deciding_point=True),
          tennis.Tiebreak(first_server_points=3, first_returner_points=4, target_points=7)
        ],
        target_games=8,
        deciding_point=True,
        tiebreak_games=5,
        tiebreak_points=7
      )),
      'Set('
        'games=['
          'Game(server_points=1, returner_points=2, deciding_point=True), '
          'Tiebreak(first_server_points=3, first_returner_points=4, target_points=7)'
        '], '
        'target_games=8, '
        'deciding_point=True, '
        'tiebreak_games=5, '
        'tiebreak_points=7'
      ')'
    )

  def test_eq(self):
    self.assertEqual(
      tennis.Set(
        games=[tennis.Game(server_points=1, returner_points=2, deciding_point=True)],
        target_games=4,
        deciding_point=True,
        tiebreak_games=2,
        tiebreak_points=3
      ),
      tennis.Set(
        games=[tennis.Game(server_points=1, returner_points=2, deciding_point=True)],
        target_games=4,
        deciding_point=True,
        tiebreak_games=2,
        tiebreak_points=3
      )
    )
    self.assertNotEqual(tennis.Set(games=None), tennis.Set(games=[]))
    self.assertNotEqual(tennis.Set(target_games=5), tennis.Set(target_games=6))
    self.assertNotEqual(tennis.Set(deciding_point=True), tennis.Set(deciding_point=False))
    self.assertNotEqual(tennis.Set(tiebreak_games=1), tennis.Set(tiebreak_games=2))
    self.assertNotEqual(tennis.Set(tiebreak_points=3), tennis.Set(tiebreak_points=4))

if __name__ == '__main__':
  unittest.main()
