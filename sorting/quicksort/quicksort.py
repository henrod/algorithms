def _quicksort(nums: list[int], start: int, end: int) -> None:
    if start >= end:
        return

    pivot = nums[start]
    left = start + 1
    right = end

    def swap(i: int, j: int):
        nums[i], nums[j] = nums[j], nums[i]

    while left < right:
        while left < right and nums[left] <= pivot:
            left += 1

        while right > left and nums[right] > pivot:
            right -= 1

        swap(left, right)

    if nums[left] > pivot:
        left -= 1

    swap(left, start)
    _quicksort(nums, start, left - 1)
    _quicksort(nums, left + 1, end)


def quicksort(nums: list[int]) -> None:
    _quicksort(nums, 0, len(nums) - 1)


def run_tests():
    tests = [
        ([2, 1, 3], [1, 2, 3]),
        ([2, 1, 3, 3, 1], [1, 1, 2, 3, 3]),
        ([2, 2, 2, 2], [2, 2, 2, 2]),
        ([1, 2, 3, 4], [1, 2, 3, 4]),
        ([4, 3, 2, 1], [1, 2, 3, 4]),
        ([1, 3, 2], [1, 2, 3]),
        ([3, 2], [2, 3])
    ]

    for n_test, (nums, expected) in enumerate(tests):
        quicksort(nums)
        if nums != expected:
            raise Exception(f'Test #{n_test} failed: ',
                            f'result={nums}, expected={expected}')

    print('Success!')


if __name__ == '__main__':
    run_tests()
