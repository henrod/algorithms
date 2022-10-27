# Given a list of temperatures, return a list of days until
# the next warmer day.
# Example:
# Input: [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

def next_warmer_day(temperatures: list[int]) -> list[int]:
    r: list[int] = [0] * len(temperatures)
    stack: list[tuple[int, int]] = []

    for i in range(len(temperatures) - 1, -1, -1):
        temp = temperatures[i]

        while stack:
            j, next_temp = stack[-1]
            if temp < next_temp:
                r[i] = j - i
                break
            stack.pop()

        stack.append((i, temp))

    return r


if __name__ == '__main__':
    n_cases = int(input())

    for case in range(n_cases):
        temperatures = list(map(int, input().split()))
        expected = input()

        result = next_warmer_day(temperatures)
        print(f'Case #{case}: result={result}, expected={expected}')
