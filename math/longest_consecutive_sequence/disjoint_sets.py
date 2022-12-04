from __future__ import annotations


class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.rank = 1
        self.parent = self
        self.size = 1

    def __repr__(self) -> str:
        return f'{self.value}[{self.parent.value}]{{{self.size}}}'

    def root(self) -> Node:
        if self != self.parent:
            self.parent = self.parent.root()

        return self.parent

    def union(self, node: Node) -> None:
        root1 = self.root()
        root2 = node.root()

        if root1.rank > root2.rank:
            root2.parent = root1
            root1.size += root2.size
        elif root1.rank < root2.rank:
            root1.parent = root2
            root2.size += root1.size
        else:
            root2.parent = root1
            root1.rank += 1
            root1.size += root2.size


def longest_consecutive_sequence(nums: list[int]) -> int:
    nodes: dict[int, Node] = {}
    for num in nums:
        if num in nodes:
            continue

        nodes[num] = Node(num)

        if num - 1 in nodes:
            nodes[num].union(nodes[num - 1])
        if num + 1 in nodes:
            nodes[num].union(nodes[num + 1])

    max_size = 0
    for node in nodes.values():
        max_size = max(max_size, node.size)
    return max_size


def run_tests():
    tests = [
        ([4, 1, 3, 2], 4),
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([], 0),
        ([1, 3, 5, 7], 1),
        ([1, 3, 5, 7, 2, 6], 3),
        ([1, 3, 5, 7, 2, 6, 4], 7),
        ([1, 3, 5, 7, 2, 6, 4, 3, 5], 7),
        ([1, 1, 1, 1], 1),
        ([0, 0, 1, -1], 3),
        ([2, -1, 0, 1], 4),
    ]

    for n_test, (nums, expected) in enumerate(tests):
        result = longest_consecutive_sequence(nums)
        if result != expected:
            raise Exception(f'Test #{n_test} failed:'
                            f'result={result}, expected={expected}')

    print('Success!')


if __name__ == '__main__':
    run_tests()
