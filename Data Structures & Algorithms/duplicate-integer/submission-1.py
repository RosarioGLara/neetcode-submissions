class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        expected = [1] * len(nums)
        hashmap = {}
        for i in nums:
            if i not in hashmap.keys():
                hashmap[i] = 1
                continue
            hashmap[i] += 1
        
        return list(hashmap.values()) != expected