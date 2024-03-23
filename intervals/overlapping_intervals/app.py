"""
Input is a list of intervals with values. When intervals overlap, the values are summed. 
Given this list, return the peak value. 

Example:
0--10 100
5--25 200
20--30 300

peak: 500 at 20--25
"""


def find_peak(intervals):
    events = [None] * (len(intervals) * 2)

    i = 0
    for start, end, value in intervals:
        events[i] = (start, value)
        events[i + 1] = (end, -value)
        i += 2

    events.sort(key=lambda event: event[0])

    peak = 0
    curr = 0
    for _, value in events:
        curr += value
        peak = max(peak, curr)

    return peak


def run_tests():
    tests = [
        {
            "intervals": [(0, 10, 100), (5, 25, 200), (20, 30, 300)],
            "expected": 500,
        },
        {
            "intervals": [(0, 30, 100), (10, 20, 200), (13, 17, 300)],
            "expected": 600,
        },
    ]

    for i, test in enumerate(tests):
        intervals = test["intervals"]
        expected_peak = test["expected"]
        actual_peak = find_peak(intervals)

        if expected_peak != actual_peak:
            raise Exception(
                f"Test #{i}: expected: {expected_peak}, actual: {actual_peak}"
            )

    print("Success")


if __name__ == "__main__":
    run_tests()
