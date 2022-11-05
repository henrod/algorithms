'''
https://leetcode.com/problems/longest-common-subsequence/
'''


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
                dp[i][j] = max(dp[i+1][j], dp[i][j+1])

    return dp[0][0]


if __name__ == '__main__':
    tests = [
        ('abcde', 'ace', 3),
        ('abc', 'abc', 3),
        ('abc', 'def', 0),
    ]

    for n_test, (text1, text2, expected) in enumerate(tests):
        result = longest_common_subsequence(text1, text2)
        if result != expected:
            raise Exception(f'Test #{n_test} failed:'
                            f'result={result}, expected={expected}')

    print('Success!')
