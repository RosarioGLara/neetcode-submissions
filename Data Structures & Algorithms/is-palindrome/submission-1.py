import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_s = s.replace(" ", "").lower()
        only_letters = re.sub(r'[^a-zA-Z0-9]', '', lower_s)
        print(only_letters)

        left, right = 0, len(only_letters)-1
        while left <= right:
            print(only_letters[left], only_letters[right], only_letters[left] != only_letters[right])
            if only_letters[left] != only_letters[right]:
                return False
            left += 1
            right -= 1
        return True