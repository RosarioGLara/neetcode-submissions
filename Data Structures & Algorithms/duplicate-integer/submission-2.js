class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const hashmap = new Map();
        for (var i=0; i<nums.length; i++) {
            hashmap.set(nums[i], -1);
        }

        // check which numbers already have an assigned index.
        for (var i=0; i<nums.length; i++) {
            if (hashmap.get(nums[i]) > -1) {
                return true;
            }
            hashmap.set(nums[i], i);
        }
        return false;
    }
}
