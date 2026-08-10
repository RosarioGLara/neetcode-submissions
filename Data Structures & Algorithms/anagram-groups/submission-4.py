from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = defaultdict(list)
        for i in strs:
            final[tuple(sorted(i))].append(i)
        
        return list(final.values())