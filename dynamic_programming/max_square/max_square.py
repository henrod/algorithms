'''
Given an m x n binary matrix filled with 0's and 1's,
find the largest square containing only 1's and return its area.

https://leetcode.com/problems/maximal-square/
'''


def max_area(matrix: list[list[int]]) -> int:
    max_len = max(
        *matrix[0],
        *[matrix[row][0] for row in range(len(matrix))]
    )

    for row in range(1, len(matrix)):
        for col in range(1, len(matrix[row])):
            if matrix[row][col] == 0:
                continue

            matrix[row][col] = min(
                matrix[row - 1][col],
                matrix[row][col - 1],
                matrix[row - 1][col - 1],
            ) + 1

            max_len = max(max_len, matrix[row][col])

    return max_len * max_len


def run_tests():
    tests = [
        ([
            [1, 0, 1, 0, 0],
            [1, 0, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 0, 0, 1, 0],
        ], 4),
        ([
            [1, 0],
            [1, 0],
        ], 1),
        ([
            [1, 0, 1, 0, 0],
            [1, 0, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 0, 1, 1, 1],
        ], 9),
    ]

    for n_test, (matrix, expected) in enumerate(tests):
        result = max_area(matrix)
        if result != expected:
            raise Exception(f'Test #{n_test} failed:'
                            f'result={result}, expected={expected}')

    print('Success!')


if __name__ == '__main__':
    run_tests()
