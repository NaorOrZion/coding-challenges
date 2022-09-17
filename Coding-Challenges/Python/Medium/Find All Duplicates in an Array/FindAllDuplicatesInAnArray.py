class Solution(object):
    def findDuplicates(self, nums):
        dict1 = {}
        lis = []
        for i in range(len(nums)):
            if nums[i] in dict1:
                dict1[nums[i]] = 2
                lis.append(nums[i])
            else:
                dict1[nums[i]] = 1
        return lis