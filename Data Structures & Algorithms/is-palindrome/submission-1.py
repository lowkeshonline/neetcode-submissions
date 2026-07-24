class Solution:

    def is_alphanumeric(self, c):

        if (ord(c) >= 48 and ord(c) <= 57
            or ord(c) >= 65 and ord(c) <= 90
            or ord(c) >= 97 and ord(c) <= 122):
            return True
        
        return False


    def isPalindrome(self, s: str) -> bool:

        newstr = ""

        for c in s:
            if self.is_alphanumeric(c):
                newstr += c.lower()
            
        return newstr == newstr[::-1]


        