class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicti = dict()
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in dicti:
                return sorted([i, dicti[diff]])
            else:
                dicti[nums[i]] = i
        return []
