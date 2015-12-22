input = 36000000
value = 60
presents = 0

def GetDivisors(number):
  array = []
  for i in range(1,number + 1):
    if number % i == 0:
      array.append(i)
  return array


while presents < input:
  presents = 0
  value += 60
  for divisor in GetDivisors(value):
    presents += divisor * 10
    print value, divisor, presents

print "answer", value
