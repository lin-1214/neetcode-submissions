class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = dict()
        for i, n in enumerate(nums):
            complement = target - n
            if complement in table:
                return list((table[complement], i))
            table[n] = i



        
        