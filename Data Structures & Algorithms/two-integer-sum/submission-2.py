class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        bucket = {}
        for i, num in enumerate(nums):
            if num in bucket.keys():
                return [bucket[num], i]
            bucket[target-num] = i
        return []