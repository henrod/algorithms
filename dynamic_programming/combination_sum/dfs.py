def _combinations_sum(numbers, target, combination, r):
    if target < 0:
        return

    if target == 0:
        r.append(combination)
        return

    for i in range(len(numbers)):
        _combinations_sum(
            numbers[i:], target - numbers[i],
            combination + [numbers[i]], r,
        )


def combinations_sum(numbers, target):
    r = []
    _combinations_sum(numbers, target, [], r)
    return r


if __name__ == '__main__':
    n_cases = int(input())
    for case in range(n_cases):
        numbers = list(map(int, input().split()))
        target = int(input())
        expected = input()

        combinations = combinations_sum(numbers, target)
        print(f'Case #{case}: {combinations}, expected: {expected}')
