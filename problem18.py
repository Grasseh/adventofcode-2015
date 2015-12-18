from inputs.input18 import input
import re
import copy
string = input()
array = string.splitlines()
value = 0
lights = []
size = 100
steps = 100

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
      #COUNT all eight neighbours
      count = 0
      if i > 0:
        count += 1 if lights[i-1][j].on else 0
        if j > 0:
          count += 1 if lights[i-1][j-1].on else 0
        if j < size - 1:
          count += 1 if lights[i-1][j+1].on else 0
      if i < size - 1:
        count += 1 if lights[i+1][j].on else 0
        if j > 0:
          count += 1 if lights[i+1][j-1].on else 0
        if j < size - 1:
          count += 1 if lights[i+1][j+1].on else 0
      if j > 0:
        count += 1 if lights[i][j-1].on else 0
      if j < size - 1:
        count += 1 if lights[i][j+1].on else 0


      if lights[i][j].on:
        #If on, check if 2 or 3 neighbours are on
        lights[i][j].next = count in [2,3]
      else:
        #If off, check if EXACTLY 3 neighbours are on
        lights[i][j].next = count in [3]

  #Put each on at next
  for i in range(0,size):
    for j in range(0,size):
      lights[i][j].on = lights[i][j].next


#CountAmountOn
for i in range(0,size):
  string = ""
  for j in range(0,size):
    string += "#" if lights[i][j].on else "."
    value += 1 if lights[i][j].on else 0
  print string

print "answer" , value

