"""
Given a list of songs and a integer k, return the next song to play.
k is the number of songs before repeating one.

* k > 0 and k < len(songs)
* len(songs) > 0
"""

from collections import deque
from random import randint


class Shuffle:
    def __init__(self, songs: list[str], k: int) -> None:
        self._songs = songs
        self._queue = deque([None] * k)

    def next(self) -> str:
        i = randint(0, len(self._queue) - 1)
        song = self._songs[i]

        self._songs[i] = self._songs[-1]
        self._songs.pop()

        available_song = self._queue.popleft()
        if available_song:
            self._songs.append(available_song)

        self._queue.append(song)

        return song


if __name__ == "__main__":
    tests = [
        (["A", "B", "C", "D"], 2, 10),
        (["A", "B"], 1, 10),
    ]

    for n_test, (songs, k, n_calls) in enumerate(tests):
        shuffle = Shuffle(songs, k)
        for _ in range(n_calls):
            print(f"Test #{n_test + 1} - Next song: {shuffle.next()}")
