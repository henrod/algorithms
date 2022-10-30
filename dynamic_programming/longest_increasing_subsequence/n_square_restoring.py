def longest_increasing_subsequence(nums: list[int]) -> list[int]:
    dp = [1] * len(nums)
    p = [i for i in range(len(nums))]

    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                p[i] = j

    max_lsi = 0
    seq_idx = -1

    for i, lsi in enumerate(dp):
        if lsi > max_lsi:
            max_lsi = lsi
            seq_idx = i

    seq = []
    while seq_idx != p[seq_idx]:
        seq.append(nums[seq_idx])
        seq_idx = p[seq_idx]

    seq.append(nums[seq_idx])
    seq.reverse()

    return seq


def run_tests():
    tests = [
        ([10, 9, 2, 5, 3, 7, 101, 18], [2, 5, 7, 101]),
        ([0, 1, 0, 3, 2, 3], [0, 1, 2, 3]),
        ([7, 7, 7, 7, 7, 7, 7], [7])
    ]

    for n_test, (nums, expected) in enumerate(tests):
        result = longest_increasing_subsequence(nums)
        if result != expected:
            raise Exception(f'Test #{n_test} failed: ',
                            f'result={result}, expected={expected}')

    print('Success!')


if __name__ == '__main__':
    run_tests()
