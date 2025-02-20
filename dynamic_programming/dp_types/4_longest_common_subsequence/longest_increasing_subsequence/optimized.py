"""
https://leetcode.com/problems/longest-increasing-subsequence/
"""


def longest_increasing_subsequence(nums: list[int]) -> int:
    lis = []

    for num in nums:
        i = _lower_bound_bin_search(lis, num)
        if i == len(lis):
            lis.append(num)
        else:
            lis[i] = num

    return len(lis)


def _lower_bound_bin_search(arr: list[int], value: int) -> int:
    l, r = 0, len(arr) - 1

    while l <= r:
        m = (l + r) // 2

        if arr[m] == value:
            return m

        if arr[m] < value:
            l = m + 1
        else:
            r = m - 1

    return l


if __name__ == "__main__":
    tests = [
        ([1, 2, 4, 3], 3),
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([0, 1, 0, 3, 2, 3], 4),
        ([7, 7, 7, 7], 1),
    ]

    for n_test, (nums, expected) in enumerate(tests):
        result = longest_increasing_subsequence(nums)
        if result != expected:
            raise Exception(
                f"Test #{n_test} failed:" f"result={result}, expected={expected}"
            )

    print("Success!")
