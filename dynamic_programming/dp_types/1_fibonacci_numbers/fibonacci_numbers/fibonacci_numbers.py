'''
Given n, return the nth fibonacci number.
'''


def fibonacci(n: int) -> int:
    if n == 0:
        return 0

    f1, f2 = 0, 1
    for _ in range(n - 1):
        f1, f2 = f2, f1 + f2
    return f2


if __name__ == '__main__':
    tests = [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (8, 21),
    ]

    for n_test, (n, expected) in enumerate(tests):
        result = fibonacci(n)
        if result != expected:
            raise Exception(f'Test #{n_test} failed:'
                            f'result={result}, expected={expected}')

    print('Success!')
