'''
Given a binary array nums, return the maximum length of a
contiguous subarray with an equal number of 0 and 1.

https://leetcode.com/problems/contiguous-array/
'''


def contiguous_subarray(nums: list[int]) -> int:
    previous: dict[int, int] = {}
    max_len = 0

    for i, num in enumerate(nums):
        diff = 1 if num == 1 else -1
        nums[i] = nums[i - 1] + diff if i > 0 else diff

        if nums[i] == 0:
            max_len = i + 1
        elif nums[i] in previous and i - previous[nums[i]] > max_len:
            max_len = i - previous[nums[i]]
        else:
            previous[nums[i]] = i

    return max_len


def run_tests():
    tests = [
        ([0, 1], 2),
        ([0, 1, 0], 2),
        ([0, 1, 1, 1, 0], 2),
        ([0, 1, 1, 0], 4),
    ]

    for n_test, (nums, expected) in enumerate(tests):
        result = contiguous_subarray(nums)
        if result != expected:
            raise Exception(f'Test #{n_test} failed: ',
                            f'result={result}, expected={expected}')

    print('Success!')


if __name__ == '__main__':
    run_tests()
