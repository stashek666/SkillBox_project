a = int(input('Set first number: '))
b = int(input('Set second number: '))
x = input('Choose action(+, -, *, /): ')

while True:
  if x == '+':
    print('Result: ', a, x, b, '=', a + b)
    break
  elif x == '-':
    print('Result: ', a, x, b, '=', a - b)
    break
  elif x == '*':
    print('Result: ', a, x, b, '=', a * b)
    break
  elif x == '/':
    print('Result: ', a, x, b, '=', a // b)
    break
  else:
    print('Error! Try again.')
    print()
    a = int(input('Set first number: '))
    b = int(input('Set second number: '))
    x = input('Choose action(+, -, *, /): ')