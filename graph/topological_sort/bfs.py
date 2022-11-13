from collections import deque


def topological_sort(n: int, edges: list[tuple[int, int]]) -> list[int]:
    roots = {v for v in range(n)}
    graph: list[list[int]] = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        if v in roots:
            roots.remove(v)

    r: list[int] = []
    queue = deque(roots)
    visited: set[int] = set()

    while queue:
        node = queue.popleft()
        visited.add(node)
        r.append(node)

        for adj in graph[node]:
            if adj not in visited:
                visited.add(adj)
                queue.append(adj)

    return r


if __name__ == '__main__':
    tests = [
        (
            6,
            [(0, 1), (1, 2), (1, 3), (2, 4), (3, 4), (4, 5)],
            [0, 1, 2, 3, 4, 5],
        ),
        (
            6,
            [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)],
            [0, 5, 1, 2, 3, 4],
        ),
    ]

    for n_test, (n, edges, expected) in enumerate(tests):
        result = topological_sort(n, edges)
        if result != expected:
            raise Exception(f'Test {n_test} failed:'
                            f'result={result}, expected={expected}')
    print('Success!')
