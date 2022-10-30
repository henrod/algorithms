'''
Given an integer array nums, return the length of the longest strictly
increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting
some or no elements without changing the order of the remaining elements.

For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
'''


'''
The idea is to keep memo[i] as the LSI (longest increasing subsequence)
until i.

When filling i, we check all j before i. If nums[j] is less then nums[i],
we can include i in its LSI, getting the value memo[j]+1.

For every j before i, we save the largest one.

As final result, we get the max value in memo because we don't
know in which i the maximum LSI is terminating.
'''


def longest_increasing_subsequence(nums: list[int]) -> int:
    memo = [1] * len(nums)

    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i] and memo[i] < memo[j] + 1:
                memo[i] = memo[j] + 1

    return max(memo)


def run_tests():
    tests = [
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([0, 1, 0, 3, 2, 3], 4),
        ([7, 7, 7, 7, 7, 7, 7], 1),
        ([1, 3, 6, 7, 9, 4, 10, 5, 6], 6),
    ]

    for n_test, (nums, expected) in enumerate(tests):
        result = longest_increasing_subsequence(nums)
        if result != expected:
            raise BaseException(f'Test #{n_test} failed: '
                                f'result={result}, expected={expected}')

    print('Success!')


if __name__ == '__main__':
    run_tests()
