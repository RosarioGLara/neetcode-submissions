class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            num_i = -nums[i]
            j, k = i + 1, len(nums)-1
            while j < k:
                res = nums[j] + nums[k]
                if res == num_i:
                    triplets.append([-num_i, nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif res < num_i:
                    j += 1
                elif res > num_i:
                    k -= 1
        return triplets