"""
Given an array of non-negative integers and a target sum, return the
start and end index of a subarray whose sum is equal to target sum.
Return empty if no solution exists.
"""

from collections.abc import Callable


def get_subarray(nums: list[int], target: int) -> int:
    sums: dict[int, int] = {0: -1}
    curr: int = 0

    for i, num in enumerate(nums):
        curr += num

        if curr - target in sums:
            return [sums[curr - target] + 1, i]

        sums[curr] = i

    return []


class Test:
    def __init__(self, nums: list[int], target: int, expected: list[int]):
        self.nums = nums
        self.target = target
        self.expected = expected

    def run(self, id: int, get_subarray: Callable[[list[int], int], int]) -> None:
        actual = get_subarray(self.nums, self.target)
        if actual != self.expected:
            raise Exception(
                f"Test #{id}: actual = {actual}, expected = {self.expected}"
            )


def run_tests():
    tests: list[Test] = [
        Test(
            nums=[1, 2, 3],
            target=5,
            expected=[1, 2],
        ),
        Test(
            nums=[0],
            target=0,
            expected=[0, 0],
        ),
        Test(
            nums=[],
            target=0,
            expected=[],
        ),
        Test(
            nums=[1, 2, 3],
            target=10,
            expected=[],
        ),
        Test(
            nums=[1, 0, 3],
            target=4,
            expected=[0, 2],
        ),
    ]

    for id, test in enumerate(tests):
        test.run(id, get_subarray)

    print("Success!")


if __name__ == "__main__":
    run_tests()
