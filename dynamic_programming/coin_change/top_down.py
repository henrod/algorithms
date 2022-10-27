INF = 10_001


def _minimum_coins_for_amount(
    amount: int,
    coins: list[int],
    coins_for_amount: dict[int, int],
) -> int:
    if amount == 0:
        return 0

    if amount < 0:
        return INF

    if amount in coins_for_amount:
        return coins_for_amount[amount]

    coins_for_amount[amount] = min(
        _minimum_coins_for_amount(amount - coin, coins, coins_for_amount) + 1
        for coin in coins
    )

    return coins_for_amount[amount]


def minimum_coins_for_amount(amount: int, coins: list[int]) -> int:
    r = _minimum_coins_for_amount(amount, coins, {})
    return -1 if r >= INF else r


if __name__ == '__main__':
    n_cases = int(input())
    for case in range(n_cases):
        coins = list(map(int, input().split()))
        amount = int(input())
        expected = int(input())

        n = minimum_coins_for_amount(amount, coins)
        print(f'Case #{case}: {n}, expected: {expected}')
