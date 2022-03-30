x = input('Choose action(+, -, *, /): ')
c = int(input('Count operations: '))

count_o = 0
count = 0
while c != 0:
  count_o += 1
  print(count_o, end = ' ')
  a = int(input('Set number: '))

  
  if x == '+':
    count += a
  elif x == '-':
    count -= a
  elif x == '*':
    count *= a
  elif x == '/':
    count //= a
  else:
    print('Error! Try again.')
    print()
    a = int(input('Set number: '))
  c -= 1
  print()

print('Result: ', count)