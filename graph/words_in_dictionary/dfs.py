'''
Given a matrix of letters and a dictionary, returns the words in the matrix present
in the dictionary. A word in the matrix is formed by consecutive letters in either
direction up, right, down, or left. You can't reuse a coordinate.

Complexities:
- Time: O(len(dictionary) * len(word) * N * M)
- Space: O(N*M)
'''


def adj(matrix: list[list[str]], row: int, col: int) -> list[tuple[int, int]]:
    r = []

    if row - 1 >= 0:
        r.append((row - 1, col))
    if row + 1 < len(matrix):
        r.append((row + 1, col))
    if col - 1 >= 0:
        r.append((row, col - 1))
    if col + 1 < len(matrix[row]):
        r.append((row, col + 1))

    return r


def find_word(matrix: list[list[str]], word: str) -> bool:
    def find(row: int, col: int, i: int, visited: set[tuple[int, int]]) -> bool:
        if i >= len(word):
            return True

        if matrix[row][col] != word[i]:
            return False

        for adj_row, adj_col in adj(matrix, row, col):
            if (adj_row, adj_col) not in visited:
                visited.add((adj_row, adj_col))
                if find(adj_row, adj_col, i + 1, visited):
                    return True
                visited.remove((adj_row, adj_col))

        return False

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if find(row, col, 0, {(row, col)}):
                return True

    return False


def find_words(matrix: list[list[str]], dictionary: list[str]) -> list[str]:
    ans = []

    for word in dictionary:
        if find_word(matrix, word):
            ans.append(word)

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
            ['COPY', 'ASK', 'CAR'],
        ),
        (
            [
                ['C', 'A'],
                ['O', 'S'],
            ],
            ['CASOC', 'CASU', 'XYZ'],
            [],
        ),
    ]

    for n_test, (matrix, dictionary, expected) in enumerate(tests):
        result = find_words(matrix, dictionary)
        if result != expected:
            raise Exception(f'Test #{n_test} failed: result={result}, expected={expected}')

    print('Success!')


if __name__ == '__main__':
    run_tests()
