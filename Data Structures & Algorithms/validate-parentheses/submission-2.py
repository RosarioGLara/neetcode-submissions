class Solution:
    def isValid(self, s: str) -> bool:
        stack = [s[0]]
        for i in s[1:]:
            stack.append(i)
            if len(stack) < 2:
                continue
            i, j = stack.pop(), stack.pop()
            if j+i in ["[]", "()", "{}"]:
                    continue
            stack.extend([j,i])
        return stack == []
              
        