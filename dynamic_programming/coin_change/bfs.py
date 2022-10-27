from collections import deque


def minimum_coins_for_amount(amount, coins):
    queue = deque([(0, 0)])
    visited = {0}

    while queue:
        curr_amount, n_coins = queue.popleft()
        if curr_amount == amount:
            return n_coins

        for coin in coins:
            next_amount = curr_amount + coin
            if next_amount in visited or next_amount > amount:
                continue

            visited.add(next_amount)
            queue.append((next_amount, n_coins + 1))

    return -1


if __name__ == '__main__':
    n_cases = int(input())
    for case in range(n_cases):
        coins = list(map(int, input().split()))
        amount = int(input())
        expected = int(input())

        n = minimum_coins_for_amount(amount, coins)
        print(f'Case #{case}: {n}, expected: {expected}')
