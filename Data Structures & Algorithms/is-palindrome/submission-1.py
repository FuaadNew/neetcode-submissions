class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = ""
        for c in s:
            if self.isalphanum(c):
                newString+=c.lower()
        return newString == newString[::-1]


        



    def isalphanum(self,c):

        return (ord('a') <= ord(c) <= ord('z') or ord('A') <= ord(c) <= ord('Z') or ord('0') <= ord(c) <= ord('9'))  
