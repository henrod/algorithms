'''
https://leetcode.com/problems/maximum-alternating-subsequence-sum/
'''


def max_alternating_sum_rec(nums: list[int]) -> int:
    memo: dict[tuple[int, int], int] = {}

    def _max_alternating_sum(i: int, signal: int) -> int:
        if i >= len(nums):
            return 0

        key = (i, signal)
        if key in memo:
            return memo[key]

        include = _max_alternating_sum(i + 1, -signal) + signal * nums[i]
        not_include = _max_alternating_sum(i + 1, signal)

        memo[key] = max(include, not_include)

        return memo[key]

    return _max_alternating_sum(0, 1)


def max_alternating_sum(nums: list[int]) -> int:
    # sumEven represents the max sum of an even number of nums after index i.
    # Same for sumOdd.
    sumEven, sumOdd = 0, 0

    for i in range(len(nums) - 1, -1, -1):
        # The new sumEvem will be either:
        # - getting nums[i] plus the max sum of an odd number of nums after i
        # - not getting nums[i] and keeping the previous sumEven value
        # Same for sumOdd.
        tempEven = max(+nums[i] + sumOdd, sumEven)
        tempOdd = max(-nums[i] + sumEven, sumOdd)
        sumEven = tempEven
        sumOdd = tempOdd

    # We always want to get even numbers. If odd, the last number of
    # the sequence would only be subtracting from a possible max.
    return sumEven


if __name__ == '__main__':
    tests = [
        ([4, 2, 5, 3], 7),
        ([5, 6, 7, 8], 8),
        ([6, 2, 1, 2, 4, 5], 10),
    ]

    for n_test, (nums, expected) in enumerate(tests):
        result = max_alternating_sum(nums)
        if result != expected:
            raise Exception(f'Test #{n_test} failed:'
                            f'result={result}, expected={expected}')

    print('Success!')
