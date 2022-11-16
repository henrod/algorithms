class SegmentTree:
    def __init__(self, nums: list[int]) -> None:
        self._tree = SegmentTree._build_tree(nums)
        self._n = len(nums)

    def sum(self, start: int, end: int) -> int:
        return self._sum(start, end, 0, self._n - 1, 0)

    def update(self, idx: int, value: int) -> None:
        self._update(0, self._n - 1, idx, 0, value)

    def _update(self, left: int, right: int, idx: int, tree_idx: int, value: int) -> None:
        if left > right:
            return

        if left == right:
            self._tree[tree_idx] = value
            return

        mid = (left + right) // 2
        if idx <= mid:
            self._update(left, mid, idx, 2 * tree_idx + 1, value)
        elif idx > mid:
            self._update(mid+1, right, idx, 2 * tree_idx + 2, value)

        self._tree[tree_idx] = self._tree[2 * tree_idx + 1] + self._tree[2 * tree_idx + 2]

    def _sum(self, start: int, end: int, left: int, right: int, idx: int) -> int:
        if (start, end) == (left, right):
            return self._tree[idx]

        mid = (left + right) // 2
        if end <= mid:
            return self._sum(start, end, left, mid, 2 * idx + 1)
        elif start > mid:
            return self._sum(start, end, mid + 1, right, 2 * idx + 2)
        else:
            return (
                self._sum(start, mid, left, mid, 2 * idx + 1) +
                self._sum(mid + 1, end, mid + 1, right, 2 * idx + 2)
            )

    @staticmethod
    def _build_tree(nums: list[int]) -> list[int]:
        tree: list[int] = []

        def _segment_tree(left: int, right: int, idx: int) -> None:
            if left > right:
                return

            if idx >= len(tree):
                tree.extend([0] * (idx - len(tree) + 1))

            if left == right:
                tree[idx] = nums[left]
                return

            mid = (left + right) // 2
            _segment_tree(left, mid, 2 * idx + 1)
            _segment_tree(mid + 1, right, 2 * idx + 2)

            tree[idx] = tree[2 * idx + 1] + tree[2 * idx + 2]

        _segment_tree(0, len(nums) - 1, 0)

        return tree


def run_tests():
    tests = [
        (
            [1, 2, 3, 4],
            [(0, 3), (1, 2), (3, 3), (0, 2)],
            [10, 3, 7, 1, 2, 3, 4],
            (0, 10),
            [10, 5, 4, 6],
            [19, 5, 4, 15],
        ),
        (
            [1, 2, 3, 4, 5],
            [(0, 3), (1, 2), (3, 3), (0, 2), (0, 4)],
            [15, 6, 9, 3, 3, 4, 5, 1, 2],
            (4, 10),
            [10, 5, 4, 6, 15],
            [10, 5, 4, 6, 20],
        ),
    ]

    for n_test, (
        nums, ranges, expected_tree, update, expected_sums, expected_updated_sums
    ) in enumerate(tests):
        tree = SegmentTree(nums)
        if tree._tree != expected_tree:
            raise Exception(f'Test #{n_test} failed for array:\n'
                            f'result={tree._tree}\nexpect={expected_tree}')

        for i, (start, end) in enumerate(ranges):
            result = tree.sum(start, end)
            if result != expected_sums[i]:
                raise Exception(f'Test #{n_test} failed for sum:\n'
                                f'result={result}\nexpect={expected_sums[i]}')

        update_idx, update_value = update
        tree.update(update_idx, update_value)
        for i, (start, end) in enumerate(ranges):
            result = tree.sum(start, end)
            if result != expected_updated_sums[i]:
                raise Exception(f'Test #{n_test} failed for sum:\n'
                                f'result={result}\nexpect={expected_sums[i]}')

    print('Success!')


if __name__ == '__main__':
    run_tests()
