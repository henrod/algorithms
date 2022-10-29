'''
Design a data structure that supports adding new words and finding if
a string matches any previously added string.

Example:
1. addWord("bad")
2. search("bad") # return True
3. search(".ad") # return True
3. search("..d") # return True

https://leetcode.com/problems/design-add-and-search-words-data-structure
'''

from __future__ import annotations


class Trie:
    class _Node:
        def __init__(self) -> None:
            self._children: dict[str, Trie._Node] = {}
            self._is_word = False

    def __init__(self) -> None:
        self._root = self._Node()

    def add_word(self, word: str) -> None:
        node = self._root
        for letter in word:
            if letter not in node._children:
                node._children[letter] = self._Node()
            node = node._children[letter]
        node._is_word = True

    def _search(self, word: str, i: int, node: Trie._Node) -> bool:
        if i >= len(word):
            return node._is_word

        if word[i] != '.':
            if not word[i] in node._children:
                return False
            return self._search(word, i + 1, node._children[word[i]])

        for next_node in node._children.values():
            if self._search(word, i + 1, next_node):
                return True

        return False

    def search(self, word: str) -> bool:
        return self._search(word, 0, self._root)


if __name__ == '__main__':
    trie = Trie()

    with open('input.txt') as input:
        for line in input:
            strs = line.split()
            op = strs[0]
            word = strs[1]

            if op == 'addWord':
                trie.add_word(word)
                print(f'add_word("{word}")')
            elif op == 'search':
                expected = strs[2]
                exists = trie.search(word)
                print(f'search("{word}") -> {exists}, '
                      f'expected = {expected}')
            else:
                raise Exception(f'invalid op: {op}')
