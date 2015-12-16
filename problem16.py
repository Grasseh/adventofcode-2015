from inputs.input16 import input
import re
import copy
string = input()
array = string.splitlines()
value = "0"
sues = []

class Sue:
  def __init__(self,name,data):
    self.name = name
    self.data = data

  def checkInput(self,inputString):
    inputArray = inputString.splitlines()
    check = True
    for lines in inputArray:
      matchUp = re.match("(.+): (\d+)",lines)
      if matchUp:
        key = matchUp.group(1)
        value = matchUp.group(2)
        if key in self.data:
          check = check and self.data[key] == value
    return check

for lines in array:
  matchUp = re.match("Sue (.+): (.+): (\d+), (.+): (\d+), (.+): (\d+)",lines)
  if matchUp:
    newArray = {}
    newArray[matchUp.group(2)] = matchUp.group(3)
    newArray[matchUp.group(4)] = matchUp.group(5)
    newArray[matchUp.group(6)] = matchUp.group(7)
    sues.append(Sue(matchUp.group(1),newArray))


MFCSAM = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1"""
for sue in sues:
  if sue.checkInput(MFCSAM):
    value = sue.name

print "answer" , value

