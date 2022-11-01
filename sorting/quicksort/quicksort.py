'''
Idea: always keep the following invariant:
[    <= pivot    ][    > pivot    ][ ]
                i                j  p
- pivot is at the last index
- everything before i (inclusive) is less or equal than pivot
    - that's why i starts at `start - 1`
- everything before j (inclusive) and after i, is greater than pivot
'''


def _pivot(nums: list[int], start: int, end: int) -> int:
    def swap(i: int, j: int) -> None:
        nums[i], nums[j] = nums[j], nums[i]

    pivot = nums[end]

    i = start - 1
    for j in range(start, end):
        if nums[j] <= pivot:
            i += 1
            swap(i, j)

    swap(i + 1, end)

    return i + 1


def _quicksort(nums: list[int], start: int, end: int) -> None:
    if start >= end:
        return

    pivot = _pivot(nums, start, end)
    _quicksort(nums, start, pivot - 1)
    _quicksort(nums, pivot + 1, end)


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
