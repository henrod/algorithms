import sys

inf = sys.maxsize


def bellman_ford(
    n: int,
    start: int,
    edges: list[tuple[int, int, int]],
) -> tuple[bool, list[int], list[int | None]]:
    distances: list[int] = [inf] * n
    distances[start] = 0
    parents: list[int | None] = [None] * n

    for _ in range(n - 1):
        for u, v, w in edges:
            if distances[u] + w < distances[v]:
                distances[v] = distances[u] + w
                parents[v] = u

    for u, v, w in edges:
        if distances[u] + w < distances[v]:
            return True, distances, parents

    return False, distances, parents


def run_tests() -> None:
    tests = [
        (
            5, 0,
            [(0, 1, 1), (0, 2, 5), (1, 3, 10), (2, 3, 2)],
            (
                False,
                [0, 1, 5, 7, inf],
                [None, 0, 0, 2, None],
            )
        ),
        (
            5, 1,
            [(0, 1, 1), (0, 2, 5), (1, 3, 10), (2, 3, 2)],
            (
                False,
                [inf, 0, inf, 10, inf],
                [None, None, None, 1, None],
            ),
        ),
        (
            5, 4,
            [(0, 1, 1), (0, 2, 5), (1, 3, 10), (2, 3, 2)],
            (
                False,
                [inf, inf, inf, inf, 0],
                [None, None, None, None, None],
            ),
        ),
        (
            4, 0,
            [(0, 1, 1), (1, 2, 1), (2, 3, 1), (0, 3, 100)],
            (
                False,
                [0, 1, 2, 3],
                [None, 0, 1, 2],
            ),
        ),
        (
            4, 0,
            [(0, 1, 1), (1, 2, -1), (2, 3, -2), (0, 3, 100)],
            (
                False,
                [0, 1, 0, -2],
                [None, 0, 1, 2],
            ),
        ),
        (
            3, 0,
            [(0, 1, -1), (1, 2, -1), (2, 1, -1)],
            (
                True,
                [],
                [],
            ),
        ),
    ]

    for n_test, (n, start, edges, expected) in enumerate(tests):
        result = bellman_ford(n, start, edges)
        if expected[0]:
            if expected[0] != result[0]:
                raise Exception(f'Distances test #{n_test} failed:'
                                f'\nhas_cyle={result[0]}, \nexpected={expected[0]}')
        elif result != expected:
            raise Exception(f'Distances test #{n_test} failed:'
                            f'\nresult={result}, \nexpected={expected}')

    print('Success!')


if __name__ == '__main__':
    run_tests()
