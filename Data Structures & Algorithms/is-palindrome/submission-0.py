class Solution:
    def isPalindrome(self, s: str) -> bool:

        # filter the non - alphanumeric chars from the input and make it lowercase
        cleaned = "".join(filter(str.isalnum, s)).lower()

        # take two pointer approach to compare chars on both sides
        left = 0
        right = len(cleaned) - 1

        # visit every element until each pointer crosses their opposite pointer
        while left <= right:
            # if left char not equals to right char return false (not palindrome)
            if cleaned[left] != cleaned[right]:
                return False
            
            # increase left pointer and decrease right pointer
            left += 1
            right -= 1
        
        #return True if no difference found
        return True

        