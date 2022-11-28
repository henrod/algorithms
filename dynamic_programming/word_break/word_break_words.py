'''
https://leetcode.com/problems/word-break/

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into
a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
'''


def word_break(text: str, words_dictionary: list[str]) -> list[str]:
    words = set(words_dictionary)
    dp: list[list[list[str]]] = [[] for _ in range(len(text) + 1)]
    dp[-1].append([])

    for i in range(len(text) - 1, -1, -1):
        for j in range(i + 1, len(text) + 1):
            word = text[i:j]
            if word in words:
                dp[i].extend([word] + next_words for next_words in dp[j])

    return [' '.join(words) for words in dp[0]]


def run_tests() -> None:
    tests = [
        (
            'catsanddog',
            ['cat', 'cats', 'and', 'sand', 'dog'],
            ['cat sand dog', 'cats and dog'],
        ),
        (
            'pineapplepenapple',
            ['apple', 'pen', 'applepen', 'pine', 'pineapple'],
            ['pine apple pen apple', 'pine applepen apple', 'pineapple pen apple']
        ),
        (
            'catsandog',
            ['cats', 'dog', 'sand', 'and', 'cat'],
            [],
        ),
    ]

    for n_test, (text, words_dictionary, expected) in enumerate(tests):
        result = word_break(text, words_dictionary)
        result.sort()
        if result != expected:
            raise Exception(f'Test #{n_test} failed:'
                            f'result={result}, expected={expected}')

    print('Success!')


if __name__ == '__main__':
    run_tests()
