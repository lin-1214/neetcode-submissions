class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        for i in range(n):
            if (i != 0 and nums[i] == nums[i-1]):
                continue

            l = i + 1
            r = n - 1

            while (l < r):
                tmp = []
                if ((nums[l] + nums[r]) == -nums[i]):
                    tmp.append(nums[i])
                    tmp.append(nums[l])
                    tmp.append(nums[r])
                    ans.append(tmp)
                    l += 1
                    r -= 1
                    while (l < r and nums[l] == nums[l-1]):
                        l += 1
                    while (l < r and nums[r] == nums[r+1]):
                        r -=1

                elif ((nums[l] + nums[r]) < -nums[i]):
                    l += 1
                    while (l < r and nums[l] == nums[l-1]):
                        l += 1
                else:
                    r -= 1
                    while (l < r and nums[r] == nums[r+1]):
                        r -=1
        
        return ans
