def _find(intervals, num):
    l, r = 0, len(intervals) - 1
    while l <= r:
        m = (l + r) // 2
        if intervals[m] == num:
            return m

        if intervals[m] < num:
            l = m + 1
        else:
            r = m - 1

    return l


def _max_range(intervals: list[int]) -> int:
    max_range = 0
    for i in range(0, len(intervals), 2):
        rang = intervals[i + 1] - intervals[i] + 1
        max_range = max(max_range, rang)

    return max_range


def longest_consecutive_sequence(nums: list[int]) -> int:
    intervals: list[int] = []
    for num in nums:
        i = _find(intervals, num)
        if i % 2 == 1:
            continue

        if i < len(intervals) and intervals[i] == num:
            continue

        l, r = i, i
        sub = [num, num]
        if l > 0 and intervals[l - 1] == num - 1:
            sub[0] = intervals[l - 2]
            l -= 2

        if r < len(intervals) and intervals[r] == num + 1:
            sub[1] = intervals[r + 1]
            r += 2

        intervals[l:r] = sub

    return _max_range(intervals)


def run_tests():
    tests = [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([], 0),
        ([1, 3, 5, 7], 1),
        ([1, 3, 5, 7, 2, 6], 3),
        ([1, 3, 5, 7, 2, 6, 4], 7),
        ([1, 3, 5, 7, 2, 6, 4, 3, 5], 7),
        ([1, 1, 1, 1], 1),
        ([0, 0, 1, -1], 3),
        ([2, -1, 0, 1], 4),
    ]

    for n_test, (nums, expected) in enumerate(tests):
        result = longest_consecutive_sequence(nums)
        if result != expected:
            raise Exception(f'Test #{n_test} failed:'
                            f'result={result}, expected={expected}')

    print('Success!')


if __name__ == '__main__':
    run_tests()
