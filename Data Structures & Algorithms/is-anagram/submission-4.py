class Solution:

    def helper(self, word):
        counter_word = {}
        for i in word:
            if i not in counter_word.keys():
                counter_word[i] = 1
                continue
            counter_word[i] += 1
        return counter_word

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter_s, counter_t = self.helper(s), self.helper(t)
        
        return counter_t == counter_s