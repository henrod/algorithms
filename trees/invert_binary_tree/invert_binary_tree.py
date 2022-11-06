from collections import deque


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left: Node | None = None
        self.right: Node | None = None

    def __repr__(self) -> str:
        if not self:
            return 'null'
        return f'{self.value}: [{self.left}, {self.right}]'


def build_list(head: Node | None) -> list[int | None]:
    r: list[int | None] = []

    queue = deque([head])
    while queue:
        node = queue.popleft()
        if not node:
            r.append(None)
            continue

        r.append(node.value)
        queue.append(node.left)
        queue.append(node.right)

    while r and r[-1] is None:
        r.pop()

    return r


def build_tree(nums: list[int]) -> Node | None:
    if not nums:
        return None

    def _build(i: int) -> Node | None:
        if i >= len(nums) or nums[i] is None:
            return None

        node = Node(nums[i])
        node.left = _build(2 * i + 1)
        node.right = _build(2 * i + 2)
        return node

    return _build(0)


def invert(root: Node | None) -> Node | None:
    if not root:
        return None

    root.left, root.right = root.right, root.left
    invert(root.left)
    invert(root.right)

    return root


def run_tests():
    tests = [
        ([1, 2, 3], [1, 3, 2]),
        ([1, 2, None], [1, None, 2]),
        ([1, 2, None, 3, 4], [1, None, 2, 4, 3]),
    ]

    for n_test, (nums, expected) in enumerate(tests):
        root = build_tree(nums)
        root = invert(root)
        result = build_list(root)
        if result != expected:
            raise Exception(f'Test #{n_test} failed: ',
                            f'result={result}, expected={expected}')

    print('Success!')


if __name__ == '__main__':
    run_tests()
