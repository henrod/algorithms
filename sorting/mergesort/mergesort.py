def _mergesort(nums: list[int], start: int, end: int, aux: list[int]) -> None:
    if start >= end:
        return

    m = (start + end) // 2
    _mergesort(nums, start, m, aux)
    _mergesort(nums, m + 1, end, aux)

    i, j = start, m + 1
    for k in range(start, end + 1):
        if i > m:
            aux[k] = nums[j]
            j += 1
        elif j > end:
            aux[k] = nums[i]
            i += 1
        elif nums[i] <= nums[j]:
            aux[k] = nums[i]
            i += 1
        else:
            aux[k] = nums[j]
            j += 1

    for k in range(start, end + 1):
        nums[k] = aux[k]


def mergesort(nums: list[int]) -> None:
    _mergesort(nums, 0, len(nums) - 1, nums.copy())


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
        mergesort(nums)
        if nums != expected:
            raise Exception(f'Test #{n_test} failed: ',
                            f'result={nums}, expected={expected}')

    print('Success!')


if __name__ == '__main__':
    run_tests()
