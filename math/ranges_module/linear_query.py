class RangesModule:
    def __init__(self) -> None:
        self._ranges: set[tuple[int, int]] = set()

    def add(self, start: int, end: int) -> None:
        self._ranges.add((start, end))

    def query(self, value: int) -> bool:
        for start, end in self._ranges:
            if start <= value <= end:
                return True

        return False


def run_tests() -> None:
    tests = [
        ('add', 2, 5),
        ('add', 9, 13),
        ('query', 0, False),
        ('query', 3, True),
        ('query', 10, True),
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
