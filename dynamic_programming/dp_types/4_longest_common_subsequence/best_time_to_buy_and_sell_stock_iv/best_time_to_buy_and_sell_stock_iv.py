'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/

You are given an integer array prices where prices[i] is the price of a given
stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions.

Note: You may not engage in multiple transactions simultaneously
(i.e., you must sell the stock before you buy again).
'''


'''
The idea is to memoize in the dimensions prices index and number of transactions:
    dp[i][j] -> max profit with at most i transactions until prices[j].
    0 <= i <= k and 0 <= j < len(prices).

At every j, there are two options:
    1. Do nothing or buy, meaning dp[i][j] = dp[i][j - 1]
    2. Max profit until any day t < j plus the profit of buying at t and selling at j.
       Mathematically:
        dp[i][j] = t:1->j-1 max(dp[i - 1][t] + prices[j] - prices[t])

This runs in O(kn^2).

The option 2 can be rewritten, though:
    t:1->j-1 max(dp[i - 1][t] + prices[j] - prices[t]) =
    prices[j] + t:1->j-1 max(dp[i - 1][t] - prices[t])
Where the second part we keep in a variable maxIncompleteProfit.
Incomplete because the stock was bought at t, thus `-prices[t]`, but not sold yet.

Making the run equal to O(kn).
'''


def max_profit_v1(prices: list[int], k: int) -> int:
    dp: list[list[int]] = [
        [0 for _ in range(len(prices))]
        for _ in range(k + 1)
    ]

    for i in range(1, k + 1):
        maxIncompleteProfit = -prices[0]
        for j in range(1, len(prices)):
            dp[i][j] = max(dp[i][j - 1], prices[j] + maxIncompleteProfit)
            maxIncompleteProfit = max(maxIncompleteProfit, dp[i - 1][j] - prices[j])

    return dp[k][len(prices) - 1]


def run_tests() -> None:
    class Test:
        def __init__(self, prices: list[int], k: int, expected: int):
            self.prices = prices
            self.k = k
            self.expected = expected

    for i, test in enumerate([
        Test(
            prices=[2, 4, 1],
            k=2,
            expected=2,
        ),
        Test(
            prices=[3, 2, 6, 5, 0, 3],
            k=2,
            expected=7,
        ),
        Test(
            prices=[1, 2, 4, 2, 5, 7, 2, 4, 9, 0],
            k=2,
            expected=13,
        )
    ]):
        result = max_profit(test.prices, test.k)
        if result != test.expected:
            raise Exception(f'Test #{i} failed: got={result}, want={test.expected}')

    print("Success!")


if __name__ == '__main__':
    run_tests()
