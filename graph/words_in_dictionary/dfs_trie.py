'''
Given a matrix of letters and a dictionary, returns the words in the matrix present
in the dictionary. A word in the matrix is formed by consecutive letters in either
direction up, right, down, or left. You can't reuse a coordinate.

Complexities:
- Time: O(M*N*len(word))
- Space: O(M*N + len(dictionary)*len(word))
'''

from __future__ import annotations


class Trie:
    class Node:
        def __init__(self):
            self.children: dict[str, Trie.Node] = {}
            self.children_count: dict[str, int] = {}
            self.word: str | None = None

    def __init__(self) -> None:
        self.root = self.Node()

    def add(self, word: str) -> None:
        node = self.root

        for letter in word:
            if letter not in node.children:
                node.children[letter] = self.Node()
                node.children_count[letter] = 0

            node.children_count[letter] += 1
            node = node.children[letter]

        node.word = word

    def remove(self, word: str) -> None:
        node = self.root

        for letter in word:
            if letter not in node.children:
                return

            next_node = node.children[letter]
            node.children_count[letter] -= 1
            if node.children_count[letter] == 0:
                del node.children_count[letter]
                del node.children[letter]

            node = next_node

        node.word = None


def adj(matrix: list[list[str]], row: int, col: int) -> list[tuple[int, int]]:
    return [
        (row + drow, col + dcol)
        for drow, dcol in [(-1, 0), (1, 0), (0, -1), (0, 1)]
        if (
            0 <= row + drow < len(matrix) and
            0 <= col + dcol < len(matrix[0])
        )
    ]


def _find_words(
    matrix: list[list[str]],
    trie: Trie,
    row: int,
    col: int,
    node: Trie.Node,
    ans: list[str],
) -> None:
    letter = matrix[row][col]
    if letter not in node.children:
        return

    next_node = node.children[letter]
    if next_node.word:
        ans.append(next_node.word)
        trie.remove(next_node.word)

    matrix[row][col] = '#'

    for adj_row, adj_col in adj(matrix, row, col):
        _find_words(matrix, trie, adj_row, adj_col, next_node, ans)

    matrix[row][col] = letter


def find_words(matrix: list[list[str]], dictionary: list[str]) -> list[str]:
    trie = Trie()
    for word in dictionary:
        trie.add(word)

    ans: list[str] = []

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            _find_words(matrix, trie, row, col, trie.root, ans)

    return ans


def run_tests() -> None:
    tests = [
        (
            [
                ['C', 'A', 'R'],
                ['O', 'S', 'K'],
                ['P', 'Y', 'R'],
            ],
            ['COPY', 'ASK', 'CAR', 'SOS'],
            ['COPY', 'CAR', 'ASK'],
        ),
        (
            [
                ['C', 'A'],
                ['O', 'S'],
            ],
            ['CASOC', 'CASU', 'XYZ'],
            [],
        ),
        (
            [
                ['O', 'A', 'A', 'N'],
                ['E', 'T', 'A', 'E'],
                ['I', 'H', 'K', 'R'],
                ['I', 'F', 'L', 'V']
            ],
            ['OATH', 'PEA', 'EAT', 'RAIN'],
            ['OATH', 'EAT'],
        ),
        (
            [
                ['A', 'B'],
                ['C', 'D']
            ],
            ['ABCB'],
            []
        ),
    ]

    for n_test, (matrix, dictionary, expected) in enumerate(tests):
        result = find_words(matrix, dictionary)
        if result != expected:
            raise Exception(f'Test #{n_test} failed: result={result}, expected={expected}')

    print('Success!')


if __name__ == '__main__':
    run_tests()
