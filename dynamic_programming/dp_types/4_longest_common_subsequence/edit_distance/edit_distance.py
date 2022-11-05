'''
https://leetcode.com/problems/edit-distance/

Given two strings word1 and word2, return the minimum number of 
operations required to convert word1 to word2.

You have the following three operations permitted on a word:
- Insert a character
- Delete a character
- Replace a character

Solution: https://www.youtube.com/watch?v=XYi2-LPrwm4

Idea: similar to longest_common_subsequence.
- abc
- adc

1. word1[i] == word2[j] --> advance both pointers and don't count an operation
2. word1[i] != word2[j] --> one operation will be done, so incremented:
    i. Insert a char: insert in word1 the char of word2, advance only i pointer
    ii. Delete a char: delete char in word1, advance only j pointer
    iii. Replace a char: force char in word1 be equal to in word2, avance both pointers

Base cases: 
- when word1 is empty, len(word1) operations are required, which are len(word1) deletes.
- when word2 is empty, len(word2) operations are required, which are len(word2) inserts.
'''


def edit_distance(word1: str, word2: str) -> int:
    dp: list[list[int]] = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
    for i, row in enumerate(dp):
        row[-1] = len(word1) - i
    for j, col in enumerate(dp[-1]):
        dp[-1][col] = len(word2) - j

    for i in range(len(word1) - 1, -1, -1):
        for j in range(len(word2) - 1, -1, -1):
            if word1[i] == word2[j]:
                dp[i][j] = dp[i+1][j+1]
            else:
                dp[i][j] = min(
                    dp[i+1][j],
                    dp[i][j+1],
                    dp[i+1][j+1],
                ) + 1

    return dp[0][0]


if __name__ == '__main__':
    tests = [
        ('horse', 'ros', 3),
        ('intention', 'execution', 5),
    ]

    for n_test, (word1, word2, expected) in enumerate(tests):
        result = edit_distance(word1, word2)
        if result != expected:
            raise Exception(f'Test #{n_test} failed:'
                            f'result={result}, expected={expected}')

    print('Success!')
