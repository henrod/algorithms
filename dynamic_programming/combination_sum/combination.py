def combinations_sum(numbers, target):
    combinations_by_target = [[] for _ in range(target + 1)]

    for number in numbers:
        for curr_target in range(number, target + 1):
            if curr_target == number:
                combinations_by_target[curr_target].append([number])

            for combination in combinations_by_target[curr_target - number]:
                combinations_by_target[curr_target].append(
                    combination + [number])

    return combinations_by_target[-1]


if __name__ == '__main__':
    n_cases = int(input())
    for case in range(n_cases):
        numbers = list(map(int, input().split()))
        target = int(input())
        expected = input()

        combinations = combinations_sum(numbers, target)
        print(f'Case #{case}: {combinations}, expected: {expected}')
