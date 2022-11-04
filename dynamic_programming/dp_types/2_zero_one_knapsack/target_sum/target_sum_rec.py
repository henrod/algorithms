'''
https://leetcode.com/problems/target-sum/
'''


def target_sum_rec(nums: list[int], target: int) -> int:
    # (index, sub_target) -> quantity
    # sub_target because we are dividing into subproblems by backtracking
    dp: dict[tuple[int, int], int] = {}

    def backtrack(i: int, sub_target: int) -> int:
        if i >= len(nums):
            return 1 if sub_target == target else 0

        key = (i, sub_target)
        if key in dp:
            return dp[key]

        dp[key] = (
            backtrack(i + 1, sub_target + nums[i]) +
            backtrack(i + 1, sub_target - nums[i])
        )

        return dp[key]

    return backtrack(0, 0)


if __name__ == '__main__':
    tests = [
        ([1, 1, 1, 1, 1], 3, 5),
        ([0, 0, 0, 1], 1, 8),
        ([1], 1, 1),
    ]

    for n_test, (nums, target, expected) in enumerate(tests):
        result = target_sum_rec(nums, target)
        if result != expected:
            raise Exception(f'Test #{n_test} failed:'
                            f'result={result}, expected={expected}')

    print('Success!')
