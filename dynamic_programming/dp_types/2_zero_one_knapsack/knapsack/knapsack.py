'''
Given a set of items, each with a weight and a value, determine the number of each
item to include in a collection so that the total weight is less than or equal to
a given limit and the total value is as large as possible
'''
import sys


def knapsack(rocks: list[tuple[int, int]], max_weight: int) -> int:
    values = {0: 0}
    max_value = 0

    for weight, value in rocks:
        next_values = values.copy()

        for curr_value, curr_weight in values.items():
            if curr_weight + weight > max_weight:
                continue

            next_value = curr_value + value
            if next_value not in next_values:
                next_values[next_value] = sys.maxsize

            next_values[next_value] = min(next_values[next_value], curr_weight + weight)
            max_value = max(max_value, next_value)

        values = next_values

    return max_value


def run_tests():
    tests = [
        ([(1, 10), (2, 5), (5, 10), (6, 15)], 6, 20),
        ([(10, 60), (20, 100), (30, 120)], 50, 220),
    ]

    for n_test, (rocks, max_weight, expected) in enumerate(tests):
        result = knapsack(rocks, max_weight)
        if result != expected:
            raise Exception(f'Test #{n_test} failed:'
                            f'result={result}, expected={expected}')

    print('Success!')


if __name__ == '__main__':
    run_tests()
