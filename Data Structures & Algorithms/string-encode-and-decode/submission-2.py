class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "empty"
        string = strs[0]
        for s in strs[1:]:
            string = string + ":;" + s 
        return string
    def decode(self, s: str) -> List[str]:
        if s == "empty":
            return []
        return s.split(':;')
