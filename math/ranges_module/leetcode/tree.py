class RangeModule:
    class _Node:
        def __init__(self, left_range: int, right_range: int) -> None:
            self.contains = False
            self.left_range = left_range
            self.right_range = right_range
            self.left: RangeModule._Node | None = None
            self.right: RangeModule._Node | None = None

        def __repr__(self) -> str:
            return f'[{self.left_range}, {self.right_range}]{self.contains}\n{self.left}\n{self.right}'

    def __init__(self):
        self._root = self._Node(0, 1)

    def addRange(self, left: int, right: int) -> None:
        while right >= self._root.right_range:
            node = self._Node(0, 2 * self._root.right_range)
            node.left = self._root
            self._root = node

        self._add_range(self._root, left, right - 1)

    def removeRange(self, left: int, right: int) -> None:
        self._remove_range(self._root, left, min(right - 1, self._root.right_range))

    def queryRange(self, left: int, right: int) -> bool:
        return self._query_range(self._root, left, right - 1)

    def _add_range(self, node: _Node, left: int, right: int) -> None:
        if left > right:
            return

        if left == node.left_range and right == node.right_range:
            node.contains = True
            return

        m = (node.left_range + node.right_range) // 2
        node.left = node.left or self._Node(node.left_range, m)
        node.right = node.right or self._Node(m + 1, node.right_range)

        if right <= m:
            self._add_range(node.left, left, right)
        elif left > m:
            self._add_range(node.right, left, right)
        else:
            self._add_range(node.left, left, m)
            self._add_range(node.right, m + 1, right)

    def _remove_range(self, node: _Node | None, left: int, right: int) -> None:
        if not node:
            return

        if left > right:
            return

        if left == node.left_range and right == node.right_range:
            node.contains = False
            node.left = node.right = None
            return

        m = (node.left_range + node.right_range) // 2
        node.left = node.left or self._Node(node.left_range, m)
        node.right = node.right or self._Node(m + 1, node.right_range)

        if right <= m:
            self._remove_range(node.left, left, right)
        elif left > m:
            self._remove_range(node.right, left, right)
        else:
            self._remove_range(node.left, left, m)
            self._remove_range(node.right, m + 1, right)

        if node.contains:
            self._add_range(node, node.left_range, left - 1)
            self._add_range(node, right + 1, node.right_range)

        node.contains = False

    def _query_range(self, node: _Node | None, left: int, right: int) -> bool:
        if not node:
            return False
        if node.contains:
            return True

        m = (node.left_range + node.right_range) // 2
        if right <= m:
            return self._query_range(node.left, left, right)
        elif left > m:
            return self._query_range(node.right, left, right)
        else:
            return self._query_range(node.left, left, m) and \
                self._query_range(node.right, m + 1, right)


def run_tests() -> None:
    tests: list[list[tuple[str, int, int] | tuple[str, int, int, bool]]] = [
        [
            ('add', 5, 7),
            ('query', 2, 7, False),
            ('add', 6, 9),
            ('query', 2, 9, False),
            ('add', 2, 7),
            ('remove', 3, 10),
            ('remove', 1, 8),
            ('remove', 1, 10),
            ('query', 4, 7, False),
        ],

        [
            ('add', 1, 10),
            ('remove', 4, 6),
            ('query', 6, 7, True),
        ],

        [
            ('add', 10, 20),
            ('remove', 14, 16),
            ('query', 10, 14, True),
            ('query', 13, 15, False),
            ('query', 16, 17, True),
        ],

        [
            ('add', 8, 12),
            ('query', 9, 10, True),
            ('query', 9, 15, False),
            ('query', 1, 3, False),
            ('add', 16, 20),
            ('query', 16, 18, True),
            ('query', 20, 22, False),
            ('query', 13, 22, False),
        ],

        [
            ('add', 0, 15),
            ('remove', 0, 7),
            ('remove', 8, 10),
            ('query', 12, 15, True),
            ('query', 5, 10, False),
        ],

        [
            ('add', 0, 20),
            ('query', 10, 14, True),
            ('remove', 12, 16),
            ('query', 13, 15, False),
            ('query', 16, 17, True),
        ],

        [
            ('add', 10, 20),
            ('query', 10, 14, True),
            ('remove', 14, 16),
            ('query', 13, 15, False),
            ('add', 25, 30),
            ('query', 18, 28, False),
            ('query', 28, 29, True),
            ('remove', 29, 40),
            ('query', 27, 28, True),
            ('remove', 0, 5),
            ('query', 11, 13, True),
        ],

        [
            ('add', 6, 8),
            ('remove', 7, 8),
            ('remove', 8, 9),
            ('add', 8, 9),
            ('remove', 1, 3),
            ('add', 1, 8),
            ('query', 2, 4, True),
            ('query', 2, 9, True),
            ('query', 4, 6, True),
        ],
    ]

    for n_testset, test_set in enumerate(tests):
        range_module = RangeModule()
        for n_test, test in enumerate(test_set):
            start, end = test[1:3]

            if test[0] == 'add':
                range_module.addRange(start, end)
            elif test[0] == 'remove':
                range_module.removeRange(start, end)
            elif test[0] == 'query':
                expected = test[3]
                result = range_module.queryRange(start, end)
                if result != expected:
                    raise Exception(f'Test #{n_testset}/{n_test} failed:'
                                    f'result={result}, expected={expected}')

    print('Success!')


if __name__ == '__main__':
    run_tests()
