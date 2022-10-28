'''
Return the continuous subarray with maximum sum.
'''

import sys


def max_sum(nums: list[int]) -> int:
    local_max = ~sys.maxsize
    global_max = ~sys.maxsize

    for num in nums:
        local_max = max(local_max + num, num)
        global_max = max(global_max, local_max)

    return global_max


if __name__ == '__main__':
    n_cases = int(input())

    for case in range(n_cases):
        nums = list(map(int, input().split()))
        expected = input()
        result = max_sum(nums)
        print(f'Case #{case}: result={result}, expected={expected}')
