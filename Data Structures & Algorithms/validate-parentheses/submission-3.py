class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = ["[]", "{}", "()"]
        for i in s:
            stack.append(i)
            if len(stack) < 2:
                continue
            if stack[-2] + stack[-1] in valid:
                stack.pop()
                stack.pop()
        
        return stack == []