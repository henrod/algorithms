"""
Given an array of intervals, return an array of arrays of non-overlapping intervals.

Example:
* input: [0, 10], [5, 15], [20, 30]
* output: [[0, 10], [20, 30]], [[5, 15]]
"""

import heapq


def merge(intervals):
    intervals.sort()
    min_heap = []

    for start, end in intervals:
        if min_heap and min_heap[0][0] < start:
            _, merged_intervals = heapq.heappop(min_heap)
            merged_intervals.append((start, end))
        else:
            merged_intervals = [(start, end)]

        heapq.heappush(min_heap, (end, merged_intervals))

    return [merged_intervals for _, merged_intervals in min_heap]


def are_equal(actual, expected):
    if len(actual) != len(expected):
        return False

    actual.sort(key=lambda arr: arr[0][0])

    for i in range(len(actual)):
        if len(actual[i]) != len(expected[i]):
            return False

        for j in range(len(actual[i])):
            if actual[i][j] != expected[i][j]:
                return False

    return True


if __name__ == "__main__":
    tests = [
        ([(0, 10), (5, 15), (20, 30)], [[(0, 10), (20, 30)], [(5, 15)]]),
        ([(0, 10), (20, 30), (40, 50)], [[(0, 10), (20, 30), (40, 50)]]),
        ([(0, 10), (5, 15), (8, 12)], [[(0, 10)], [(5, 15)], [(8, 12)]]),
    ]

    for n_test, (input, expected) in enumerate(tests):
        actual = merge(input)

        if not are_equal(actual, expected):
            raise Exception(
                f"Test #{n_test} failed:" f"actual={actual}, expected={expected}"
            )

    print("Success!")
