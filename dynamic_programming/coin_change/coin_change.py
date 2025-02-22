import sys


def minimum_coins_for_amount(amount, coins):
    min_coins_by_amount = [sys.maxsize] * (amount + 1)
    min_coins_by_amount[0] = 0

    for sub_amount in range(1, amount + 1):
        for coin in coins:
            if coin <= sub_amount:
                min_coins_by_amount[sub_amount] = min(
                    min_coins_by_amount[sub_amount],
                    min_coins_by_amount[sub_amount - coin] + 1,
                )

    return (
        min_coins_by_amount[amount] if min_coins_by_amount[amount] < sys.maxsize else -1
    )


if __name__ == "__main__":
    n_cases = int(input())
    for case in range(n_cases):
        coins = list(map(int, input().split()))
        amount = int(input())
        expected = int(input())

        n = minimum_coins_for_amount(amount, coins)
        if n != expected:
            raise Exception(f"Case #{case}: actual={n}, expected={expected}")

    print("Success!")
