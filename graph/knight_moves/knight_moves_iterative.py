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


def _chessboard(n):
    return [[0] * chessboard_size for _ in range(chessboard_size)]


def _knight_moves(chessboard):
    n = len(chessboard)
    next_chessboard = _chessboard(n)

    for row in range(len(chessboard)):
        for col in range(len(chessboard[row])):
            for nrow, ncol in _next(n, row, col):
                next_chessboard[nrow][ncol] += chessboard[row][col]

    return next_chessboard


"""
Idea:
- For each position and iteration, count the number of times the knight is in it. 
- Loop through the positions; for each next position (that is, a position that can reach the current position after a move), sum the number of times the knight landed there in the previous iteration. 
- That is, the number of times that the knight is present in the position (row, col) at iteration i is the sum of times, from the previous iteration, that the knight is present in the positions that can reach p after a move. 

Time Complexity: O(N * M)
- N: number of iterations
- M: total number of chessboard positions
"""


def knight_moves(chessboard_size: int, total_moves: int) -> float:
    chessboard = _chessboard(chessboard_size)
    chessboard[-1][0] = 1

    for _ in range(total_moves):
        chessboard = _knight_moves(chessboard)

    total = sum(sum(row) for row in chessboard)

    return chessboard[0][-1] / total


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
