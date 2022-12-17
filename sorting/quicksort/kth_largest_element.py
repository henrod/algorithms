'''
https://leetcode.com/problems/kth-largest-element-in-an-array/
'''


def _swap(nums: list[int], i: int, j: int) -> None:
    nums[i], nums[j] = nums[j], nums[i]


def _partition(nums: list[int], start: int, end: int) -> int:
    pivot = nums[end]
    i = start - 1
    for j in range(start, end):
        if nums[j] <= pivot:
            i += 1
            _swap(nums, i, j)

    _swap(nums, i + 1, end)

    return i + 1


def kth_largest_element(nums: list[int], k: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        p = _partition(nums, l, r)
        if p == len(nums) - k:
            return nums[p]

        if p < len(nums) - k:
            l = p + 1
        else:
            r = p - 1

    return -1


def run_tests():
    tests = [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
    ]

    for n_test, (nums, k, expected) in enumerate(tests):
        result = kth_largest_element(nums, k)
        if result != expected:
            raise Exception(f'Test #{n_test} failed: ',
                            f'result={result}, expected={expected}')

    print('Success!')


if __name__ == '__main__':
    run_tests()
