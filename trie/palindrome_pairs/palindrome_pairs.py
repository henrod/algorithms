'''
https://leetcode.com/problems/palindrome-pairs/
'''


class Trie:
    class Node:
        def __init__(self) -> None:
            self.children: dict[str, Trie.Node] = {}
            self.word: str | None = None
            self.index: int | None = None

    def __init__(self) -> None:
        self.root = self.Node()

    def add(self, word: str, index: int) -> None:
        node = self.root

        for letter in word:
            if letter not in node.children:
                node.children[letter] = self.Node()
            node = node.children[letter]

        node.word = word
        node.index = index

    def prefix_words(self, prefix: str) -> list[tuple[int, str]]:
        words: list[tuple[int, str]] = []
        node = self.root

        for letter in prefix:
            if node.word is not None and node.index is not None:
                words.append((node.index, node.word))

            if letter not in node.children:
                return words

            node = node.children[letter]

        self._prefix_words(node, words)

        return words

    def _prefix_words(self, node: Node, words: list[tuple[int, str]]) -> None:
        if node.word is not None and node.index is not None:
            words.append((node.index, node.word))

        for next_node in node.children.values():
            self._prefix_words(next_node, words)


def _is_palindrome(word: str, start: int) -> bool:
    end = len(word) - 1

    while start < end:
        if word[start] != word[end]:
            return False

        start += 1
        end -= 1

    return True


def palindrome_pairs(words: list[str]) -> list[tuple[int, int]]:
    trie = Trie()
    for i, word in enumerate(words):
        trie.add(word[::-1], i)

    pairs: list[tuple[int, int]] = []

    for i, word in enumerate(words):
        candidates = trie.prefix_words(word)
        for j, candidate in candidates:
            if i == j:
                continue
            elif len(word) == len(candidate):
                pairs.append((i, j))
            elif len(word) > len(candidate) and _is_palindrome(word, len(candidate)):
                pairs.append((i, j))
            elif len(word) < len(candidate) and _is_palindrome(candidate, len(word)):
                pairs.append((i, j))

    return pairs


def run_tests():
    tests = [
        (
            ['a', 'ab', 'aaa'],
            [(0, 2), (1, 0), (2, 0)]
        ),
        (
            ['abcd', 'dcba', 'lls', 's', 'sssll'],
            [(0, 1), (1, 0), (2, 4), (3, 2)]
        ),
        (
            ['bat', 'tab', 'cat'],
            [(0, 1), (1, 0)]
        ),
        (
            ['a', ''],
            [(0, 1), (1, 0)]
        ),
        (
            ['bb', 'bababab', 'baab', 'abaabaa', 'aaba', '', 'bbaa', 'aba', 'baa', 'b'],
            [(0, 5), (0, 9), (1, 5), (2, 5), (4, 3), (4, 8), (5, 0), (5, 1), (5, 2),
             (5, 7), (5, 9), (6, 0), (7, 4), (7, 5), (8, 2), (8, 9), (9, 0), (9, 5)]
        )
    ]

    for n_test, (words, expected) in enumerate(tests):
        result = palindrome_pairs(words)
        result.sort()
        if result != expected:
            raise Exception(f'Test #{n_test} failed:\n'
                            f'result={result}\nexpect={expected}')
    print('Success!')


if __name__ == '__main__':
    run_tests()
