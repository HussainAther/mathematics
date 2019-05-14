"""
Palindromes are the same forwards and backwards.
"""

def isPalindrome(n):
    """
    Is n a palindrome?
    """
    return n == n[::-1]
