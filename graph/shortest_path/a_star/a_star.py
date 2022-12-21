from __future__ import annotations
import math
import heapq


class Node:
    def __init__(self, is_wall: bool, row: int, col: int, src_dist: float, dst_dist: float) -> None:
        self.is_wall = is_wall
        self.src_dist = src_dist
        self.dst_dist = dst_dist
        self.row = row
        self.col = col
        self.parent: Node | None = None

    def __lt__(self, other: Node) -> bool:
        if self.dst_dist + self.src_dist == other.dst_dist + other.src_dist:
            return self.dst_dist < other.dst_dist

        return self.dst_dist + self.src_dist < other.dst_dist + other.src_dist

    def __repr__(self) -> str:
        if self.is_wall:
            return 'X              '

        return f'({self.row}, {self.col})[{self.src_dist}][{self.dst_dist}]'


def a_star(
    map: list[list[int]],
    src: tuple[int, int],
    dst: tuple[int, int],
) -> tuple[list[tuple[int, int]], float]:
    nodes = _nodes(map, src, dst)
    pq = [node for row in nodes for node in row if not node.is_wall]
    heapq.heapify(pq)
    visited: set[Node] = set()

    dst_node = nodes[dst[0]][dst[1]]

    while pq:
        node = heapq.heappop(pq)
        if node == dst_node:
            break

        visited.add(node)

        for adj_node in _adj(nodes, visited, node.row, node.col):
            new_src_dist = node.src_dist + _distance(
                (node.row, node.col),
                (adj_node.row, adj_node.col)
            )

            if new_src_dist < adj_node.src_dist:
                adj_node.src_dist = new_src_dist
                adj_node.parent = node

            adj_node.dst_dist = _distance((adj_node.row, adj_node.col), dst)

        heapq.heapify(pq)

    path: list[tuple[int, int]] = []
    path_node: Node | None = dst_node
    while path_node:
        path.append((path_node.row, path_node.col))
        path_node = path_node.parent

    return path, dst_node.src_dist


def _nodes(
    map: list[list[int]],
    src: tuple[int, int],
    dst: tuple[int, int],
) -> list[list[Node]]:
    nodes: list[list[Node]] = []

    for row in range(len(map)):
        nodes.append([])
        for col in range(len(map[row])):
            is_wall = map[row][col] == 1
            nodes[-1].append(Node(is_wall, row, col, float('inf'), float('inf')))

    nodes[src[0]][src[1]].src_dist = 0
    nodes[src[0]][src[1]].dst_dist = _distance(src, dst)

    return nodes


def _adj(nodes: list[list[Node]], visited: set[Node], row: int, col: int) -> list[Node]:
    adjs: list[Node] = []
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    n_rows = len(nodes)
    n_cols = len(nodes[0])

    for drow, dcol in directions:
        nrow, ncol = row + drow, col + dcol
        in_bound = 0 <= nrow < n_rows and 0 <= ncol < n_cols
        if not in_bound:
            continue

        is_wall = nodes[nrow][ncol].is_wall
        is_visited = nodes[nrow][ncol] in visited

        if not is_wall and not is_visited:
            adjs.append(nodes[nrow][ncol])

    return adjs


def _distance(a: tuple[int, int], b: tuple[int, int]) -> float:
    return round(math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2), 1)


def run_tests() -> None:
    tests = [
        (
            [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 1, 1, 0],
                [0, 0, 1, 0],
            ],
            (3, 1),
            (2, 3),
            5.2
        ),
        (
            [
                [0, 0, 0, 0],
                [0, 0, 1, 0],
                [0, 1, 1, 0],
                [0, 0, 1, 0],
            ],
            (3, 1),
            (3, 3),
            7.6
        ),
        (
            [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ],
            (4, 7),
            (1, 4),
            6.8
        ),
        (
            [
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ],
            (4, 7),
            (1, 4),
            9.6
        )
    ]

    for n_test, (map, src, dst, expected) in enumerate(tests):
        path, cost = a_star(map, src, dst)
        if abs(cost - expected) > 0.01:
            raise Exception(f'Test #{n_test} failed:'
                            f'\nresult={cost}, \nexpected={expected}')
        for row, col in path:
            map[row][col] = 2
        for row in map:
            print([{0: ' ', 1: '#', 2: 'o'}[v] for v in row])
        print('')

    print('Success!')


if __name__ == '__main__':
    run_tests()
