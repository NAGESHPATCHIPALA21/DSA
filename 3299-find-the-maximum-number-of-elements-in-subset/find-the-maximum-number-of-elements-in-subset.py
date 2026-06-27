class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        freq = Counter(nums)
        ans = 1

        if 1 in freq:
            ans = max(ans, freq[1] if freq[1] & 1 else freq[1] - 1)

        for x in freq:
            if x == 1:
                continue

            cur = x
            length = 0

            while freq[cur] >= 2 and freq[cur * cur] >= 1:
                length += 2
                cur *= cur

            ans = max(ans, length + 1)

        return ans
        