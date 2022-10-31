'''
Given an array of integers nums containing n + 1 integers where each
integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

Idea: use the array as the visited record by changing the signal of the value
in idx=num.
'''


def find_duplicate(nums: list[int]) -> int:
    for num in nums:
        num = abs(num)
        if nums[num] < 0:  # if negative, then it's already seen
            return num
        nums[num] = -nums[num]

    return -1


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
