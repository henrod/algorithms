"""
Design a data structure that adds complete addresses and returns true if a
partial address is present in it.
The complete address is composed by state, city, street and number.

Example:
insert('sp', 'sao_paulo', 'paulista', '101')
search('sp', 'sao_paulo', 'paulista', '101') # return True
search('sp', '', 'paulista', '101') # return True
search('sp', '', 'paulista', '') # return True
search('', 'ubatuba', 'paulista', '') # return False
"""


class Solution:
    def __init__(self):
        self._addresses: set[str] = set()

    def _insert(self, address: list[str], i: int, partial_address: list[str]) -> None:
        if i >= len(address):
            self._addresses.add(tuple(partial_address))
            return

        partial_address.append(address[i])
        self._insert(address, i + 1, partial_address)
        partial_address.pop()

        partial_address.append("")
        self._insert(address, i + 1, partial_address)
        partial_address.pop()

    def insert(self, address: list[str]) -> None:
        self._insert(address, 0, [])

    def search(self, address: list[str]) -> bool:
        return tuple(address) in self._addresses


def test():
    op_cases = [
        ("insert", "state1", "city1", "street1", "number1"),
        ("insert", "state1", "city1", "street1", "number2"),
        ("insert", "state1", "city1", "street1", "number3"),
        ("insert", "state1", "city1", "street2", "number1"),
        ("insert", "state1", "city1", "street2", "number2"),
        ("insert", "state1", "city1", "street2", "number3"),
        ("insert", "state1", "city2", "street1", "number1"),
        ("insert", "state1", "city2", "street1", "number2"),
        ("insert", "state1", "city2", "street1", "number3"),
        ("insert", "state2", "city1", "street1", "number1"),
        ("insert", "state2", "city1", "street1", "number2"),
        ("insert", "state2", "city1", "street1", "number3"),
        ("search", "state1", "city1", "street1", "number1", True),
        ("search", "state3", "city1", "street1", "number1", False),
        ("search", "state1", "city3", "street1", "number1", False),
        ("search", "state1", "city1", "street3", "number1", False),
        ("search", "state1", "city1", "street1", "number4", False),
        ("search", "state1", "city1", "street1", "", True),
        ("search", "state1", "city1", "", "number1", True),
        ("search", "state1", "", "street1", "number1", True),
        ("search", "", "city1", "street1", "number1", True),
        ("search", "state1", "", "street1", "", True),
        ("search", "", "", "", "", True),
    ]

    solution = Solution()

    for n_test, op_case in enumerate(op_cases):
        op = op_case[0]
        if op == "insert":
            address = op_case[1:]
            solution.insert(address)
        elif op == "search":
            address = op_case[1:-1]
            expected = op_case[-1]
            result = solution.search(address)

            if result != expected:
                raise Exception(
                    f"Failed test #{n_test}: result={result}, expected={expected}"
                )

    print("Success!")


if __name__ == "__main__":
    test()
