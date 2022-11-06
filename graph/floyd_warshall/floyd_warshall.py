import sys

inf = sys.maxsize


def _distances(n: int, edges: list[tuple[int, int, int]]) -> list[list[int]]:
    distances = [[inf for _ in range(n)] for _ in range(n)]
    for i in range(n):
        distances[i][i] = 0
    for u, v, w in edges:
        distances[u][v] = w
        distances[v][u] = w
    return distances


def _parents(n: int, edges: list[tuple[int, int, int]]) -> list[list[int | None]]:
    parents: list[list[int | None]] = [[None for _ in range(n)] for _ in range(n)]
    for u, v, _ in edges:
        parents[v][u] = v
        parents[u][v] = u
    return parents


def floyd_warshall(
    n: int,
    edges: list[tuple[int, int, int]],
) -> tuple[list[list[int]], list[list[int | None]]]:
    distances = _distances(n, edges)
    parents = _parents(n, edges)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distances[i][k] + distances[k][j] < distances[i][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]
                    parents[i][j] = parents[k][j]

    return distances, parents


def run_tests() -> None:
    tests = [
        (
            5,
            [(0, 1, 1), (0, 2, 5), (1, 3, 10), (2, 3, 2)],
            (
                [
                    [0, 1, 5, 7, inf],
                    [1, 0, 6, 8, inf],
                    [5, 6, 0, 2, inf],
                    [7, 8, 2, 0, inf],
                    [inf, inf, inf, inf, 0],
                ],
                [
                    [None, 0, 0, 2, None],
                    [1, None, 0, 2, None],
                    [2, 0, None, 2, None],
                    [2, 0, 3, None, None],
                    [None, None, None, None, None],
                ],
            )
        ),
    ]

    for n_test, (n, edges, expected) in enumerate(tests):
        result = floyd_warshall(n, edges)
        if result != expected:
            raise Exception(f'Test #{n_test} failed:'
                            f'\nresult={result}, \nexpected={expected}')

    print('Success!')


if __name__ == '__main__':
    run_tests()
