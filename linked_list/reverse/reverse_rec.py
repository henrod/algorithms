'''
Reverse a singly linked list.
'''


class Node:
    def __init__(self, value: int) -> None:
        self.val = value
        self.next: Node | None = None


def build_linked_list(nums: list[int]) -> Node | None:
    head = None

    for num in nums[::-1]:
        node = Node(num)
        node.next = head
        head = node

    return head


def build_list(head: Node | None) -> list[int]:
    r = []

    while head:
        r.append(head.val)
        head = head.next

    return r


def _reverse(node: Node | None) -> tuple[Node | None, Node | None]:
    if not node or not node.next:
        return node, node

    tail, head = _reverse(node.next)
    tail.next = node

    return node, head


def reverse(head: Node | None) -> Node | None:
    if not head:
        return None
    tail, head = _reverse(head)
    tail.next = None
    return head


def run_tests():
    tests = [
        ([1, 2, 3], [3, 2, 1]),
        ([1, 2, 3, 4], [4, 3, 2, 1]),
        ([], []),
    ]

    for n_test, (nums, expected) in enumerate(tests):
        head = build_linked_list(nums)
        head = reverse(head)
        result = build_list(head)
        if result != expected:
            raise Exception(f'Test #{n_test} failed: ',
                            f'result={result}, expected={expected}')

    print('Success!')


if __name__ == '__main__':
    run_tests()
