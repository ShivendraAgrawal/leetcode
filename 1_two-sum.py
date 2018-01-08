class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, num in enumerate(nums):
            if target - num in nums[:i]:
                return [nums.index(num), nums[:i].index(target - num)]
            elif target - num in nums[i+1:]:
                return [nums.index(num), i + 1 + nums[i+1:].index(target - num)]


solution = Solution()
print(solution.twoSum([3,3], 6))
