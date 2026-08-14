class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights)-1
        final = float('-inf')
        while i < j:
            mini = min(heights[i], heights[j])
            res = (j-i) * mini
            if mini == heights[j]:
                j -=1
            if mini == heights[i]:
                i += 1
            
            if res > final:
                final = res
        return final