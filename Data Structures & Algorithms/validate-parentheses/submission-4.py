class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        for i in s:
            stack.append(i)
            if len(stack) < 2:
                continue
            
            if stack[-2] + stack[-1] in ["{}", "[]", "()"]:
                stack.pop()
                stack.pop()

        return stack == []            