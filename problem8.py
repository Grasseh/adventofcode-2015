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
    previous = ""
    hexCount = 0
    for character in data:
      if hexCount > 0:
        value += 1
        hexCount -= 1
      if previous == "&":
        if character == "&":
          value += 1
          previous = ""
        elif character == "@":
          value += 1
          previous = "@"
        elif character == "x":
          value += 1
          hexCount = 2
          previous = "x"
      else:
        previous = character
  value += 2

print value
