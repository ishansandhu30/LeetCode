class Solution:
    def isPalindrome(self, s: str) -> bool:
        stringL = s.lower()
        a=[]
        for i in stringL:
            if i.isalnum():
                a.append(i)
        if a == a[::-1]:
            return True
        else:
            return False
                