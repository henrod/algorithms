'''
https://leetcode.com/problems/subtree-of-another-tree/

Idea: each node is the hash of its value and the hash of its subtrees.
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


def is_subtree(root: Node | None, subroot: Node | None) -> bool:
    hashes = set()

    def to_hash(node: Node | None, add: bool) -> str:
        if not node:
            return ' #'

        h = str(hash(
            ' ' +
            node.val +
            to_hash(node.left, add) +
            to_hash(node.right, add)
        ))

        if add:
            hashes.add(h)

        return h

    to_hash(root, True)
    h = to_hash(subroot, False)

    return h in hashes


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
