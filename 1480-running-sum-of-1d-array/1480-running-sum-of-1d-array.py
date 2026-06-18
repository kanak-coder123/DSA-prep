class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        x=len(nums)
        for i in range(1,x):
            nums[i] = nums[i] + nums[i - 1]
        return nums