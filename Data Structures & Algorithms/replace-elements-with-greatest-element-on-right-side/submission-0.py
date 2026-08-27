class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        for i in range(len(arr)-1):
            currentMax = max(arr[i+1:])
            
            arr[i] = currentMax
        
        arr[-1] = -1
        return arr