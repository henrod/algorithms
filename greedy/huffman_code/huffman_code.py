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


def huffman_decode(word: str) -> int:
    pass


def huffman_encode(word: str) -> str:
    nodes = _nodes(word)
    root = _build_tree(nodes)
    _set_code(root, [])

    encoded = []
    for letter in word:
        encoded.append(nodes[letter].code)

    return ''.join(encoded)


def _build_tree(nodes: dict[str, Node]) -> Node:
    heap = list(nodes.values())
    heapq.heapify(heap)

    while len(heap) > 1:
        node = Node('')
        node.left = heapq.heappop(heap)
        node.freq = node.left.freq
        if heap:
            node.right = heapq.heappop(heap)
            node.freq += node.right.freq

        heapq.heappush(heap, node)

    return node


def _nodes(word: str) -> dict[str, Node]:
    nodes: dict[str, Node] = {}
    for letter in word:
        if letter not in nodes:
            nodes[letter] = Node(letter)
        nodes[letter].freq += 1
    return nodes


def _set_code(node: Node | None, code: list[str]) -> None:
    if not node:
        return

    if node.letter:
        node.code = ''.join(code)
        return

    code.append('0')
    _set_code(node.left, code)
    code.pop()

    code.append('1')
    _set_code(node.right, code)
    code.pop()


def run_tests() -> None:
    tests = [
        ('aaaabbc', '1111010100'),
        ('bcabaaa', '0100101111'),
    ]

    for n_test, (word, expected) in enumerate(tests):
        result = huffman_encode(word)
        if result != expected:
            raise Exception(f'Test #{n_test} failed:'
                            f'result={result}, expected={expected}')

    print('Success!')


if __name__ == '__main__':
    run_tests()
