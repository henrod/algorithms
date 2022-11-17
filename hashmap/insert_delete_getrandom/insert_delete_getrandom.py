'''
https://leetcode.com/problems/insert-delete-getrandom-o1/
'''

import random


class ValuesHolder:
    def __init__(self) -> None:
        self._arr: list[int] = []
        self._mapping: dict[int, list[int]] = {}

    def insert(self, value: int) -> None:
        self._arr.append(value)
        if value not in self._mapping:
            self._mapping[value] = []

        self._mapping[value].append(len(self._arr) - 1)

    def delete(self, value: int) -> None:
        if value not in self._mapping:
            raise ValueError(f'value {value} not found')

        i = self._mapping[value][-1]
        j = len(self._arr) - 1

        self._arr[i], self._arr[j] = self._arr[j], self._arr[i]
        self._arr.pop()

        self._mapping[value].pop()

        if i != j:
            self._mapping[self._arr[i]].append(i)

    def get_random(self) -> int:
        if not self._arr:
            raise RuntimeError('empty array')

        i = random.randint(0, len(self._arr) - 1)
        return self._arr[i]


def run_tests():
    tests = [
        ('insert', 1),
        ('insert', 2),
        ('insert', 3),
        ('insert', 3),
        ('random', {1: 0, 2: 0, 3: 0}),
        ('delete', 3),
        ('random', {1: 0, 2: 0, 3: 0}),
        ('insert', 4),
        ('random', {1: 0, 2: 0, 3: 0, 4: 0}),
    ]

    holder = ValuesHolder()

    for op, value in tests:
        if op == 'insert':
            holder.insert(value)
        elif op == 'delete':
            holder.delete(value)
        elif op == 'random':
            for _ in range(1_000):
                result = holder.get_random()
                value[result] += 1
            print(value)

    print('Success!')


if __name__ == '__main__':
    run_tests()
