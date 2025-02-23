"""
https://leetcode.com/problems/word-break/

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into
a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
"""

"""
Analysis.

N: len(text)
M: len(word_dictionary)
K: avg(len(word) for word in word_dictionary)

Time: O(N * M * K)
Space: O(N + M * K)
"""


def word_break(text: str, word_dictionary: list[str]) -> bool:
    dp = [False] * (len(text) + 1)  # sub problem: can word break starting from index i
    dp[len(text)] = True  # base: index after end of text (empty text) can be word break

    for i in range(len(text) - 1, -1, -1):  # bottom up, so move backwards
        for word in word_dictionary:
            if i + len(word) <= len(text) and text[i : i + len(word)] == word:
                dp[i] = dp[i + len(word)]

            if dp[i]:
                break

    return dp[0]


def run_tests() -> None:
    tests = [
        ("leetcode", ["leet", "code"], True),
        ("applepenapple", ["apple", "pen"], True),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
        (
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
            [
                "a",
                "aa",
                "aaa",
                "aaaa",
                "aaaaa",
                "aaaaaa",
                "aaaaaaa",
                "aaaaaaaa",
                "aaaaaaaaa",
                "aaaaaaaaaa",
            ],
            False,
        ),
        (
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            [
                "aa",
                "aaa",
                "aaaa",
                "aaaaa",
                "aaaaaa",
                "aaaaaaa",
                "aaaaaaaa",
                "aaaaaaaaa",
                "aaaaaaaaaa",
                "ba",
            ],
            False,
        ),
        ("aaaaaaa", ["aaaa", "aaa"], True),
        ("catsandogcat", ["cats", "dog", "sand", "and", "cat", "an"], True),
    ]

    for n_test, (text, words_dictionary, expected) in enumerate(tests):
        result = word_break(text, words_dictionary)
        if result != expected:
            raise Exception(
                f"Test #{n_test} failed:" f"result={result}, expected={expected}"
            )

    print("Success!")


if __name__ == "__main__":
    run_tests()
