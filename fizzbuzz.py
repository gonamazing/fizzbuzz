import random
import re
import sys

number = input("Number? ")
result = "UNDETERMINED"

def fizzBuzz(n):
  try:
    n = int(n)
  except:
    print("Input not an integer")
    sys.exit()

  threeDivisible = not (n % 3)
  fourDivisible = not (n % 4)
  if (threeDivisible and fourDivisible):
    result = "POP"
  elif (threeDivisible):
    result = "FIZZ"
  elif (fourDivisible):
    result = "BUZZ"
  
  return result

def test():
  testInput1 = random.randint(0,99999999999999)
  popOrFizz = fizzBuzz(testInput1*3)
  popOrBuzz = fizzBuzz(testInput1*4)
  popOnly = fizzBuzz(testInput1*3*4)

  print("Test Input: ", testInput1)
  count = 0

  if (re.match("POP|FIZZ", popOrFizz)):
    count += 1
    print("PASS ", count)
  else:
    count += 1
    print("FAIL ", count)
  if (re.match("POP|BUZZ", popOrBuzz)):
    count += 1
    print("PASS ", count)
  else:
    print("FAIL ", count)
    count += 1
  if (re.match("POP", popOnly)):
    count += 1
    print("PASS ", count)
  else:
    count += 1
    print("FAIL ", count)

  # Known Primes
  testInput2 = [947,953,967,971,977,983,991,997,1009,1013,1019,1021,1031,1033,1039,1049,1051,1061,1063,1069]
  for prime in testInput2:
    fizzOnly = fizzBuzz(prime*3)
    buzzOnly = fizzBuzz(prime*4)
    if (re.match("FIZZ", fizzOnly)):
      count += 1
      print("PASS ", count)
    else:
      count += 1
      print("FAIL ", count)
    
    if (re.match("BUZZ", buzzOnly)):
      count += 1
      print("PASS ", count)
    else:
      count += 1
      print("FAIL ", count)

if (number.lower() == 'test'):
  test()
else:
  print(fizzBuzz(number))
