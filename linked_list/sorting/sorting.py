'''
Sort a singly linked list in O(NlogN) time and O(1) space.
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


def _mergesort(head: Node | None) -> Node | None:
    if not head or not head.next:
        return head

    prev_slow: Node | None = None
    slow = head
    fast = head
    while fast and fast.next:
        prev_slow = slow
        slow = slow.next
        fast = fast.next.next

    prev_slow.next = None
    left = _mergesort(head)
    right = _mergesort(slow)

    dummy = node = Node(0)

    while left and right:
        if left.val <= right.val:
            node.next = left
            node = left
            left = left.next
        else:
            node.next = right
            node = right
            right = right.next

    node.next = left or right

    return dummy.next


def sort(head: Node | None) -> Node | None:
    return _mergesort(head)


def run_tests():
    tests = [
        ([4, 3, 2], [2, 3, 4]),
        ([3, 2], [2, 3]),
        ([2, 1, 3], [1, 2, 3]),
        ([2, 1, 3, 3, 1], [1, 1, 2, 3, 3]),
        ([2, 2, 2, 2], [2, 2, 2, 2]),
        ([1, 2, 3, 4], [1, 2, 3, 4]),
        ([4, 3, 2, 1], [1, 2, 3, 4]),
        ([1, 3, 2], [1, 2, 3]),
        ([3, 2], [2, 3])
    ]

    for n_test, (nums, expected) in enumerate(tests):
        head = build_linked_list(nums)
        head = sort(head)
        result = build_list(head)
        if result != expected:
            raise Exception(f'Test #{n_test} failed: ',
                            f'result={result}, expected={expected}')

    print('Success!')


if __name__ == '__main__':
    run_tests()
