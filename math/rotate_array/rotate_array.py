'''
Given an array, rotate the array to the right by k steps, where k is
non-negative.

Idea: reverse first n-k elements, reverse last k elements, then reverse the 
whole array.  By reversing twice, you "desreverse" the two parts while putting
the second half elements in the first half.
Time: O(N)
Space: O(1), inplace.
'''


def rotate(nums: list[int], k: int) -> None:
    n = len(nums)
    k %= n

    def reverse(l: int, r: int) -> None:
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    reverse(0, n - k - 1)
    reverse(n - k, n - 1)
    reverse(0, n - 1)


def run_tests():
    tests = [
        ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
        ([1, 2, 3, 4, 5, 6, 7], 5, [3, 4, 5, 6, 7, 1, 2]),
        ([1, 2, 3, 4, 5, 6, 7], 10, [5, 6, 7, 1, 2, 3, 4]),
        ([1, 2, 3, 4, 5, 6, 7], 0, [1, 2, 3, 4, 5, 6, 7]),
    ]

    for n_test, (nums, k, expected) in enumerate(tests):
        rotate(nums, k)
        if nums != expected:
            raise Exception(f'Test #{n_test} failed:'
                            f'result={nums}, expected={expected}')
    print('Success!')


if __name__ == '__main__':
    run_tests()
