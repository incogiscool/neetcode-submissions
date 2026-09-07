class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        exists_dict = {}
        for i in range(len(nums)):
            if nums[i] in exists_dict:
                return True
            else:
                exists_dict[nums[i]] = 1
        return False
        