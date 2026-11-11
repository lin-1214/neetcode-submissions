class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        
        while (l < r):
            mid = l + (r - l) // 2

            if (nums[mid] > nums[r]):
                l = mid + 1
            elif (nums[mid] < nums[r]):
                r = mid

        
        return nums[l]
            