class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        x=len(nums)
        nums.sort()
        return nums[x//2]

       

        

