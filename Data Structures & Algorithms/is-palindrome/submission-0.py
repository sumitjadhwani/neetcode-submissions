class Solution:
    def isPalindrome(self, s: str) -> bool:
        string_to_check=""
        for c in s:
            if c.isalnum():
                string_to_check+=c.lower()
        
        return(string_to_check == string_to_check[::-1])