'''
Given a list of coins, return the minimum amount of coins to sum target.
The quantity of each coin is infinite.

https://leetcode.com/problems/coin-change/
'''

import sys


def coin_change(coins: list[int], target: int) -> int:
    # sub_target -> quantity
    inf = sys.maxsize
    dp = [0] + [inf] * target

    for sub_target in range(1, target + 1):
        for coin in coins:
            if sub_target - coin >= 0:
                dp[sub_target] = min(dp[sub_target - coin] + 1, dp[sub_target])

    return dp[target] if dp[target] < inf else -1


if __name__ == '__main__':
    tests = [
        ([1, 2, 5], 11, 3),
        ([2, 4, 6], 7, -1),
    ]

    for n_test, (coins, target, expected) in enumerate(tests):
        result = coin_change(coins, target)
        if result != expected:
            raise Exception(f'Test #{n_test} failed:'
                            f'result={result}, expected={expected}')

    print('Success!')
