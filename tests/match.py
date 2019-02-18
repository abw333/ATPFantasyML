import re
import unittest

import tennis

class Match(unittest.TestCase):
  def test_init_no_args(self):
    match = tennis.Match()

    self.assertEqual(
      match.sets,
      [tennis.Set(
        games=[tennis.Game(server_points=0, returner_points=0, deciding_point=False)],
        target_games=6,
        deciding_point=False,
        tiebreak_games=6,
        tiebreak_points=7
      )]
    )
    self.assertEqual(match.target_sets, 2)
    self.assertEqual(match.target_games, 6)
    self.assertFalse(match.deciding_point)
    self.assertEqual(match.tiebreak_games, 6)
    self.assertEqual(match.tiebreak_points, 7)
    self.assertEqual(match.final_set_target_games, 6)
    self.assertFalse(match.final_set_deciding_point)
    self.assertEqual(match.final_set_tiebreak_games, 6)
    self.assertEqual(match.final_set_tiebreak_points, 7)

  def test_init_args(self):
    with self.assertRaisesRegex(
      TypeError,
      '^{}$'.format(re.escape('__init__() takes 1 positional argument but 2 were given'))
    ):
      tennis.Match([])

  def test_init_kwargs(self):
    match = tennis.Match(
      final_set_tiebreak_points=1,
      final_set_tiebreak_games=2,
      final_set_deciding_point=True,
      final_set_target_games=3,
      tiebreak_points=4,
      tiebreak_games=5,
      deciding_point=True,
      target_games=6,
      target_sets=7,
      sets=[tennis.Set()]
    )

    self.assertEqual(match.sets, [tennis.Set()])
    self.assertEqual(match.target_sets, 7)
    self.assertEqual(match.target_games, 6)
    self.assertTrue(match.deciding_point)
    self.assertEqual(match.tiebreak_games, 5)
    self.assertEqual(match.tiebreak_points, 4)
    self.assertEqual(match.final_set_target_games, 3)
    self.assertTrue(match.final_set_deciding_point)
    self.assertEqual(match.final_set_tiebreak_games, 2)
    self.assertEqual(match.final_set_tiebreak_points, 1)

  def test_init_inconsistent_tiebreak_args(self):
    with self.assertRaisesRegex(
      RuntimeError,
      '^{}$'.format(re.escape('tiebreak_games and tiebreak_points must both be None or non-None.'))
    ):
      tennis.Match(tiebreak_games=1, tiebreak_points=None)

    with self.assertRaisesRegex(
      RuntimeError,
      '^{}$'.format(re.escape('tiebreak_games and tiebreak_points must both be None or non-None.'))
    ):
      tennis.Match(tiebreak_games=None, tiebreak_points=1)

  def test_init_inconsistent_final_set_tiebreak_args(self):
    with self.assertRaisesRegex(
      RuntimeError,
      '^{}$'.format(re.escape(
        'final_set_tiebreak_games and final_set_tiebreak_points must both be None or non-None.'
      ))
    ):
      tennis.Match(final_set_tiebreak_games=1, final_set_tiebreak_points=None)

    with self.assertRaisesRegex(
      RuntimeError,
      '^{}$'.format(re.escape(
        'final_set_tiebreak_games and final_set_tiebreak_points must both be None or non-None.'
      ))
    ):
      tennis.Match(final_set_tiebreak_games=None, final_set_tiebreak_points=1)

  def test_init_negative_points(self):
    with self.assertRaisesRegex(
      RuntimeError,
      '^{}$'.format(re.escape('Point scores must be non-negative.'))
    ):
      tennis.Match(target_games=-1)

    with self.assertRaisesRegex(
      RuntimeError,
      '^{}$'.format(re.escape('Point scores must be non-negative.'))
    ):
      tennis.Match(tiebreak_games=-1, tiebreak_points=1)

    with self.assertRaisesRegex(
      RuntimeError,
      '^{}$'.format(re.escape('Point scores must be non-negative.'))
    ):
      tennis.Match(tiebreak_games=1, tiebreak_points=-1)

  def test_init_final_set_negative_points(self):
    with self.assertRaisesRegex(
      RuntimeError,
      '^{}$'.format(re.escape('Point scores must be non-negative.'))
    ):
      tennis.Match(final_set_target_games=-1)

    with self.assertRaisesRegex(
      RuntimeError,
      '^{}$'.format(re.escape('Point scores must be non-negative.'))
    ):
      tennis.Match(final_set_tiebreak_games=-1, final_set_tiebreak_points=1)

    with self.assertRaisesRegex(
      RuntimeError,
      '^{}$'.format(re.escape('Point scores must be non-negative.'))
    ):
      tennis.Match(final_set_tiebreak_games=1, final_set_tiebreak_points=-1)

  def test_init_zero_target_sets(self):
    with self.assertRaisesRegex(
      RuntimeError,
      '^{}$'.format(re.escape('target_sets must be at least 1.'))
    ):
      tennis.Match(target_sets=0)

  def test_init_first_set(self):
    match = tennis.Match(
      sets=None,
      target_sets=7,
      target_games=6,
      deciding_point=True,
      tiebreak_games=5,
      tiebreak_points=4,
      final_set_target_games=3,
      final_set_deciding_point=False,
      final_set_tiebreak_games=2,
      final_set_tiebreak_points=1
    )

    self.assertEqual(
      match.sets,
      [tennis.Set(
        games=[tennis.Game(server_points=0, returner_points=0, deciding_point=True)],
        target_games=6,
        deciding_point=True,
        tiebreak_games=5,
        tiebreak_points=4
      )]
    )
    self.assertEqual(match.target_sets, 7)
    self.assertEqual(match.target_games, 6)
    self.assertTrue(match.deciding_point)
    self.assertEqual(match.tiebreak_games, 5)
    self.assertEqual(match.tiebreak_points, 4)
    self.assertEqual(match.final_set_target_games, 3)
    self.assertFalse(match.final_set_deciding_point)
    self.assertEqual(match.final_set_tiebreak_games, 2)
    self.assertEqual(match.final_set_tiebreak_points, 1)

  def test_init_final_set(self):
    match = tennis.Match(
      sets=None,
      target_sets=1,
      target_games=2,
      deciding_point=False,
      tiebreak_games=3,
      tiebreak_points=4,
      final_set_target_games=5,
      final_set_deciding_point=True,
      final_set_tiebreak_games=6,
      final_set_tiebreak_points=7
    )

    self.assertEqual(
      match.sets,
      [tennis.Set(
        games=[tennis.Game(server_points=0, returner_points=0, deciding_point=True)],
        target_games=5,
        deciding_point=True,
        tiebreak_games=6,
        tiebreak_points=7
      )]
    )
    self.assertEqual(match.target_sets, 1)
    self.assertEqual(match.target_games, 2)
    self.assertFalse(match.deciding_point)
    self.assertEqual(match.tiebreak_games, 3)
    self.assertEqual(match.tiebreak_points, 4)
    self.assertEqual(match.final_set_target_games, 5)
    self.assertTrue(match.final_set_deciding_point)
    self.assertEqual(match.final_set_tiebreak_games, 6)
    self.assertEqual(match.final_set_tiebreak_points, 7)

  def test_first_server_served_first(self):
    match = tennis.Match(sets=[
      tennis.Set(games=[tennis.Game()]),
      tennis.Set(games=[tennis.Game()] * 2),
      tennis.Set(games=[tennis.Game()] * 3),
      tennis.Set(games=[tennis.Game()] * 4)
    ])

    self.assertEqual(list(match.first_server_served_first), [True, False, False, True])

  def test_sets(self):
    sets = []
    match = tennis.Match(sets=sets)

    self.assertEqual(match.first_server_sets(), 0)
    self.assertEqual(match.first_returner_sets(), 0)

    sets.append(tennis.Set(
      games=[tennis.Game(server_points=4), tennis.Game(returner_points=4)],
      target_games=2
    ))
    match = tennis.Match(sets=sets)

    self.assertEqual(match.first_server_sets(), 1)
    self.assertEqual(match.first_returner_sets(), 0)

    sets.append(tennis.Set(
      games=[tennis.Tiebreak(first_returner_points=7)],
      tiebreak_games=0
    ))
    match = tennis.Match(sets=sets)

    self.assertEqual(match.first_server_sets(), 1)
    self.assertEqual(match.first_returner_sets(), 1)

    sets.append(tennis.Set(
      games=[tennis.Game(server_points=4), tennis.Game(returner_points=4)],
      target_games=2
    ))
    match = tennis.Match(sets=sets)

    self.assertEqual(match.first_server_sets(), 1)
    self.assertEqual(match.first_returner_sets(), 2)

    sets.append(tennis.Set(
      games=[tennis.Tiebreak(first_returner_points=7)],
      tiebreak_games=0
    ))
    match = tennis.Match(sets=sets)

    self.assertEqual(match.first_server_sets(), 2)
    self.assertEqual(match.first_returner_sets(), 2)

    sets.append(tennis.Set())
    match = tennis.Match(sets=sets)

    self.assertEqual(match.first_server_sets(), 2)
    self.assertEqual(match.first_returner_sets(), 2)

    sets.append(tennis.Set())
    match = tennis.Match(sets=sets)

    self.assertEqual(match.first_server_sets(), 2)
    self.assertEqual(match.first_returner_sets(), 2)

  def test_winner(self):
    self.assertIsNone(tennis.Match(sets=[]).winner)
    self.assertIsNone(tennis.Match(sets=[
      tennis.Set(games=[tennis.Tiebreak(first_server_points=7)], tiebreak_games=0)
    ]).winner)
    self.assertIsNone(tennis.Match(sets=[
      tennis.Set(games=[tennis.Tiebreak(first_server_points=7)], tiebreak_games=0),
      tennis.Set(games=[tennis.Tiebreak(first_server_points=7)], tiebreak_games=0)
    ]).winner)
    self.assertTrue(tennis.Match(sets=[
      tennis.Set(games=[tennis.Tiebreak(first_server_points=7)], tiebreak_games=0),
      tennis.Set(games=[tennis.Tiebreak(first_server_points=7)], tiebreak_games=0),
      tennis.Set(games=[tennis.Tiebreak(first_server_points=7)], tiebreak_games=0)
    ]).winner)
    self.assertFalse(tennis.Match(sets=[
      tennis.Set(games=[tennis.Tiebreak(first_server_points=7)], tiebreak_games=0),
      tennis.Set(games=[tennis.Tiebreak(first_server_points=7)], tiebreak_games=0),
      tennis.Set(games=[tennis.Tiebreak(first_returner_points=7)], tiebreak_games=0)
    ]).winner)
    self.assertTrue(tennis.Match(
      sets=[tennis.Set(games=[tennis.Tiebreak(first_server_points=7)], tiebreak_games=0)],
      target_sets=1
    ).winner)
    self.assertFalse(tennis.Match(
      sets=[tennis.Set(games=[tennis.Tiebreak(first_returner_points=7)], tiebreak_games=0)],
      target_sets=1
    ).winner)

  def test_first_server_to_serve(self):
    with self.assertRaisesRegex(
      RuntimeError,
      '^{}$'.format(re.escape('No server is to serve the next point because the match is over.'))
    ):
      tennis.Match(
        sets=[tennis.Set(games=[tennis.Tiebreak(first_server_points=7)], tiebreak_games=0)],
        target_sets=1,
        tiebreak_games=0
      ).first_server_to_serve()

    self.assertTrue(
      tennis.Match(
        sets=[tennis.Set(games=[tennis.Tiebreak(first_server_points=0)], tiebreak_games=0)],
        tiebreak_games=0
      ).first_server_to_serve()
    )
    self.assertFalse(
      tennis.Match(
        sets=[tennis.Set(games=[tennis.Tiebreak(first_server_points=1)], tiebreak_games=0)],
        tiebreak_games=0
      ).first_server_to_serve()
    )
    self.assertFalse(
      tennis.Match(
        sets=[
          tennis.Set(games=[tennis.Tiebreak(first_server_points=7)], tiebreak_games=0),
          tennis.Set(games=[tennis.Tiebreak(first_server_points=0)], tiebreak_games=0)
        ],
        tiebreak_games=0
      ).first_server_to_serve()
    )
    self.assertTrue(
      tennis.Match(
        sets=[
          tennis.Set(games=[tennis.Tiebreak(first_server_points=7)], tiebreak_games=0),
          tennis.Set(games=[tennis.Tiebreak(first_server_points=1)], tiebreak_games=0)
        ],
        tiebreak_games=0
      ).first_server_to_serve()
    )

  def test_point(self):
    with self.assertRaisesRegex(
      RuntimeError,
      '^{}$'.format(re.escape('Cannot advance this match\'s score because the match is over.'))
    ):
      tennis.Match(
        sets=[tennis.Set(games=[tennis.Tiebreak(first_server_points=7)], tiebreak_games=0)],
        target_sets=1,
        tiebreak_games=0
      ).point(first_server=True)

    match = tennis.Match(tiebreak_games=0, tiebreak_points=2)
    self.assertIsNone(match.point(first_server=True))
    self.assertEqual(
      match,
      tennis.Match(
        sets=[tennis.Set(
          games=[tennis.Tiebreak(first_server_points=1, target_points=2)],
          tiebreak_games=0,
          tiebreak_points=2
        )],
        tiebreak_games=0,
        tiebreak_points=2
      )
    )
    self.assertIsNone(match.point(first_server=True))
    self.assertEqual(
      match,
      tennis.Match(
        sets=[
          tennis.Set(
            games=[tennis.Tiebreak(first_server_points=2, target_points=2)],
            tiebreak_games=0,
            tiebreak_points=2
          ),
          tennis.Set(
            games=[tennis.Tiebreak(target_points=2)],
            tiebreak_games=0,
            tiebreak_points=2
          )
        ],
        tiebreak_games=0,
        tiebreak_points=2
      )
    )
    self.assertIsNone(match.point(first_server=True))
    self.assertEqual(
      match,
      tennis.Match(
        sets=[
          tennis.Set(
            games=[tennis.Tiebreak(first_server_points=2, target_points=2)],
            tiebreak_games=0,
            tiebreak_points=2
          ),
          tennis.Set(
            games=[tennis.Tiebreak(first_returner_points=1, target_points=2)],
            tiebreak_games=0,
            tiebreak_points=2
          )
        ],
        tiebreak_games=0,
        tiebreak_points=2
      )
    )
    self.assertTrue(match.point(first_server=True))
    self.assertEqual(
      match,
      tennis.Match(
        sets=[
          tennis.Set(
            games=[tennis.Tiebreak(first_server_points=2, target_points=2)],
            tiebreak_games=0,
            tiebreak_points=2
          ),
          tennis.Set(
            games=[tennis.Tiebreak(first_returner_points=2, target_points=2)],
            tiebreak_games=0,
            tiebreak_points=2
          )
        ],
        tiebreak_games=0,
        tiebreak_points=2
      )
    )
    match = tennis.Match(
      sets=[tennis.Set(
        games=[tennis.Tiebreak(first_server_points=1, target_points=2)],
        tiebreak_games=0,
        tiebreak_points=2
      )],
      target_sets=1,
      tiebreak_games=0,
      tiebreak_points=2
    )
    self.assertTrue(match.point(first_server=True))
    self.assertEqual(
      match,
      tennis.Match(
        sets=[tennis.Set(
          games=[tennis.Tiebreak(first_server_points=2, target_points=2)],
          tiebreak_games=0,
          tiebreak_points=2
        )],
        target_sets=1,
        tiebreak_games=0,
        tiebreak_points=2
      )
    )
    match = tennis.Match(
      sets=[
        tennis.Set(
          games=[tennis.Tiebreak(first_returner_points=2, target_points=2)],
          tiebreak_games=0,
          tiebreak_points=2
        ),
        tennis.Set(
          games=[tennis.Tiebreak(first_returner_points=1, target_points=2)],
          tiebreak_games=0,
          tiebreak_points=2
        )
      ],
      tiebreak_games=0,
      tiebreak_points=2,
      final_set_target_games=3,
      final_set_deciding_point=True,
      final_set_tiebreak_games=4,
      final_set_tiebreak_points=5
    )
    self.assertIsNone(match.point(first_server=True))
    self.assertEqual(
      match,
      tennis.Match(
        sets=[
          tennis.Set(
            games=[tennis.Tiebreak(first_returner_points=2, target_points=2)],
            tiebreak_games=0,
            tiebreak_points=2
          ),
          tennis.Set(
            games=[tennis.Tiebreak(first_returner_points=2, target_points=2)],
            tiebreak_games=0,
            tiebreak_points=2
          ),
          tennis.Set(
            games=[tennis.Game(deciding_point=True)],
            target_games=3,
            deciding_point=True,
            tiebreak_games=4,
            tiebreak_points=5
          )
        ],
        tiebreak_games=0,
        tiebreak_points=2,
        final_set_target_games=3,
        final_set_deciding_point=True,
        final_set_tiebreak_games=4,
        final_set_tiebreak_points=5
      )
    )
    match = tennis.Match(tiebreak_games=0, tiebreak_points=2)
    self.assertIsNone(match.point(first_server=False))
    self.assertEqual(
      match,
      tennis.Match(
        sets=[tennis.Set(
          games=[tennis.Tiebreak(first_returner_points=1, target_points=2)],
          tiebreak_games=0,
          tiebreak_points=2
        )],
        tiebreak_games=0,
        tiebreak_points=2
      )
    )
    self.assertIsNone(match.point(first_server=False))
    self.assertEqual(
      match,
      tennis.Match(
        sets=[
          tennis.Set(
            games=[tennis.Tiebreak(first_returner_points=2, target_points=2)],
            tiebreak_games=0,
            tiebreak_points=2
          ),
          tennis.Set(
            games=[tennis.Tiebreak(target_points=2)],
            tiebreak_games=0,
            tiebreak_points=2
          )
        ],
        tiebreak_games=0,
        tiebreak_points=2
      )
    )
    self.assertIsNone(match.point(first_server=False))
    self.assertEqual(
      match,
      tennis.Match(
        sets=[
          tennis.Set(
            games=[tennis.Tiebreak(first_returner_points=2, target_points=2)],
            tiebreak_games=0,
            tiebreak_points=2
          ),
          tennis.Set(
            games=[tennis.Tiebreak(first_server_points=1, target_points=2)],
            tiebreak_games=0,
            tiebreak_points=2
          )
        ],
        tiebreak_games=0,
        tiebreak_points=2
      )
    )
    self.assertFalse(match.point(first_server=False))
    self.assertEqual(
      match,
      tennis.Match(
        sets=[
          tennis.Set(
            games=[tennis.Tiebreak(first_returner_points=2, target_points=2)],
            tiebreak_games=0,
            tiebreak_points=2
          ),
          tennis.Set(
            games=[tennis.Tiebreak(first_server_points=2, target_points=2)],
            tiebreak_games=0,
            tiebreak_points=2
          )
        ],
        tiebreak_games=0,
        tiebreak_points=2
      )
    )
    match = tennis.Match(
      sets=[tennis.Set(
        games=[tennis.Tiebreak(first_returner_points=1, target_points=2)],
        tiebreak_games=0,
        tiebreak_points=2
      )],
      target_sets=1,
      tiebreak_games=0,
      tiebreak_points=2
    )
    self.assertFalse(match.point(first_server=False))
    self.assertEqual(
      match,
      tennis.Match(
        sets=[tennis.Set(
          games=[tennis.Tiebreak(first_returner_points=2, target_points=2)],
          tiebreak_games=0,
          tiebreak_points=2
        )],
        target_sets=1,
        tiebreak_games=0,
        tiebreak_points=2
      )
    )
    match = tennis.Match(
      sets=[
        tennis.Set(
          games=[tennis.Tiebreak(first_server_points=2, target_points=2)],
          tiebreak_games=0,
          tiebreak_points=2
        ),
        tennis.Set(
          games=[tennis.Tiebreak(first_server_points=1, target_points=2)],
          tiebreak_games=0,
          tiebreak_points=2
        )
      ],
      tiebreak_games=0,
      tiebreak_points=2,
      final_set_target_games=3,
      final_set_deciding_point=True,
      final_set_tiebreak_games=4,
      final_set_tiebreak_points=5
    )
    self.assertIsNone(match.point(first_server=False))
    self.assertEqual(
      match,
      tennis.Match(
        sets=[
          tennis.Set(
            games=[tennis.Tiebreak(first_server_points=2, target_points=2)],
            tiebreak_games=0,
            tiebreak_points=2
          ),
          tennis.Set(
            games=[tennis.Tiebreak(first_server_points=2, target_points=2)],
            tiebreak_games=0,
            tiebreak_points=2
          ),
          tennis.Set(
            games=[tennis.Game(deciding_point=True)],
            target_games=3,
            deciding_point=True,
            tiebreak_games=4,
            tiebreak_points=5
          )
        ],
        tiebreak_games=0,
        tiebreak_points=2,
        final_set_target_games=3,
        final_set_deciding_point=True,
        final_set_tiebreak_games=4,
        final_set_tiebreak_points=5
      )
    )

  def test_str(self):
    self.assertEqual(
      str(tennis.Match(
        sets=[tennis.Set(
          games=[tennis.Game(server_points=1, returner_points=2, deciding_point=True)],
          target_games=3,
          deciding_point=True,
          tiebreak_games=4,
          tiebreak_points=5
        )],
        target_sets=6,
        target_games=3,
        deciding_point=True,
        tiebreak_games=4,
        tiebreak_points=5,
        final_set_target_games=7,
        final_set_deciding_point=False,
        final_set_tiebreak_games=8,
        final_set_tiebreak_points=9
      )),
      'Match('
        'sets=[Set('
          'games=[Game(server_points=1, returner_points=2, deciding_point=True)], '
          'target_games=3, '
          'deciding_point=True, '
          'tiebreak_games=4, '
          'tiebreak_points=5'
        ')], '
        'target_sets=6, '
        'target_games=3, '
        'deciding_point=True, '
        'tiebreak_games=4, '
        'tiebreak_points=5, '
        'final_set_target_games=7, '
        'final_set_deciding_point=False, '
        'final_set_tiebreak_games=8, '
        'final_set_tiebreak_points=9'
      ')'
    )

  def test_repr(self):
    self.assertEqual(
      repr(tennis.Match(
        sets=[tennis.Set(
          games=[tennis.Game(server_points=1, returner_points=2, deciding_point=True)],
          target_games=3,
          deciding_point=True,
          tiebreak_games=4,
          tiebreak_points=5
        )],
        target_sets=6,
        target_games=3,
        deciding_point=True,
        tiebreak_games=4,
        tiebreak_points=5,
        final_set_target_games=7,
        final_set_deciding_point=False,
        final_set_tiebreak_games=8,
        final_set_tiebreak_points=9
      )),
      'Match('
        'sets=[Set('
          'games=[Game(server_points=1, returner_points=2, deciding_point=True)], '
          'target_games=3, '
          'deciding_point=True, '
          'tiebreak_games=4, '
          'tiebreak_points=5'
        ')], '
        'target_sets=6, '
        'target_games=3, '
        'deciding_point=True, '
        'tiebreak_games=4, '
        'tiebreak_points=5, '
        'final_set_target_games=7, '
        'final_set_deciding_point=False, '
        'final_set_tiebreak_games=8, '
        'final_set_tiebreak_points=9'
      ')'
    )

  def test_eq(self):
    self.assertEqual(
      tennis.Match(
        sets=[tennis.Set(
          games=[tennis.Game(server_points=1, returner_points=2, deciding_point=True)],
          target_games=3,
          deciding_point=True,
          tiebreak_games=4,
          tiebreak_points=5
        )],
        target_sets=6,
        target_games=3,
        deciding_point=True,
        tiebreak_games=4,
        tiebreak_points=5,
        final_set_target_games=6,
        final_set_deciding_point=False,
        final_set_tiebreak_games=7,
        final_set_tiebreak_points=8
      ),
      tennis.Match(
        sets=[tennis.Set(
          games=[tennis.Game(server_points=1, returner_points=2, deciding_point=True)],
          target_games=3,
          deciding_point=True,
          tiebreak_games=4,
          tiebreak_points=5
        )],
        target_sets=6,
        target_games=3,
        deciding_point=True,
        tiebreak_games=4,
        tiebreak_points=5,
        final_set_target_games=6,
        final_set_deciding_point=False,
        final_set_tiebreak_games=7,
        final_set_tiebreak_points=8
      )
    )
    self.assertNotEqual(tennis.Match(sets=None), tennis.Match(sets=[]))
    self.assertNotEqual(tennis.Match(target_sets=1), tennis.Match(target_sets=2))
    self.assertNotEqual(tennis.Match(target_games=3), tennis.Match(target_games=4))
    self.assertNotEqual(tennis.Match(deciding_point=True), tennis.Match(deciding_point=False))
    self.assertNotEqual(tennis.Match(tiebreak_games=5), tennis.Match(tiebreak_games=6))
    self.assertNotEqual(tennis.Match(tiebreak_points=7), tennis.Match(tiebreak_points=8))
    self.assertNotEqual(
      tennis.Match(final_set_target_games=9),
      tennis.Match(final_set_target_games=10)
    )
    self.assertNotEqual(
      tennis.Match(final_set_deciding_point=True),
      tennis.Match(final_set_deciding_point=False)
    )
    self.assertNotEqual(
      tennis.Match(final_set_tiebreak_games=11),
      tennis.Match(final_set_tiebreak_games=12)
    )
    self.assertNotEqual(
      tennis.Match(final_set_tiebreak_points=13),
      tennis.Match(final_set_tiebreak_points=14)
    )

if __name__ == '__main__':
  unittest.main()
