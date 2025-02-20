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


def _move(chessboard_size, row, col):
    return [
        (next_row, next_col)
        for next_row, next_col in [
            (row - 2, col + 1),
            (row - 1, col + 2),
            (row + 1, col + 2),
            (row + 2, col + 1),
            (row + 2, col - 1),
            (row + 1, col - 2),
            (row - 1, col - 2),
            (row - 2, col - 1),
        ]
        if (0 <= next_row < chessboard_size and 0 <= next_col < chessboard_size)
    ]


def knight_moves(chessboard_size, total_moves):
    chessboard = [[0] * chessboard_size for _ in range(chessboard_size)]
    chessboard[-1][0] = 1

    for _ in range(total_moves):
        next_chessboard = [[0] * chessboard_size for _ in range(chessboard_size)]

        for row in range(chessboard_size):
            for col in range(chessboard_size):
                for next_row, next_col in _move(chessboard_size, row, col):
                    next_chessboard[next_row][next_col] += 2 * chessboard[row][col]

        chessboard = next_chessboard

    return chessboard[0][-1] / sum(sum(row) for row in chessboard)


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
