class Solution:
    def twoSum(self, nums, target):
        x= {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in x:
                return [x[complement], i]

            x[num] = i
  
 