'''
https://leetcode.com/problems/median-of-two-sorted-arrays/

Solution: https://www.youtube.com/watch?v=q6IEA26hvXc
'''


def median(nums1: list[int], nums2: list[int]) -> float:
    A, B = nums1, nums2
    total = len(A) + len(B)
    half = total // 2
    if len(A) > len(B):
        A, B = B, A

    l, r = 0, len(A) - 1

    while True:
        i = (l + r) // 2
        j = half - i - 2

        Aleft = A[i] if i >= 0 else float('-inf')
        Aright = A[i+1] if i < len(A) - 1 else float('inf')
        Bleft = B[j] if j >= 0 else float('-inf')
        Bright = B[j+1] if j < len(B) - 1 else float('inf')

        if Aleft <= Bright and Bleft <= Aright:
            if total % 2:
                return min(Aright, Bright)
            else:
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
        elif Aleft > Bright:
            r = i - 1
        else:
            l = i + 1


def run_tests() -> None:
    tests: list[tuple[list[int], list[int], float]] = [
        ([], [1, 2, 3], 2),
        ([1, 3], [2], 2),
        ([1, 2], [3, 4], 2.5),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6, 7, 8], 4),
        ([0, 0, 0], [1, 2, 3], 0.5),
        ([0], [1, 2, 3, 4, 5], 2.5),
        ([0, 0], [0, 0], 0),
    ]

    for n_test, (nums1, nums2, expected) in enumerate(tests):
        result = median(nums1, nums2)
        if result != expected:
            raise Exception(f'Test #{n_test} failed: result={result}, expected={expected}')

    print('Success!')


if __name__ == '__main__':
    run_tests()
