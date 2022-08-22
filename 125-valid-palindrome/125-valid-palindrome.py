class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [i for i in s.lower() if i.isalnum()]
        if s == s[::-1]:
            return True
        else: 
            return False