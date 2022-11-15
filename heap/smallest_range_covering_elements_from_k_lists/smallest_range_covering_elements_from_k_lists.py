'''
https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

Idea:
Put the first element (smallest) of each list in the min_heap.
From all these elements, the first valid range is its min and max.

From that point on, do:
1. Remove the min element from the heap.
2. Add to the heap the next element of 1's list.
Now, the current range low is the current heap's min.
And the current range high is max between current high and the recently added element.

This low and high range covers elements from all k lists because:
1. The recently added element makes the range include it's list.
2. The current low would cover all k-1 lists, but now also includes the missing list because of the
element just added.
3. If high was greater then element, element in included in the range; otherwise, element is
the new high.
'''

import sys
import heapq


def _heap(array_nums: list[list[int]]) -> tuple[int, int, list[tuple[int, int, int]]]:
    min_heap = []
    high = ~sys.maxsize

    for nums_idx, nums in enumerate(array_nums):
        high = max(high, nums[0])
        min_heap.append((nums[0], nums_idx, 0))

    heapq.heapify(min_heap)
    low = min_heap[0][0]

    return low, high, min_heap


def smallest_range(array_nums: list[list[int]]) -> tuple[int, int]:
    low, high, min_heap = _heap(array_nums)
    rlow, rhigh = low, high

    while min_heap:
        _, nums_idx, num_idx = heapq.heappop(min_heap)
        nums = array_nums[nums_idx]
        if num_idx == len(nums) - 1:
            # next elements will be greater than it
            # and not include it in the range, so finish now.
            break

        heapq.heappush(min_heap, (nums[num_idx + 1], nums_idx, num_idx + 1))
        low = min_heap[0][0]
        high = max(high, nums[num_idx + 1])

        if high - low < rhigh - rlow:
            rlow, rhigh = low, high

    return rlow, rhigh


def run_tests():
    tests = [
        (
            [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]],
            (20, 24)
        ),
        (
            [[1, 2, 3], [1, 2, 3], [1, 2, 3]],
            (1, 1)
        ),
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            (3, 7)
        ),
        (
            [[1, 5, 10], [4, 5, 6], [7, 8, 9]],
            (5, 7)
        ),
    ]

    for n_test, (array_nums, expected) in enumerate(tests):
        result = smallest_range(array_nums)
        if result != expected:
            raise Exception(f'Test #{n_test} failed:\n'
                            f'result={result}\nexpect={expected}')
    print('Success!')


if __name__ == '__main__':
    run_tests()
