def longest_palindrome(word: str) -> int:
    def size(l: int, r: int) -> int:
        while l >= 0 and r < len(word) and word[l] == word[r]:
            l -= 1
            r += 1
        return r - l - 1

    max_size = 0

    for i in range(len(word)):
        max_size = max(max_size, size(i, i), size(i, i + 1))

    return max_size


if __name__ == '__main__':
    tests = [
        ('abbac', 4),
        ('abc', 1),
        ('abcba', 5),
    ]

    for n_test, (word, expected) in enumerate(tests):
        result = longest_palindrome(word)
        if result != expected:
            raise Exception(f'Test #{n_test} failed:'
                            f'result={result}, expected={expected}')

    print('Success!')
