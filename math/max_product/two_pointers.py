'''
Return the continous subarray with maximum product.
Solution based on: https://leetcode.com/problems/maximum-product-subarray/discuss/1608800/C%2B%2B-or-Discussion-in-detail-or-Easy-to-understand
'''

import sys


def max_product(nums: list[int]) -> int:
    l_prod = 1
    r_prod = 1
    n = len(nums)
    max_prod = ~sys.maxsize

    for i in range(n):
        l_prod *= nums[i]
        r_prod *= nums[n - i - 1]
        max_prod = max(l_prod, r_prod, max_prod)
        l_prod = l_prod if l_prod != 0 else 1
        r_prod = r_prod if r_prod != 0 else 1

    return max_prod


if __name__ == '__main__':
    n_cases = int(input())
    for case in range(n_cases):
        nums = list(map(int, input().split()))
        expected = input()
        result = max_product(nums)
        print(f'Case #{case}: result={result}, expected={expected}')
