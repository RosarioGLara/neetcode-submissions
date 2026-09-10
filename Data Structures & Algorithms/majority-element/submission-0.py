class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)//2
        tracker = {}

        for i in nums:
            tracker[i] = tracker.get(i, 0) + 1

        return max(tracker, key=tracker.get)