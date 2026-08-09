class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def isAnagram(word1,word2):
            return sorted(word1) == sorted(word2)
        
        anagrams = []
        while strs:
            curr= strs[0]
            l = [curr]
            strs.pop(0)
            index = 0
            while index < len(strs):
                if isAnagram(strs[index],curr):
                    l.append(strs[index])
                    strs.pop(index)
                else:
                    index +=1
            anagrams.append(l)
        return anagrams
        