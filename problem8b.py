from inputs.input8 import input
import re
#Note : Find and replace all "" in the input by @ and all \ by &
string = input()
array = string.splitlines()
value = 0

for lines in array:
  matchUp = re.match("@(.*)@",lines)
  if matchUp:
    data = matchUp.group(1)
    for character in data:
      if character == "&":
        value += 1
      elif character == "@":
        value += 1
  value += 4

print value
