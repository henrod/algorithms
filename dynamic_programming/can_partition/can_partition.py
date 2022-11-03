'''
Given a non-empty array nums containing only positive integers,
find if the array can be partitioned into two subsets such
that the sum of elements in both subsets is equal.
'''


def can_partition(nums: list[int]) -> bool:
    total_sum = sum(nums)
    if total_sum & 1 == 1:
        return False

    target_sum = total_sum // 2

    sums = {0}
    for num in nums:
        sums |= {s + num for s in sums}

    return target_sum in sums


if __name__ == '__main__':
    tests = [
        ([5, 1, 5, 11], True),
        ([1, 2, 3, 5], False),
        ([1, 2, 3, 0], True),
        ([3, 3, 3, 3], True),
    ]

    for n_test, (nums, expected) in enumerate(tests):
        result = can_partition(nums)
        if result != expected:
            raise Exception(f'Test #{n_test} failed:'
                            f'result={result}, expected={expected}')

    print('Success!')
