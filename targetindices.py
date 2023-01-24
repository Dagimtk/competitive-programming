
class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        List = []

        for i in range(len(nums)):
            if nums[i] == target:
                List.append(i)
        
        return List

mySolution = Solution()
print(mySolution.targetIndices([1,2,5,2,3], 2))
