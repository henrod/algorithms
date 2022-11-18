import random


def radixsort(nums: list[int]) -> list[int]:
    div, rem = 1, 10
    max_num = max(nums)

    while div <= max_num:
        buckets: list[list[int]] = [[] for _ in range(10)]
        for num in nums:
            idx = num % rem // div
            buckets[idx].append(num)

        nums = []
        for bucket in buckets:
            nums.extend(bucket)

        div *= 10
        rem *= 10

    return nums


def run_tests() -> None:
    random_arr = [random.randint(0, 1_000_000) for _ in range(100_000)]

    tests = [
        ([10, 1, 100, 10], [1, 10, 10, 100]),
        ([4, 3, 2, 1], [1, 2, 3, 4]),
        ([10, 2, 1003, 99], [2, 10, 99, 1003]),
        ([560, 409, 422], [409, 422, 560]),
        (random_arr, sorted(random_arr)),
    ]

    for n_test, (nums, expected) in enumerate(tests):
        result = radixsort(nums)
        if result != expected:
            raise Exception(f'Test #{n_test} failed:'
                            f'result={result}, expected={expected}')

    print('Success!')


if __name__ == '__main__':
    run_tests()
