from __future__ import annotations


class LRUCache:
    class _Node:
        def __init__(self, key: int | None = None, value: int | None = None) -> None:
            self._key = key
            self._value = value
            self._next: LRUCache._Node | None = None
            self._prev: LRUCache._Node | None = None

    def __init__(self, capacity: int) -> None:
        self._cap = capacity
        self._map: dict[int, LRUCache._Node] = {}
        self._head = self._Node()
        self._tail = self._Node()
        self._head._next = self._tail
        self._tail._prev = self._head

    def _remove(self, node: LRUCache._Node) -> None:
        node_prev = node._prev
        node_next = node._next
        node_prev._next = node_next
        node_next._prev = node_prev

    def _push(self, node: LRUCache._Node) -> None:
        node._next = self._head._next
        node._prev = self._head

        self._head._next._prev = node
        self._head._next = node

    def get(self, key: int) -> int:
        if key not in self._map:
            return -1

        node = self._map[key]
        self._remove(node)
        self._push(node)
        return node._value

    def put(self, key: int, value: int) -> None:
        if key in self._map:
            node = self._map[key]
            node._value = value
        else:
            node = LRUCache._Node(key, value)
            self._map[key] = node
            self._push(node)

        if len(self._map) > self._cap:
            node = self._tail._prev
            del self._map[node._key]
            self._remove(node)


if __name__ == '__main__':
    capacity = int(input())
    cache = LRUCache(capacity)

    n_ops = int(input())

    for _ in range(n_ops):
        op = input()
        if op == 'get':
            key = int(input())
            value = cache.get(key)
            print(f'get({key}): {value}')
        if op == 'put':
            key, value = list(map(int, input().split()))
            cache.put(key, value)
            print(f'put({key}) = {value}')
