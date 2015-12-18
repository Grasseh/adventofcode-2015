from inputs.input18 import input
import re
import copy
string = input()
array = string.splitlines()
value = "0"
lights = []
size = 6
steps = 0

class Light:
  def __init__(self,on):
    self.on = on
    self.next = False

#Setup grid from input
i = 0
for lines in array:
  lights.append([])
  for j in range(0,size):
    lights[i].append(Light(array[i][j] == "#"))
  i += 1

#UpdateGrid
for i in range(0,steps):
  #Setup each next
  for i in range(0,size):
    for j in range(0,size):
      lights[i][j].next = False
  #Put each on at next
  for i in range(0,size):
    for j in range(0,size):
      lights[i][j].on = lights[i][j].next


#CountAmountOn
for i in range(0,size):
  string = ""
  for j in range(0,size):
    string += "#" if lights[i][j].on else "."
  print string

print "answer" , value

