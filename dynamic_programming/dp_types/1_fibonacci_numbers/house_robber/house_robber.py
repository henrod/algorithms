'''
Given a list of houses, where the values are the money in each house.
What is the maximum rob you can make?
You can't rob consecutive houses.

https://leetcode.com/problems/house-robber/
'''


# [rob1, rob2, num, next_num, ...]
def rob(nums: list[int]) -> int:
    rob1, rob2 = 0, 0
    for num in nums:
        rob1, rob2 = rob2, max(rob1 + num, rob2)
    return rob2


if __name__ == '__main__':
    tests = [
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
    ]

    for n_test, (houses, expected) in enumerate(tests):
        result = rob(houses)
        if result != expected:
            raise Exception(f'Test #{n_test} failed:'
                            f'result={result}, expected={expected}')

    print('Success!')
