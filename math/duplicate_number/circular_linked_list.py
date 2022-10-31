'''
Given an array of integers nums containing n + 1 integers where each
integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

Idea: read nums as a linked list, where index is the of the node
and value is the next node. The duplicate value means that
there is a cycle.
The applied technique is then the one to find the entry point
of a cycle in a linked list, which is the duplicate value.
'''


def find_duplicate(nums: list[int]) -> int:
    slow = nums[0]
    fast = nums[nums[0]]

    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]

    fast = 0

    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow


def run_tests():
    tests = [
        ([1, 3, 4, 2, 2], 2),
        ([3, 1, 3, 4, 2], 3),
        ([2, 2, 2, 2], 2)
    ]

    for n_test, (nums, expected) in enumerate(tests):
        result = find_duplicate(nums)
        if result != expected:
            raise Exception(f'Test #{n_test} failed: ',
                            f'result={result}, expected={expected}')

    print('Success!')


if __name__ == '__main__':
    run_tests()
