'''
Given a graph, return the number of strongly connected components.
'''


def build_graph(n: int, edges: list[tuple[int, int]]) -> dict[int, list[int]]:
    graph: dict[int, list[int]] = {v: [] for v in range(n)}
    for u, v in edges:
        graph[u].append(v)
    return graph


def transpose_graph(graph: dict[int, list[int]]) -> dict[int, list[int]]:
    tgraph: dict[int, list[int]] = {v: [] for v in range(len(graph))}

    for u, adj in graph.items():
        for v in adj:
            tgraph[v].append(u)

    return tgraph


def dfs(graph: dict[int, list[int]], vertex: int, visited: set[int], r: list[int] | None) -> None:
    for adj in graph[vertex]:
        if adj not in visited:
            visited.add(adj)
            dfs(graph, adj, visited, r)

    if r is not None:
        r.append(vertex)


def strongly_connected_components(n: int, edges: list[tuple[int, int]]) -> int:
    graph = build_graph(n, edges)

    # DFS to save finish time by appending to r
    visited: set[int] = set()
    r: list[int] = []
    for vertex in range(n):
        if vertex not in visited:
            dfs(graph, vertex, visited, r)

    # Transpose the graph
    graph = transpose_graph(graph)

    # DFS in ascending order of finish time
    visited = set()
    roots: list[int] = []
    for vertex in r[::-1]:
        if vertex not in visited:
            dfs(graph, vertex, visited, None)
            roots.append(vertex)

    # Roots of the strongly connected components
    return len(roots)


if __name__ == '__main__':
    tests = [
        (
            3,
            [(0, 1), (1, 0), (0, 2)],
            2
        ),
        (
            8,
            [(0, 4), (1, 0), (2, 1), (2, 3), (3, 2), (4, 1),
             (5, 1), (5, 6), (6, 5), (6, 2), (7, 6), (7, 3)],
            4
        ),
    ]

    for n_test, (n, edges, expected) in enumerate(tests):
        result = strongly_connected_components(n, edges)
        if result != expected:
            raise Exception(f'Test #{n_test} failed:'
                            f' result={result}, expected={expected}')
    print('Success!')
