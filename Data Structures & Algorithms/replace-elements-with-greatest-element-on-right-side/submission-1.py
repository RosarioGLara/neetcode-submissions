class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        counter = [0] * len(arr)
        counter[-1] = -1
        for i in range(len(arr)-1, 0, -1):
            max_curr = max(counter[i], arr[i])
            counter[i-1] = max_curr
        
        return counter