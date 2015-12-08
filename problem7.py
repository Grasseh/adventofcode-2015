from inputs.input7 import input
import re
string = input()
array = string.splitlines()
objects = []

def is_num(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

class Wire:
  value = -1
  def __init__(self,name,string,value):
    self.name = name
    self.string = string
    self.value = value

  def findValue(self):
    if self.value == -1:
      #Find value of this wire
      #Check if string is basevalue
      baseMatch = re.match("(\d+) -> (.+)",self.string)
      if baseMatch:
        self.value = baseMatch.group(1)
      #Check for standard assign
      standardMatch = re.match("(.{1,2}) -> (.+)",self.string)
      if standardMatch:
        objectToMatch = standardMatch.group(1)
        for wires in objects:
          if wires.name == objectToMatch:
            self.value = wires.findValue()
      #Check for NOT assign
      notMatch = re.match("NOT (.{1,2}) -> (.+)",self.string)
      if notMatch:
        objectToMatch = notMatch.group(1)
        for wires in objects:
          if wires.name == objectToMatch:
            self.value = 65535 - int(wires.findValue())
      #AND gate
      andMatch = re.match("(.{1,2}) AND (.{1,2}) -> (.+)",self.string)
      if andMatch:
        value1 = -1
        value2 = -1
        objectToMatch1 = andMatch.group(1)
        isDigit = is_num(objectToMatch1)
        if isDigit:
          value1 = int(objectToMatch1)
          objectToMatch1 = "zzz"
        objectToMatch2 = andMatch.group(2)
        for wires in objects:
          if wires.name == objectToMatch1:
            value1 = wires.findValue()
          if wires.name == objectToMatch2:
            value2 = wires.findValue()
        self.value = int(value1) & int(value2)
      #OR gate
      orMatch = re.match("(.{1,2}) OR (.{1,2}) -> (.+)",self.string)
      if orMatch:
        value1 = -1
        value2 = -1
        objectToMatch1 = orMatch.group(1)
        objectToMatch2 = orMatch.group(2)
        for wires in objects:
          if wires.name == objectToMatch1:
            value1 = wires.findValue()
          if wires.name == objectToMatch2:
            value2 = wires.findValue()
        self.value = int(value1) | int(value2)
      #RSHIFT GATE
      rightMatch = re.match("(.{1,2}) RSHIFT (\d+) -> (.+)",self.string)
      if rightMatch:
        objectToMatch = rightMatch.group(1)
        amountShift = int(rightMatch.group(2))
        for wires in objects:
          if wires.name == objectToMatch:
            self.value = (int(wires.findValue()) >> amountShift) & 65535
      #LSHIFT GATE
      leftMatch = re.match("(.{1,2}) LSHIFT (\d+) -> (.+)",self.string)
      if leftMatch:
        objectToMatch = leftMatch.group(1)
        amountShift = int(leftMatch.group(2))
        for wires in objects:
          if wires.name == objectToMatch:
            self.value = (int(wires.findValue()) << amountShift) & 65535
      print self.name , self.value, self.string
    else:
      print self.name , self.value

    return str(self.value)

for line in array:
  arrow = line.find("->")
  name = line[arrow + 3:]
  string = line
  value = -1
  objects.append(Wire(name,string,value))

for wires in objects:
  if wires.name == "a":
    print wires.findValue()
