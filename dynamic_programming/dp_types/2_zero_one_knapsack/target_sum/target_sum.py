'''
https://leetcode.com/problems/target-sum/

Idea: nums=[1,1,1], target=1
Possibilities:
+1 +1 +1 = 3
+1 +1 -1 = 1
+1 -1 +1 = 1
+1 -1 -1 = -1
-1 +1 +1 = 1
-1 +1 -1 = -1
-1 -1 +1 = -1
-1 -1 -1 = -3

The map of counts is: {3: 1, 1: 3, -1: 3: -3: 1}.
How to build this map? Start with subproblems!
Step 1: consider only first element of the array:
    dp = {1: 1, -1: 1}
Step 2: with the second element, get all possible sums using the previous dp
    dp = {2: 1, 0: 2, -2: 1}
Step 3: repeat
    dp = {3: 1, 1: 3, -1: 3, -3: 1}

return dp[target]
'''


def target_sum(nums: list[int], target: int) -> int:
    dp: dict[int, int] = {nums[0]: 1, -nums[0]: 1}
    if nums[0] == 0:
        dp[0] = 2

    next_dp = dp

    for num in nums[1:]:
        next_dp = {}

        for s, qnt in dp.items():
            next_dp[s + num] = next_dp.get(s + num, 0) + qnt
            next_dp[s - num] = next_dp.get(s - num, 0) + qnt

        dp = next_dp

    return next_dp.get(target, 0)


if __name__ == '__main__':
    tests = [
        ([1, 1, 1, 1, 1], 3, 5),
        ([0, 0, 0, 1], 1, 8),
        ([1], 1, 1),
    ]

    for n_test, (nums, target, expected) in enumerate(tests):
        result = target_sum(nums, target)
        if result != expected:
            raise Exception(f'Test #{n_test} failed:'
                            f'result={result}, expected={expected}')

    print('Success!')
