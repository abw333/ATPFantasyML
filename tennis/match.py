import tennis

class Match:
  '''
  Python class for objects that represent tennis matches.

  :param list sets: list of sets played in the match
  :param int target_sets: number of sets required to win the match
  :param int target_games: number of games required to win each set
  :param bool deciding_point: whether to play a deciding point at deuce
  :param int tiebreak_games: number of games each player must have before a tiebreak is played, or
                             None if a tiebreak is not to be played
  :param int tiebreak_points: number of points required to win a tiebreak, or None if a tiebreak is
                              not to be played
  :var sets: list of sets played in the match
  :var target_sets: number of sets required to win the match
  :var target_games: number of games required to win each set
  :var deciding_point: whether to play a deciding point at deuce
  :var tiebreak_games: number of games each player must have before a tiebreak is played, or None if
                       a tiebreak is not to be played
  :var tiebreak_points: number of points required to win a tiebreak, or None if a tiebreak is not to
                        be played
  '''
  def __init__(
    self,
    *,
    sets=None,
    target_sets=2,
    target_games=6,
    deciding_point=False,
    tiebreak_games=6,
    tiebreak_points=7
  ):
    # TODO(abw333): validate sets

    if min(target_sets, target_games) < 0:
      raise RuntimeError('Point scores must be non-negative.')

    if (tiebreak_games is None) != (tiebreak_points is None):
      raise RuntimeError('tiebreak_games and tiebreak_points must both be None or non-None.')

    if tiebreak_games is not None and min(tiebreak_games, tiebreak_points) < 0:
      raise RuntimeError('Point scores must be non-negative.')

    self.sets = [tennis.Set(
      games=None,
      target_games=target_games,
      deciding_point=deciding_point,
      tiebreak_games=tiebreak_games,
      tiebreak_points=tiebreak_points
    )] if sets is None else sets

    self.target_sets = target_sets
    self.target_games = target_games
    self.deciding_point = deciding_point
    self.tiebreak_games = tiebreak_games
    self.tiebreak_points = tiebreak_points

  '''
  :param object other: object to compare to the match
  :return: True if the input object is equal to the match, and False otherwise
  '''
  def __eq__(self, other):
    return isinstance(other, type(self)) and self.__dict__ == other.__dict__
