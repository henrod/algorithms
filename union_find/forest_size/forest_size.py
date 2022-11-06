'''
Given a list of edges between vertices, return the number
of disconnected graphs.

1-->2-->3
4-->5
Result: 2
'''


class UnionFind:
    def __init__(self, n: int) -> None:
        self._parents = [i for i in range(n)]
        self._ranks = [1 for _ in range(n)]

    def union(self, x: int, y: int) -> None:
        root_x = self.find(x)
        root_y = self.find(y)

        if self._ranks[root_x] < self._ranks[root_y]:
            self._parents[root_x] = self._parents[root_y]
        else:
            if self._ranks[root_x] == self._ranks[root_y]:
                self._ranks[root_x] += 1

            self._parents[root_y] = self._parents[root_x]

    def find(self, x: int) -> int:
        if self._parents[x] != x:
            self._parents[x] = self.find(self._parents[x])

        return self._parents[x]


def forest_size(n: int, edges: list[tuple[int, int]]) -> int:
    union_find = UnionFind(n)
    for u, v in edges:
        union_find.union(u, v)

    roots = {union_find.find(v) for v in range(n)}

    return len(roots)


if __name__ == '__main__':
    tests = [
        (4, [(0, 1), (0, 2), (1, 2)], 2),
        (6, [(0, 1), (0, 2), (2, 3), (3, 4)], 2),
        (6, [(0, 1)], 5),
        (6, [(0, 1), (2, 3), (4, 5), (0, 5)], 2),
    ]

    for n_test, (n, edges, expected) in enumerate(tests):
        result = forest_size(n, edges)
        if result != expected:
            raise Exception(f'Test {n_test} failed:'
                            f'result={result}, expected={expected}')
    print('Success!')
