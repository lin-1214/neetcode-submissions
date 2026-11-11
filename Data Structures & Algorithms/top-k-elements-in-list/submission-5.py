class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = dict()
        bucket = [[] for _ in range(len(nums) + 1)] 
        ans = []

        for n in nums:
            if n not in table:
                table[n] = 0

            table[n] += 1

        for n in table:
            bucket[table[n]].append(n)

        for i in range(len(nums), -1, -1):
            for candidate in bucket[i]:
                if k > 0:
                    ans.append(candidate)
                    k -= 1

        return ans
