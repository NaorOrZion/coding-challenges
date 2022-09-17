class Solution(object): 
    def canJump(self, nums):
        far = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if far - i <= nums[i]:
                far = i
        return far == 0
        