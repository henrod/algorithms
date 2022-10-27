INF = 10_001


def minimum_coins_for_amount(amount, coins):
    coins_for_amount = [0] + [INF] * amount

    for curr_amount in range(1, amount + 1):
        for coin in coins:
            if curr_amount - coin < 0:
                continue

            coins_for_amount[curr_amount] = min(
                coins_for_amount[curr_amount],
                coins_for_amount[curr_amount - coin] + 1
            )

    r = coins_for_amount[-1]

    return r if r < INF else -1


if __name__ == '__main__':
    n_cases = int(input())
    for case in range(n_cases):
        coins = list(map(int, input().split()))
        amount = int(input())
        expected = int(input())

        n = minimum_coins_for_amount(amount, coins)
        print(f'Case #{case}: {n}, expected: {expected}')
