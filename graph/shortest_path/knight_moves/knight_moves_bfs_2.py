"""
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
"""

from collections import deque


def _next(n: int, row: int, col: int) -> list[(int, int)]:
    return [
        (row + drow, col + dcol)
        for drow, dcol in [
            (2, 1),
            (1, 2),
            (-1, 2),
            (-2, 1),
            (-2, -1),
            (-1, -2),
            (1, -2),
            (2, -1),
        ]
        if 0 <= row + drow < n and 0 <= col + dcol < n
    ]


"""
Idea:
1. The next possible knight positions are the next nodes in the tree.
2. We traverse it with BFS, with every level being the number of moves made.
3. Positions that are repeated for that level are not added again in the queue, instead its count
    is incremented.
4. Count is the number of times it ends up in (row, col) after n_moves from (0, 0).
5. The next position has its count summed with the current count, because the number of times it
    ends up in (next_row, next_col) after n_moves+1 is the same number of times it ends up in
    (row, col) after n_moves.
"""


def knight_moves(chessboard_size: int, total_moves: int) -> float:
    queue = deque([(0, 0, 0)])
    curr_moves = 0
    prev_count = {(0, 0): 1}
    curr_count = {}

    total_count = 0
    target_count = 0

    while queue:
        row, col, n_moves = queue.popleft()
        if n_moves > curr_moves:
            curr_moves = n_moves
            prev_count = curr_count
            curr_count = {}

        if n_moves == total_moves:
            total_count += prev_count.get((row, col), 0)

            if row == chessboard_size - 1 and col == chessboard_size - 1:
                target_count += prev_count.get((row, col), 0)

            continue

        for nrow, ncol in _next(chessboard_size, row, col):
            if (nrow, ncol) in curr_count:
                curr_count[(nrow, ncol)] += prev_count[(row, col)]
            else:
                curr_count[(nrow, ncol)] = prev_count[(row, col)]
                queue.append((nrow, ncol, n_moves + 1))

    return target_count / total_count


if __name__ == "__main__":
    tests = [
        (4, 2, 0.250000),
        (3, 4, 0.125000),
        (4, 4, 0.166666),
        (8, 100, 0.01096),
        (8, 1000, 0.01096),
        (8, 1000, 0.01096),
    ]

    for n_test, (chessboard_size, total_moves, expected_prob) in enumerate(tests):
        actual_prob = knight_moves(chessboard_size, total_moves)
        if abs(actual_prob - expected_prob) > 0.000001:
            raise Exception(
                f"Test #{n_test} failed: expected probability {expected_prob}, got {actual_prob}"
            )

    print("Success!")
