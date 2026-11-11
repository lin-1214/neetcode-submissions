class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        table = dict()
        for num in nums:
            if num in table and table[num] == 1:
                return True

            table[num] = 1

        return False     
        