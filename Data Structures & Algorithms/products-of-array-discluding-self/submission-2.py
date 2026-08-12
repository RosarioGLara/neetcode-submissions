class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # get prefix and postfix
        prefix, postfix = [1] * len(nums), [1] * len(nums)
        for i in range(len(nums)):
            next_num = prefix[i-1]
            prefix[i] = nums[i] * next_num 
        for i in range(len(nums)-1, -1, -1):
            next_num = postfix[i+1] if i+1 < len(nums) else 1 
            postfix[i] = nums[i] * next_num
        res = [] 
        for i in range(len(nums)):
            n = prefix[i-1] if i > 0 else 1 
            m = postfix[i+1] if i < len(postfix)-1 else 1
            res.append(n*m)
        return res
