class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter_s, counter_t = {}, {}
        for i in s:
            if i not in counter_s.keys():
                counter_s[i] = 1
                continue
            counter_s[i] += 1
        
        for i in t:
            if i not in counter_t.keys():
                counter_t[i] = 1
                continue
            counter_t[i] += 1
        return counter_t == counter_s