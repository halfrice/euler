#The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

def isPrime(n):
  if n%2 == 0 and n > 2: return False
  for i in range(3, int(n**0.5)+1, 2):
    if n%i == 0: return False
  return True

def pfac(n):
  primefacs = []
  for i in range(3,int(n**0.5)+1,2):
    if isPrime(i) and n%i == 0:
      primefacs.append(i)
  return primefacs[-1] # return largest prime factor

print(pfac(600851475143))
