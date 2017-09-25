# A palindromic number reads the same both ways. The largest palindrome made from the 
# product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(s):
  if len(s) <= 1: return True
  if s[0] == s[-1]: return isPalindrome(s[1:-1])
  return False

def largestPalindrome(digits):
  largest = 0
  for i in range(1,10**digits):
    for j in range(1,10**digits):
      p = i*j
      isPal = isPalindrome(str(p))
      if isPal and p > largest: 
        largest = p
  return largest

# largestPalindrome(91,99)
# largestPalindrome(991,999)
print(largestPalindrome(2))
print(largestPalindrome(3))

