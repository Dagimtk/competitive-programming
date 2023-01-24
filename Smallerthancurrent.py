class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        List=[0]*len(nums)
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if nums[i]>nums[j]:
                    List[i]+=1
        return List

mySolution = Solution()
print(mySolution.smallerNumbersThanCurrent([8,1,2,2,3]))
