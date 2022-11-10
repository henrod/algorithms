'''
https://leetcode.com/problems/subtree-of-another-tree/
'''


class Node:
    def __init__(self, val: str) -> None:
        self.val = val
        self.left: Node | None = None
        self.right: Node | None = None


def to_tree(values: list[str | None], i: int) -> Node | None:
    if i >= len(values):
        return None

    value = values[i]
    if value is None:
        return None

    node = Node(value)
    node.left = to_tree(values, 2 * i + 1)
    node.right = to_tree(values, 2 * i + 2)

    return node


def _serialize(root: Node | None) -> str:
    arr = []

    def dfs(node: Node | None):
        if not node:
            arr.append(' #')
            return

        arr.append(f' {node.val}')
        dfs(node.left)
        dfs(node.right)

    dfs(root)

    return ''.join(arr)


def is_subtree(root: Node | None, subroot: Node | None) -> bool:
    root_s = _serialize(root)
    subroot_s = _serialize(subroot)
    return subroot_s in root_s


def run_tests() -> None:
    tests: list[tuple[
        list[str | None], list[str | None], bool
    ]] = [
        (['4', '5'], ['4', None, '5'], False),
        (['3', '4', '5', '1', '2'], ['4', '1', '2'], True),
        (['11'], ['1'], False),
        (['3', '4', '5', '1', '2', None, None, None, None, '0'], ['4', '1', '2'], False),
    ]

    for n_test, (tree_values, subtree_values, expected) in enumerate(tests):
        root = to_tree(tree_values, 0)
        subroot = to_tree(subtree_values, 0)

        result = is_subtree(root, subroot)
        if result != expected:
            raise Exception(f'Test #{n_test} failed:'
                            f'\nresult={result}\nexpected={expected}')

    print('Success!')


if __name__ == '__main__':
    run_tests()
