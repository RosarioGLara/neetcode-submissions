class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = {}

        for i in range(len(nums)):
            if nums[i] in tracker.keys():
                return [tracker[nums[i]], i]
            
            res = target - nums[i]
            tracker[res] = i
        
        return []