"""
Given an array of integers, find any local minimum.

Local minimum if a value in the array less than its left and right neighbors.
The first and last indices consider their only neighbor.

Examples:
1. [5, 9, 7, 10, 12] -> 5 or 7
2. [1, 1, 1] -> None
3. [2, 1, 2] -> 1
"""


def local_min(nums, l, r):
    if not nums:
        return None

    if len(nums) == 1:
        return nums[0]

    if l > r:
        return None

    while l <= r:
        m = (l + r) // 2

        if m == 0:
            return nums[0] if nums[0] < nums[1] else None

        if m == len(nums) - 1:
            return nums[-1] if nums[-2] > nums[-1] else None

        if nums[m - 1] > nums[m] < nums[m + 1]:
            return nums[m]

        if nums[m - 1] < nums[m]:
            r = m - 1
        elif nums[m] > nums[m + 1]:
            l = m + 1
        else:
            return local_min(nums, l, m - 1) or local_min(nums, m + 1, r)

    return None


def run_tests() -> None:
    tests = [
        ([5, 9, 7, 10, 12], {5, 7}),
        ([1, 2, 2, 2, 3], {1}),
        ([3, 2, 2, 2, 1], {1}),
        ([10], {10}),
        ([], {None}),
        ([1, 1, 1, 1], {None}),
    ]

    for n_test, (nums, expected) in enumerate(tests):
        result = local_min(nums, 0, len(nums) - 1)
        if result not in expected:
            raise Exception(
                f"Test #{n_test} failed: result={result}, expected={expected}"
            )

    print("Success!")


if __name__ == "__main__":
    run_tests()
