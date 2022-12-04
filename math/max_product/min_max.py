import sys


def max_product(nums: list[int]) -> int:
    min_prod = 1
    max_prod = 1
    r = ~sys.maxsize

    for num in nums:
        if num == 0:
            min_prod = 1
            max_prod = 1
            r = max(r, 0)
        else:
            new_min = min(num, min_prod * num, max_prod * num)
            new_max = max(num, min_prod * num, max_prod * num)
            min_prod = new_min
            max_prod = new_max
            r = max(r, max_prod)

    return r


def run_tests():
    tests = [
        ([2, -5, -2, -4, 3], 24),
        ([-2], -2),
        ([2, 3, -2, 4], 6),
        ([-2, 0, -1], 0),
        ([-2, 0, -1, 0], 0),
        ([2, 3, -2, 4, -3, -1], 144),
        ([-3, -1], 3),
    ]

    for n_test, (nums, expected) in enumerate(tests):
        result = max_product(nums)
        if result != expected:
            raise Exception(f'Test #{n_test} failed: result={result}, expected={expected}')

    print('Success!')


if __name__ == '__main__':
    run_tests()
