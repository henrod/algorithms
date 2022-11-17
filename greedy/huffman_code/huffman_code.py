from __future__ import annotations
import heapq


class Node:
    def __init__(self, letter: str) -> None:
        self.letter = letter
        self.freq = 0
        self.left: Node | None = None
        self.right: Node | None = None
        self.code = ''

    def __lt__(self, other: Node) -> bool:
        return self.freq < other.freq

    def __repr__(self) -> str:
        return f'({self.letter}: {self.code}) {self.left}, {self.right}'


class HuffmanCode:
    def __init__(self, word: str) -> None:
        self.nodes = self._nodes(word)
        self.root = self._build_tree(self.nodes)
        self._set_code(self.root, [])

    def encode(self, word: str) -> str:
        encoded = []
        for letter in word:
            encoded.append(self.nodes[letter].code)

        return ''.join(encoded)

    def decode(self, code: str) -> str:
        word: list[str] = []
        i = 0
        while i < len(code):
            i = self._decode(code, i, self.root, word)
        return ''.join(word)

    def _decode(self, code: str, i: int, node: Node, word: list[str]) -> int:
        if node.letter:
            word.append(node.letter)
            return i

        if i >= len(code):
            return i

        if code[i] == '0':
            i = self._decode(code, i + 1, node.left, word)
        else:
            i = self._decode(code, i + 1, node.right, word)

        return i

    def _build_tree(self, nodes: dict[str, Node]) -> Node:
        heap = list(nodes.values())
        heapq.heapify(heap)

        while heap:
            node = Node('')
            node.left = heapq.heappop(heap)
            node.freq = node.left.freq
            if not heap:
                break

            node.right = heapq.heappop(heap)
            node.freq += node.right.freq
            if not heap:
                break

            heapq.heappush(heap, node)

        return node

    def _nodes(self, word: str) -> dict[str, Node]:
        nodes: dict[str, Node] = {}
        for letter in word:
            if letter not in nodes:
                nodes[letter] = Node(letter)
            nodes[letter].freq += 1
        return nodes

    def _set_code(self, node: Node | None, code: list[str]) -> None:
        if not node:
            return

        if node.letter:
            node.code = ''.join(code)
            return

        code.append('0')
        self._set_code(node.left, code)
        code.pop()

        code.append('1')
        self._set_code(node.right, code)
        code.pop()


def run_tests() -> None:
    tests = [
        ('a', '0'),
        ('aaaabbc', '1111010100'),
        ('bcabaaa', '0100101111'),
    ]

    for n_test, (word, expected) in enumerate(tests):
        huffman = HuffmanCode(word)

        print(huffman.root)

        result = huffman.encode(word)
        if result != expected:
            raise Exception(f'Test #{n_test} failed for encoding:'
                            f'result={result}, expected={expected}')

        decoded = huffman.decode(result)
        if word != decoded:
            raise Exception(f'Test #{n_test} failed for decoding:'
                            f'result={decoded}, expected={word}')

    print('Success!')


if __name__ == '__main__':
    run_tests()
