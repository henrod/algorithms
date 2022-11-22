class RangesModule:
    def __init__(self) -> None:
        self._ranges: list[int] = []

    def _find_left(self, val: int) -> int:
        l, r = 0, len(self._ranges) - 1
        while l <= r:
            m = (l + r) // 2
            if self._ranges[m] == val:
                return m

            if self._ranges[m] < val:
                l = m + 1
            else:
                r = m - 1

        return l

    def _find_right(self, val: int) -> int:
        l, r = 0, len(self._ranges) - 1
        while l <= r:
            m = (l + r) // 2
            if self._ranges[m] == val:
                return m + 1

            if self._ranges[m] < val:
                l = m + 1
            else:
                r = m - 1

        return l

    def add(self, start: int, end: int) -> None:
        left = self._find_left(start)
        right = self._find_right(end)

        subrange = []
        if left % 2 == 0:
            subrange.append(start)
        if right % 2 == 0:
            subrange.append(end)

        self._ranges[left:right] = subrange

    def query(self, val: int) -> bool:
        idx = self._find_left(val)
        return idx % 2 == 1 or idx < len(self._ranges) and self._ranges[idx] == val


def run_tests() -> None:
    tests = [
        ('add', 2, 5),
        ('add', 9, 13),
        ('query', 0, False),
        ('query', 3, True),
        ('query', 10, True),
        ('query', 13, True),
        ('add', 13, 16),
        ('query', 13, True),
        ('add', -10, -8),
        ('query', -2, False),
        ('query', -8, True),
    ]

    ranges_module = RangesModule()

    for n_test, test in enumerate(tests):
        if test[0] == 'add':
            start, end = test[1:]
            ranges_module.add(start, end)
        else:
            value, expected = test[1:]
            result = ranges_module.query(value)
            if result != expected:
                raise Exception(f'Test #{n_test} failed:'
                                f'result={result}, expected={expected}')

    print('Success!')


if __name__ == '__main__':
    run_tests()
