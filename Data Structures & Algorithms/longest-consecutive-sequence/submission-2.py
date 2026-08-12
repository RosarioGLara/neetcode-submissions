class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        longest = 1
        for i in nums:
            long = 0
            if i - 1 in nums:
                continue
            if i + 1 in nums:
                j = i 
                while j in nums:
                    long += 1
                    j += 1
                if long > longest:
                    longest = long
        return longest
            
