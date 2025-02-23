"""
https://leetcode.com/problems/word-break/

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into
a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
"""


class _TrieNode:
    def __init__(self):
        self.next: dict[str, _TrieNode] = {}
        self.end: bool = False


def _add_word(root: _TrieNode, word: str):
    node = root

    for letter in word:
        if letter not in node.next:
            node.next[letter] = _TrieNode()

        node = node.next[letter]

    node.end = True


def _dfs(word: str, start: int, root: _TrieNode, failed_starts: set[int]) -> bool:
    if start in failed_starts:
        return False

    node: _TrieNode = root

    for i in range(start, len(word)):
        letter: str = word[i]

        if letter not in node.next:
            return False

        node = node.next[letter]
        if node.end:
            if _dfs(word, i + 1, root, failed_starts):
                return True

            failed_starts.add(i + 1)

    return node.end


def word_break(text: str, words_dictionary: list[str]) -> bool:
    root = _TrieNode()
    for word in words_dictionary:
        _add_word(root, word)

    return _dfs(text, 0, root, set())


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
