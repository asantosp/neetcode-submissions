class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        what = set()
        for i in range(len(nums)):
            if nums[i] in what:
                return True
            what.add(nums[i])
            
        return False