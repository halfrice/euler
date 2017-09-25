# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 
# 6th prime is 13.

# What is the 10,001st prime number?

def isPrime(n):
  if n%2 == 0 and n > 2: return False 
  for i in range(3, int(n**0.5)+1, 2):
    if n%i == 0: return False
  return True

def primeAtPos(n):
  i = 1
  count = 0
  while count < n:
    i += 1
    if isPrime(i): count += 1
  return i

# print(primenum(6))
print(primeAtPos(10001))
