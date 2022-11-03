'''
Pedrinho can climb either one or two steps of a stair.
Return the total number of possibilities that he can
reach the nth step of the stair.
'''


def climb_stairs(n: int) -> int:
    prev, curr = 0, 1
    for _ in range(n):
        prev, curr = curr, prev + curr
    return curr


if __name__ == '__main__':
    tests = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 8),
    ]

    for n_test, (n, expected) in enumerate(tests):
        result = climb_stairs(n)
        if result != expected:
            raise Exception(f'Test #{n_test} failed:'
                            f'result={result}, expected={expected}')

    print('Success!')
