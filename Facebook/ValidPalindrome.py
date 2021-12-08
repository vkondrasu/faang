class Solution:
    """
    1. string is equal to it's reversal then True
    2. if not for each char -- if it's equivalent position from end match then nothing to do
    3. when it doesn't match there are 2 possibilities either ignoring the left char or right car
    4. if any one of them is a palindrome then fine, if not return False
    """
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        if s == s[::-1]:
            return True
        else:
            for i in range(n):
                if s[i] != s[n-(i+1)]:
                    a = s[:i] + s[i+1:]
                    b = s[:n-(i+1)] + s[n-(i+1)+1:]
                    if a == a[::-1] or b == b[::-1]:
                        return True
                    else:
                        return False

