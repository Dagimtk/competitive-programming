class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(1,len(nums)-1):
            if (nums[i-1]+nums[i+1])/2==nums[i]:
                nums[i+1],nums[i]=nums[i],nums[i+1]
                self.checkback(nums,i-1)
        return nums
    def checkback(self,nums,i):
        if i!=0 and (nums[i-1]+nums[i+1])/2==nums[i]:
                nums[i+1],nums[i]=nums[i],nums[i+1]
                self.checkback(nums,i-1)
mysolution=Solution()
print(mysolution.rearrangeArray([1,2,3,4,5]))
