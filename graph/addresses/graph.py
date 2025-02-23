'''
Design a data structure that adds complete addresses and returns true if a
partial address is present in it.
The complete address is composed by state, city, street and number.

Example:
insert('sp', 'sao_paulo', 'paulista', '101')
search('sp', 'sao_paulo', 'paulista', '101') # return True
search('sp', '', 'paulista', '101') # return True
search('sp', '', 'paulista', '') # return True
search('', 'ubatuba', 'paulista', '') # return False
'''

from __future__ import annotations


class Graph:
    class _Vertex:
        def __init__(self):
            self._adjs: dict[str, Graph._Vertex] = {}

    def __init__(self):
        self._root = self._Vertex()

    def insert(self, values: list[str]) -> None:
        node = self._root
        for value in values:
            if value not in node._adjs:
                node._adjs[value] = self._Vertex()
            node = node._adjs[value]

    def _search(self, values: list[str], vertex: Graph._Vertex) -> bool:
        if not values:
            return True

        value = values[0]

        if value != '':
            if value not in vertex._adjs:
                return False
            return self._search(values[1:], vertex._adjs[value])

        for adj_vertex in vertex._adjs.values():
            if self._search(values[1:], adj_vertex):
                return True

        return False

    def search(self, values: list[str]) -> bool:
        return self._search(values, self._root)


def test():
    op_cases = [
        ('insert', 'state1', 'city1', 'street1', 'number1'),
        ('insert', 'state1', 'city1', 'street1', 'number2'),
        ('insert', 'state1', 'city1', 'street1', 'number3'),

        ('insert', 'state1', 'city1', 'street2', 'number1'),
        ('insert', 'state1', 'city1', 'street2', 'number2'),
        ('insert', 'state1', 'city1', 'street2', 'number3'),

        ('insert', 'state1', 'city2', 'street1', 'number1'),
        ('insert', 'state1', 'city2', 'street1', 'number2'),
        ('insert', 'state1', 'city2', 'street1', 'number3'),

        ('insert', 'state2', 'city1', 'street1', 'number1'),
        ('insert', 'state2', 'city1', 'street1', 'number2'),
        ('insert', 'state2', 'city1', 'street1', 'number3'),

        ('search', 'state1', 'city1', 'street1', 'number1', True),
        ('search', 'state3', 'city1', 'street1', 'number1', False),
        ('search', 'state1', 'city3', 'street1', 'number1', False),
        ('search', 'state1', 'city1', 'street3', 'number1', False),
        ('search', 'state1', 'city1', 'street1', 'number4', False),
        ('search', 'state1', 'city1', 'street1', '', True),
        ('search', 'state1', 'city1', '', 'number1', True),
        ('search', 'state1', '', 'street1', 'number1', True),
        ('search', '', 'city1', 'street1', 'number1', True),
        ('search', 'state1', '', 'street1', '', True),
        ('search', '', '', '', '', True),
    ]

    graph = Graph()

    for n_test, op_case in enumerate(op_cases):
        op = op_case[0]
        if op == 'insert':
            address = op_case[1:]
            graph.insert(address)
        elif op == 'search':
            address = op_case[1:-1]
            expected = op_case[-1]
            result = graph.search(address)

            if result != expected:
                raise Exception(
                    f'Failed test #{n_test}: result={result}, expected={expected}')

    print('Success!')


if __name__ == '__main__':
    test()
