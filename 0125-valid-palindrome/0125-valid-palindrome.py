class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s=''.join(c for c in s if c.isalnum())
        s_reverse=s[::-1]
        return s == s_reverse