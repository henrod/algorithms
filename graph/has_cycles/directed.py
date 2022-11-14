def _build_graph(n: int, edges: list[tuple[int, int]]) -> list[list[int]]:
    graph: list[list[int]] = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
    return graph


def _has_cycle(graph: list[list[int]], visited: set[int], path: set[int], vertex: int) -> bool:
    for adj in graph[vertex]:
        if adj in path:
            return True

        if adj in visited:
            continue

        visited.add(adj)
        path.add(adj)
        if _has_cycle(graph, visited, path, adj):
            return True
        path.remove(adj)

    return False


def has_cycle(n: int, edges: list[tuple[int, int]]) -> bool:
    graph = _build_graph(n, edges)
    visited: set[int] = set()
    path: set[int]

    for vertex in range(n):
        if vertex not in visited:
            path = {vertex}
            visited.add(vertex)
            if _has_cycle(graph, visited, path, vertex):
                return True

    return False


def run_tests() -> None:
    tests = [
        (3, [(0, 1), (1, 2), (2, 0)], True),
        (3, [(0, 1), (1, 2), (0, 2)], False),
        (6, [(0, 1), (1, 2), (1, 5), (2, 3), (3, 4), (4, 2)], True),
    ]

    for n_test, (matrix, dictionary, expected) in enumerate(tests):
        result = has_cycle(matrix, dictionary)
        if result != expected:
            raise Exception(f'Test #{n_test} failed: result={result}, expected={expected}')

    print('Success!')


if __name__ == '__main__':
    run_tests()
