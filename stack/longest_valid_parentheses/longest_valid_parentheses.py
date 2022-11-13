'''
https://leetcode.com/problems/longest-valid-parentheses/
'''


def longest_valid_parentheses(text: str) -> int:
    stack = [-1]
    longest = 0

    for i, char in enumerate(text):
        if char == '(':
            stack.append(i)
            continue

        stack.pop()
        if stack:
            longest = max(longest, i - stack[-1])
        else:
            stack.append(i)

    return longest


def run_tests() -> None:
    tests: list[tuple[str, int]] = [
        ('()()(',       4),
        (')()())()()(', 4),
        (')))',         0),
        ('(()',         2),
        (')()())',      4),
        ('',            0),
        ('()())',       4),
        ('(()(()',      2),
        ('(()(())',     6),
        ('())(',        2),
        ('',            0),
    ]

    for n_test, (text, expected) in enumerate(tests):
        result = longest_valid_parentheses(text)
        if result != expected:
            raise Exception(f'Test #{n_test} failed: result={result}, expected={expected}')

    print('Success!')


if __name__ == '__main__':
    run_tests()
