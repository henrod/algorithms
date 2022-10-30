def _override(nums: list[int], num: int) -> None:
    l, r = 0, len(nums) - 1

    while l <= r:
        m = (l + r) // 2

        if nums[m] == num:
            return
        elif nums[m] < num:
            l = m + 1
        elif nums[m] > num:
            r = m - 1

    nums[l] = num


def longest_increasing_subsequence(nums: list[int]) -> int:
    dp: list[int] = []

    for num in nums:
        if not dp or dp[-1] < num:
            dp.append(num)
        else:
            _override(dp, num)

    return len(dp)


def run_tests() -> None:
    tests = [
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([0, 1, 0, 3, 2, 3], 4),
        ([7, 7, 7, 7, 7, 7, 7], 1),
        ([1, 3, 6, 7, 9, 4, 10, 5, 6], 6),
        ([2, 6, 8, 3, 4, 5, 1], 4)
    ]

    for n_test, (nums, expected) in enumerate(tests):
        result = longest_increasing_subsequence(nums)
        if result != expected:
            raise BaseException(f'Test #{n_test} failed: '
                                f'result={result}, expected={expected}')

    print('Success!')


if __name__ == '__main__':
    run_tests()
