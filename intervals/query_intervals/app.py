"""
Build a class that holds a list of ranges and has two functions:
* AddRange: adds a new range
* Query: given a value, return True if within at least one range
"""


class Intervals:
    def __init__(self) -> None:
        self._intervals = []

    def _find(self, num):
        ints = self._intervals
        l, r = 0, len(ints) - 1

        while l <= r:
            m = (l + r) // 2

            if ints[m][0] <= num <= ints[m][1]:
                return m, True

            if num < ints[m][0]:
                r = m - 1
            else:
                l = m + 1

        return l, False

    def add(self, start, end):
        l, _ = self._find(start)
        r, includes = self._find(end)
        if includes:
            r += 1

        self._intervals[l:r] = [(start, end)]

    def query(self, num):
        _, includes = self._find(num)

        return includes


if __name__ == "__main__":
    tests = [
        ("add", 2, 5),
        ("add", 9, 13),
        ("query", 0, False),
        ("query", 2, True),
        ("query", 8, False),
        ("query", 10, True),
        ("query", 20, False),
        ("add", 7, 10),
        ("query", 8, True),
        ("add", 10, 20),
        ("query", 20, True),
    ]

    intervals = Intervals()

    for n_test, test in enumerate(tests):
        op = test[0]

        if op == "add":
            intervals.add(start=test[1], end=test[2])
        if op == "query":
            actual = intervals.query(num=test[1])
            expected = test[2]
            if actual != expected:
                raise Exception(
                    f"Test #{n_test} failed:" f"actual={actual}, expected={expected}"
                )

    print("Success!")
