'''
Given an 8x8 chessboard with the knight starting at the bottom-left spot.
After 1000 moves, what is the probability of the knight ending at the upper-right spot?

Knight moves in L format.
Knight possible moves, starting at K0 ending at any K1:
+--+--+--+--+--+--+--+--+
|  |  |  |  |  |  |  |  |
+--+--+--+--+--+--+--+--+
|  |  |K1|  |K1|  |  |  |
+--+--+--+--+--+--+--+--+
|  |K1|  |  |  |K1|  |  |
+--+--+--+--+--+--+--+--+
|  |  |  |K0|  |  |  |  |
+--+--+--+--+--+--+--+--+
|  |K1|  |  |  |K1|  |  |
+--+--+--+--+--+--+--+--+
|  |  |K1|  |K1|  |  |  |
+--+--+--+--+--+--+--+--+
|  |  |  |  |  |  |  |  |
+--+--+--+--+--+--+--+--+
|  |  |  |  |  |  |  |  |
+--+--+--+--+--+--+--+--+
'''

import sys
sys.setrecursionlimit(2000)


def knight_moves(chessboard_size: int, total_moves: int) -> float:
    paths: dict[tuple[int, int, int], tuple[int, int]] = {}
    total_paths, correct_paths = _knight_moves(
        0, 0, 0,
        chessboard_size, total_moves,
        paths,
    )

    return correct_paths / total_paths


def _knight_moves(
    row: int,
    col: int,
    n_moves: int,
    chessboard_size: int,
    total_moves: int,
    paths: dict[tuple[int, int, int], tuple[int, int]],
) -> tuple[int, int]:
    if (row, col, n_moves) in paths:
        total_paths, correct_paths = paths[(row, col, n_moves)]
        return total_paths, correct_paths

    if n_moves == total_moves:
        total_paths = 1
        correct_paths = 1 if (row, col) == (chessboard_size - 1, chessboard_size - 1) else 0
        return total_paths, correct_paths

    total_paths, correct_paths = 0, 0

    for next_row, next_col in _next_spots(chessboard_size, row, col):
        next_total_paths, next_correct_paths = _knight_moves(
            next_row, next_col, n_moves + 1,
            chessboard_size, total_moves,
            paths,
        )

        total_paths += next_total_paths
        correct_paths += next_correct_paths

    paths[(row, col, n_moves)] = (total_paths, correct_paths)

    return total_paths, correct_paths


def _next_spots(chessboard_size: int, row: int, col: int) -> list[tuple[int, int]]:
    directions = [
        (2, 1), (2, 1),
        (1, 2), (1, 2),
        (-1, 2), (-1, 2),
        (-2, 1), (-2, 1),
        (2, -1), (2, -1),
        (1, -2), (1, -2),
        (-1, -2), (-1, -2),
        (-2, -1), (-2, -1),
    ]

    next_spots = []
    for drow, dcol in directions:
        nrow = row + drow
        ncol = col + dcol

        if 0 <= nrow < chessboard_size and 0 <= ncol < chessboard_size:
            next_spots.append((nrow, ncol))

    return next_spots


def run_tests() -> None:
    tests = [
        (3, 4, 0.125),
        (4, 4, 0.166),
        (8, 100, 0.011),
        (8, 1000, 0.011),
    ]

    for i, (chessboard_size, total_moves, expected) in enumerate(tests):
        probability = knight_moves(chessboard_size, total_moves)
        if abs(probability - expected) > 0.01:
            raise Exception(f"Test #{i} failed: got={probability}, want={expected}")

    print('Success!')


if __name__ == '__main__':
    run_tests()
