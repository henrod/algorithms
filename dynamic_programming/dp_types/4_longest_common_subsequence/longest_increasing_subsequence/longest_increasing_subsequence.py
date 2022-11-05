'''
https://leetcode.com/problems/longest-increasing-subsequence/
'''


def longest_increasing_subsequence(nums: list[int]) -> int:
    # lsi starting at position i
    dp = [1] * len(nums)

    for i in range(len(nums) - 2, -1, -1):
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1

    return max(dp)


if __name__ == '__main__':
    tests = [
        ([1, 2, 4, 3], 3),
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([0, 1, 0, 3, 2, 3], 4),
        ([7, 7, 7, 7], 1),
    ]

    for n_test, (nums, expected) in enumerate(tests):
        result = longest_increasing_subsequence(nums)
        if result != expected:
            raise Exception(f'Test #{n_test} failed:'
                            f'result={result}, expected={expected}')

    print('Success!')
