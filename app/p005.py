# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 
# without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers 
# from 1 to 20?

def evendiv(min,max):
  div = False
  guess = max
  while div is False:
    possible = True
    i = min
    while possible and i <= max:
      if guess%i != 0: 
        guess += max
        possible = False
      i += 1
    if possible: div = True
  return guess

print(evendiv(1,20))
