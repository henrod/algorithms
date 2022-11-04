'''
Given a non-empty array nums containing only positive integers, 
find if the array can be partitioned into two subsets such that 
the sum of elements in both subsets is equal.

https://leetcode.com/problems/partition-equal-subset-sum/
'''


def can_partition(nums: list[int]) -> bool:
    total_sum = sum(nums)
    if total_sum % 1 == 1:
        return False

    target_sum = total_sum // 2

    sums = set([0])
    for num in nums:
        next_sums = sums.copy()
        for s in sums:
            if s + num == target_sum:
                return True

            next_sums.add(s + num)
        sums = next_sums

    return False


if __name__ == '__main__':
    tests = [
        ([1, 5, 11, 5], True),
        ([1, 2, 3, 5], True),
        ([1, 1, 1, 1], True),
        ([2, 4, 10, 20], False),
    ]

    for n_test, (nums, expected) in enumerate(tests):
        result = can_partition(nums)
        if result != expected:
            raise Exception(f'Test #{n_test} failed:'
                            f'result={result}, expected={expected}')

    print('Success!')
