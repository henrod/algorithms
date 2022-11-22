'''
https://leetcode.com/problems/range-module/discuss/2279206/Digested-explanation-after-reading-some-posts...-Python
'''


class RangeModule:
    def __init__(self):
        self._list: list[int] = []

    def _find_left(self, value: int) -> int:
        l, r = 0, len(self._list) - 1

        while l <= r:
            m = (l + r) // 2
            if self._list[m] >= value:
                r = m - 1
            else:
                l = m + 1

        return l

    def _find_right(self, value: int) -> int:
        l, r = 0, len(self._list) - 1

        while l <= r:
            m = (l + r) // 2
            if self._list[m] <= value:
                l = m + 1
            else:
                r = m - 1

        return l

    def addRange(self, left: int, right: int) -> None:
        start = self._find_left(left)
        end = self._find_right(right)

        sublist = []
        if start % 2 == 0:
            sublist.append(left)
        if end % 2 == 0:
            sublist.append(right)

        self._list[start:end] = sublist

    def removeRange(self, left: int, right: int) -> None:
        start = self._find_left(left)
        end = self._find_right(right)

        sublist = []
        if start % 2 == 1:
            sublist.append(left)
        if end % 2 == 1:
            sublist.append(right)

        self._list[start:end] = sublist

    def queryRange(self, left: int, right: int) -> bool:
        start = self._find_right(left)
        end = self._find_left(right)
        return start % 2 == 1 and start == end


def run_tests() -> None:
    range_module = RangeModule()

    tests: list[tuple[str, int, int] | tuple[str, int, int, bool]] = [
        # ('add', 10, 20),
        # ('remove', 14, 16),
        # ('query', 10, 14, True),
        # ('query', 13, 15, False),
        # ('query', 16, 17, True),

        # ('add', 10, 20),
        # ('query', 10, 14, True),
        # ('remove', 14, 16),
        # ('query', 13, 15, False),
        # ('add', 25, 30),
        # ('query', 18, 28, False),
        # ('query', 28, 29, True),
        # ('remove', 29, 40),
        # ('query', 27, 28, True),
        # ('remove', 0, 5),
        # ('query', 11, 13, True),

        ('add', 6, 8),
        ('remove', 7, 8),
        ('remove', 8, 9),
        ('add', 8, 9),
        ('remove', 1, 3),
        ('add', 1, 8),
        ('query', 2, 4, True),
        ('query', 2, 9, True),
        ('query', 4, 6, True),
    ]

    for n_test, test in enumerate(tests):
        start, end = test[1:3]

        if test[0] == 'add':
            range_module.addRange(start, end)
        elif test[0] == 'remove':
            range_module.removeRange(start, end)
        elif test[0] == 'query':
            expected = test[3]
            result = range_module.queryRange(start, end)
            if result != expected:
                raise Exception(f'Test #{n_test} failed:'
                                f'result={result}, expected={expected}')

    print('Success!')


if __name__ == '__main__':
    run_tests()
