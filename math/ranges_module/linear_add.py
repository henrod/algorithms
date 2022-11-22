class RangesModule:
    def __init__(self) -> None:
        self._values: list[int] = []
        self._neg_values: list[int] = []

    def _add(self, values: list[int], start: int, end: int):
        if end >= len(values):
            values.extend([0] * (end - len(values)))

        for i in range(start, end + 1):
            values[i] = 1

    def add(self, start: int, end: int) -> None:
        if start >= 0:
            self._add(self._values, start, end)
        elif end >= 0:
            self._add(self._neg_values, 0, -start-1)
            self._add(self._values, 0, end)
        else:
            self._add(self._neg_values, -end-1, -start-1)

    def query(self, value: int) -> bool:
        if value >= 0:
            idx = value
            values = self._values
        else:
            idx = -value-1
            values = self._neg_values

        return values[idx] == 1


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
