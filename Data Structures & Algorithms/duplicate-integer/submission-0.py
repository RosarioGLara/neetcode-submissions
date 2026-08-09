class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        has_dup = False
        for i in range(len(nums)):
            if not nums[i] in hashmap.keys():
                hashmap[nums[i]] = 1
            else:
                has_dup = True
                break
        return has_dup