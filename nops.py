class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        solution=[]
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if (nums[i]+nums[j]==target):
                    solution.append(i)
                    solution.append(j)
        return solution

mysolution=Solution()
print(mysolution.twoSum([2,7,11,15],9))
