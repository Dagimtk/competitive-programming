class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        list=0;
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if (nums[i]+nums[j])==k:
                    nums[i]=0
                    nums[j]=0
                    list+=1
        return list
mysolution=Solution()
print(mysolution.maxOperations([1,2,3,4],5))
