# Armstrong number: Sum of its digits, where each digit raised to power of number of digits, equal to the number itself. ex- 354 = 3^3 + 5^3 + 4^3

def is_armstrong(number):

  armstrong = False
  sum = 0
  p = len(str(number))

  for num in str(number):
    sum += int(num)**p

  if sum == number:
    armstrong = True

  return armstrong

is_armstrong(int(input("Enter a number: ")))