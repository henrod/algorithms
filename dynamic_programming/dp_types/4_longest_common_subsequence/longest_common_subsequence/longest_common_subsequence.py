'''
https://leetcode.com/problems/longest-common-subsequence/

Solution: https://youtu.be/Ua0GhsJSlWM
'''


def longest_common_subsequence_optimized(text1: str, text2: str) -> int:
    dp: list[int] = [0 for _ in range(len(text2) + 1)]

    for i in range(len(text1) - 1, -1, -1):
        prev = 0
        for j in range(len(text2) - 1, -1, -1):
            if text1[i] == text2[j]:
                prev, dp[j] = dp[j], prev + 1
            else:
                prev, dp[j] = dp[j], max(dp[j], dp[j + 1])

    return dp[0]


def longest_common_subsequence(text1: str, text2: str) -> int:
    dp: list[list[int]] = [
        [0 for _ in range(len(text2) + 1)]
        for _ in range(len(text1) + 1)
    ]

    for i in range(len(text1) - 1, -1, -1):
        for j in range(len(text2) - 1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = dp[i+1][j+1] + 1
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j + 1])

    return dp[0][0]


if __name__ == '__main__':
    tests = [
        ('abcde', 'ace', 3),
        ('abc', 'abc', 3),
        ('abc', 'def', 0),
        ('abcba', 'abcbcba', 5),
    ]

    for n_test, (text1, text2, expected) in enumerate(tests):
        result = longest_common_subsequence(text1, text2)
        if result != expected:
            raise Exception(f'Test #{n_test} failed:'
                            f'result={result}, expected={expected}')

    print('Success!')
