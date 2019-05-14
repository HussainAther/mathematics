"""
A Lychrel (lychrel) number is a natural number that cannot form a palindrome through the iterative process of 
repeatedly reversing its digits and adding the resulting numbers. 
1. Take an integer n, greater than zero.
2. Form the next n of its series by reversing the digits of the current n and adding the result to the current n.
3. Stop when n becomes palindromic - i.e. the digits of n in reverse order == n.
"""

if __name__ == "__main__":
    maxn, reversion_limit = 10000, 500
    print("Calculations using n = 1..%i and limiting each search to 2*%i reverse-digits-and-adds"
          % (maxn, reversion_limit))
    lychrel, l_related = find_lychrel(maxn, reversion_limit)
    print("  Number of Lychrel numbers:", len(lychrel))
    print("    Lychrel numbers:", ", ".join(str(n) for n in lychrel))
    print("  Number of Lychrel related:", len(l_related))
    pals = [x for x in lychrel + l_related  if x == reverse_int(x)]
    print("  Number of Lychrel palindromes:", len(pals))
    print("  Lychrel palindromes:", ", ".join(str(n) for n in pals))
