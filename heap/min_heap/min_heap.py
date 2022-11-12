class MinHeap:
    def __init__(self) -> None:
        self._arr: list[int] = []

    def _parent(self, i: int) -> int:
        return int((i - 1) / 2)

    def _left(self, i: int) -> int:
        return 2 * i + 1

    def _right(self, i: int) -> int:
        return 2 * i + 2

    def _swap(self, i: int, j: int) -> None:
        self._arr[i], self._arr[j] = self._arr[j], self._arr[i]

    def _bubble_up(self, i: int) -> None:
        parent = self._parent(i)
        while self._arr[parent] > self._arr[i]:
            self._swap(i, parent)
            i = parent

    def _sink_down(self, i: int) -> None:
        left, right = self._left(i), self._right(i)
        n = len(self._arr)

        while left < n or right < n:
            if left < n and self._arr[i] > self._arr[left]:
                target = left
            elif right < n and self._arr[left] > self._arr[right]:
                target = right
            else:
                break

            self._swap(i, target)
            i = target
            left, right = self._left(i), self._right(i)

    def push(self, value: int) -> None:
        self._arr.append(value)
        self._bubble_up(len(self._arr) - 1)

    def pop(self) -> int:
        self._swap(0, -1)
        value = self._arr.pop()
        self._sink_down(0)
        return value


def run_tests() -> None:
    tests = [
        ('push', 1), ('push', 2), ('pop', 1), ('push', 3), ('pop', 2), ('pop', 3),
        ('push', 3), ('push', 2), ('push', 1), ('pop', 1), ('pop', 2), ('pop', 3),
    ]

    heap = MinHeap()

    for n_test, (op, value) in enumerate(tests):
        if op == 'push':
            heap.push(value)
        elif op == 'pop':
            result = heap.pop()
            if result != value:
                raise Exception(f'Test #{n_test} failed: result={result}, expected={value}')

    print('Success!')


if __name__ == '__main__':
    run_tests()
