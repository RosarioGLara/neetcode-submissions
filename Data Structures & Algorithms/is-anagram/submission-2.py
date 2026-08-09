class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict_s = dict()
        dict_t = dict()
        for i in range(len(s)):
            if not s[i] in dict_s.keys():
                dict_s[s[i]] = 1
            else:
                dict_s[s[i]] += 1
            if not t[i] in dict_t.keys():
                dict_t[t[i]] = 1
            else:
                dict_t[t[i]] += 1

        return dict_s == dict_t