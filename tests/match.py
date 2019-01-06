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

  def test_init_args(self):
    with self.assertRaises(
      TypeError,
      msg='__init__() takes 1 positional argument but 2 were given'
    ):
      tennis.Match([])

  def test_init_kwargs(self):
    match = tennis.Match(
      tiebreak_points=1,
      tiebreak_games=2,
      deciding_point=True,
      target_games=3,
      target_sets=4,
      sets=[tennis.Set()]
    )

    self.assertEqual(match.sets, [tennis.Set()])
    self.assertEqual(match.target_sets, 4)
    self.assertEqual(match.target_games, 3)
    self.assertTrue(match.deciding_point)
    self.assertEqual(match.tiebreak_games, 2)
    self.assertEqual(match.tiebreak_points, 1)

  def test_init_inconsistent_tiebreak_args(self):
    with self.assertRaises(
      RuntimeError,
      msg='tiebreak_games and tiebreak_points must both be None or non-None.'
    ):
      tennis.Match(tiebreak_games=1, tiebreak_points=None)

    with self.assertRaises(
      RuntimeError,
      msg='tiebreak_games and tiebreak_points must both be None or non-None.'
    ):
      tennis.Match(tiebreak_games=None, tiebreak_points=1)

  def test_init_negative_points(self):
    with self.assertRaises(RuntimeError, msg='Point scores must be non-negative.'):
      tennis.Match(target_sets=-1)

    with self.assertRaises(RuntimeError, msg='Point scores must be non-negative.'):
      tennis.Match(target_games=-1)

    with self.assertRaises(RuntimeError, msg='Point scores must be non-negative.'):
      tennis.Match(tiebreak_games=-1, tiebreak_points=1)

    with self.assertRaises(RuntimeError, msg='Point scores must be non-negative.'):
      tennis.Match(tiebreak_games=1, tiebreak_points=-1)

  def test_init_first_set(self):
    match = tennis.Match(
      sets=None,
      target_sets=4,
      target_games=3,
      deciding_point=True,
      tiebreak_games=2,
      tiebreak_points=1
    )

    self.assertEqual(
      match.sets,
      [tennis.Set(
        games=[tennis.Game(server_points=0, returner_points=0, deciding_point=True)],
        target_games=3,
        deciding_point=True,
        tiebreak_games=2,
        tiebreak_points=1
      )]
    )
    self.assertEqual(match.target_sets, 4)
    self.assertEqual(match.target_games, 3)
    self.assertTrue(match.deciding_point)
    self.assertEqual(match.tiebreak_games, 2)
    self.assertEqual(match.tiebreak_points, 1)

  def test_first_server_served_first(self):
    match = tennis.Match(sets=[
      tennis.Set(games=[]),
      tennis.Set(games=[tennis.Game()]),
      tennis.Set(games=[tennis.Game()] * 2),
      tennis.Set(games=[tennis.Game()] * 3),
      tennis.Set(games=[tennis.Game()] * 4)
    ])

    self.assertEqual(list(match.first_server_served_first()), [True, True, False, False, True])

  def test_sets(self):
    match = tennis.Match(sets=[])

    self.assertEqual(match.first_server_sets(), 0)
    self.assertEqual(match.first_returner_sets(), 0)

    match.sets.append(tennis.Set(
      games=[tennis.Game(server_points=4), tennis.Game(returner_points=4)],
      target_games=2
    ))

    self.assertEqual(match.first_server_sets(), 1)
    self.assertEqual(match.first_returner_sets(), 0)

    match.sets.append(tennis.Set(
      games=[tennis.Tiebreak(first_returner_points=7)],
      tiebreak_games=0
    ))

    self.assertEqual(match.first_server_sets(), 1)
    self.assertEqual(match.first_returner_sets(), 1)

    match.sets.append(tennis.Set(
      games=[tennis.Game(server_points=4), tennis.Game(returner_points=4)],
      target_games=2
    ))

    self.assertEqual(match.first_server_sets(), 1)
    self.assertEqual(match.first_returner_sets(), 2)

    match.sets.append(tennis.Set(
      games=[tennis.Tiebreak(first_returner_points=7)],
      tiebreak_games=0
    ))

    self.assertEqual(match.first_server_sets(), 2)
    self.assertEqual(match.first_returner_sets(), 2)

    match.sets.append(tennis.Set())

    self.assertEqual(match.first_server_sets(), 2)
    self.assertEqual(match.first_returner_sets(), 2)

    match.sets.append(tennis.Set())

    self.assertEqual(match.first_server_sets(), 2)
    self.assertEqual(match.first_returner_sets(), 2)

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
        tiebreak_points=5
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
        'tiebreak_points=5'
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
        tiebreak_points=5
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
        'tiebreak_points=5'
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
        tiebreak_points=5
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
        tiebreak_points=5
      )
    )
    self.assertNotEqual(tennis.Match(sets=None), tennis.Match(sets=[]))
    self.assertNotEqual(tennis.Match(target_sets=1), tennis.Match(target_sets=2))
    self.assertNotEqual(tennis.Match(target_games=3), tennis.Match(target_games=4))
    self.assertNotEqual(tennis.Match(deciding_point=True), tennis.Match(deciding_point=False))
    self.assertNotEqual(tennis.Match(tiebreak_games=5), tennis.Match(tiebreak_games=6))
    self.assertNotEqual(tennis.Match(tiebreak_points=7), tennis.Match(tiebreak_points=8))

if __name__ == '__main__':
  unittest.main()
