from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count the frequency of the numbers
        freq = defaultdict(int)
        for i in nums:
            freq[i] += 1
        
        # bucket sort:
        buckets = {i:[] for i in range(len(nums)+1)}
        for key, value in freq.items():
            buckets[value].append(key)

        # top k elements
        top_k = []
        for i in range(len(nums), 0, -1):
            if len(top_k) == k:
                break
            if buckets[i]:
                top_k.extend(buckets[i])
        return top_k
    

            

        
        
