class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        mp = {}
        for num in nums:
            if num in mp:
                return True
            mp[num] = True
        return False
