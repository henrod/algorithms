def _build_graph(n: int, edges: list[tuple[int, int]]) -> list[list[int]]:
    graph: list[list[int]] = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph


def _has_cycle(graph: list[list[int]], visited: set[int], parent: int | None, vertex: int) -> bool:
    for adj in graph[vertex]:
        if adj == parent:
            continue

        if adj in visited:
            return True

        visited.add(adj)
        if _has_cycle(graph, visited, vertex, adj):
            return True

    return False


def has_cycle(n: int, edges: list[tuple[int, int]]) -> bool:
    graph = _build_graph(n, edges)
    visited: set[int] = set()

    for vertex in range(n):
        if vertex not in visited:
            parent = None
            visited.add(vertex)
            if _has_cycle(graph, visited, parent, vertex):
                return True

    return False


def run_tests() -> None:
    tests = [
        (3, [(0, 1), (1, 2), (2, 0)], True),
        (3, [(0, 1), (1, 2), (0, 2)], True),
        (6, [(0, 1), (1, 2), (1, 5), (2, 3), (3, 4), (4, 2)], True),
        (4, [(0, 1), (1, 2), (0, 3)], False),
    ]

    for n_test, (matrix, dictionary, expected) in enumerate(tests):
        result = has_cycle(matrix, dictionary)
        if result != expected:
            raise Exception(f'Test #{n_test} failed: result={result}, expected={expected}')

    print('Success!')


if __name__ == '__main__':
    run_tests()
