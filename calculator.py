def addition(num1, num2):
  return num1 + num2

def subtraction(num1, num2):
  return num1 - num2

def multiplication(num1, num2):
  return num1 * num2

def division(num1, num2):
  return num1/num2

print('\n \
      option 1: addition \n \
      option 2: subtraction \n \
      option 3: multiplication \n \
      option 4: division')

option = float(input('what operation do you want to use?'))

num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))

if option == 1 or option == 'option 1':
  print(num1, '+', num2, '=', addition(num1, num2))

if option == 2 or option == 'option 2':
  print(num1, '-', num2, '=', subtraction(num1, num2))

if option == 3 or option == 'option 3':
  print(num1, '*', num2, '=', multiplication(num1, num2))

if option == 4 or option == 'option 4':
  print(num1, '/', num2, '=', division(num1, num2))
