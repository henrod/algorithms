class UnionFind:
    def __init__(self, n: int) -> None:
        self._parents = [v for v in range(n)]
        self._ranks = [1 for _ in range(n)]

    def _link(self, x: int, y: int) -> None:
        if self._ranks[x] > self._ranks[y]:
            self._parents[y] = x
        else:
            if self._ranks[x] == self._ranks[y]:
                self._ranks[y] += 1
            self._parents[x] = y

    def union(self, x: int, y: int) -> None:
        self._link(self.find(x), self.find(y))

    def find(self, x: int) -> int:
        if x != self._parents[x]:
            self._parents[x] = self.find(self._parents[x])
        return self._parents[x]


def kruskal(n: int, edges: list[tuple[int, int, int]]) -> list[tuple[int, int]]:
    mst: list[tuple[int, int]] = []
    union_find = UnionFind(n)

    edges.sort(key=lambda edge: edge[2])
    for u, v, _ in edges:
        if union_find.find(u) != union_find.find(v):
            union_find.union(u, v)
            mst.append((u, v))

    return mst


def run_tests() -> None:
    tests = [
        (
            4,
            [(0, 1, 1), (0, 2, 5), (1, 3, 10), (2, 3, 2)],
            [(0, 1), (2, 3), (0, 2)],
        ),
        (
            4,
            [(0, 1, 1), (1, 2, 1), (2, 3, 1), (0, 3, -10)],
            [(0, 3), (0, 1), (1, 2)],
        ),
    ]

    for n_test, (n, edges, expected) in enumerate(tests):
        result = kruskal(n, edges)
        if result != expected:
            raise Exception(f'Test #{n_test} failed:'
                            f'\nresult={result}\nexpected={expected}')

    print('Success!')


if __name__ == '__main__':
    run_tests()
