'''
https://leetcode.com/problems/non-overlapping-intervals/

Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum
number of intervals you need to remove to make the rest of the intervals non-overlapping.

Idea: Sort intervals ascending by end. For each interval, choose the smaller end that
doesn't overlap.
Why is it greedy? If you have a current end x and find an end y where y > x, [y:] can't
possibly hold more intervals than [x:].
'''

import sys


def min_intervals_to_remove(intervals: list[list[int]]) -> int:
    intervals.sort(key=lambda int: int[1])
    curr_end, size = ~sys.maxsize, 0

    for start, end in intervals:
        if start >= curr_end:
            curr_end = end
            size += 1

    return len(intervals) - size


def run_tests() -> None:
    tests = [
        ([[1, 2], [1, 3], [2, 3], [3, 4]], 1),
        ([[1, 100], [11, 22], [1, 11], [2, 12]], 2),
        ([[1, 2], [1, 2], [1, 2]], 2),
        ([[1, 2], [2, 3]], 0),
    ]

    for n_test, (intervals, expected) in enumerate(tests):
        result = min_intervals_to_remove(intervals)
        if result != expected:
            raise Exception(f'Test #{n_test} failed:'
                            f'\nresult={result}\nexpected={expected}')

    print('Success!')


if __name__ == '__main__':
    run_tests()
