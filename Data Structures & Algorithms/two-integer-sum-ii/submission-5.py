class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        ans = []
        l = 0
        r = n - 1

        while l < r:
            cand = target - numbers[l]
            if cand == numbers[r]:
                ans.append(l+1)
                ans.append(r+1)
                return ans
            elif cand < numbers[r]:
                r -= 1
            else:
                l += 1
        