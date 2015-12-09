from inputs.input9 import input
import re
import copy
#Note : Find and replace all "" in the input by @ and all \ by &
string = input()
array = string.splitlines()
value = 0
cities = []

class City:
  def __init__(self,name):
    self.name = name
    self.distances = []
  def printDistances(self):
    string = self.name
    for distance in self.distances:
      string += "(" + distance.printDistance() + ")"
    print string
  def getShorterDistance(self,done):
    value = 0
    short = ""
    done.append(self.name)
    print done
    for distance in self.distances:
      if not distance.city2 in done:
        #Find City2
        for city in cities:
          if city.name == distance.city2:
            city2 = city
        #Call City2 getShorterDistance with
        thisValue = city2.getShorterDistance(copy.copy(done))
        if thisValue + distance.distance > value:
          value = thisValue + distance.distance
    return value

class Distance:
  def __init__(self,city1,city2,distance):
    self.city1 = city1
    self.city2 = city2
    self.distance = distance
  def printDistance(self):
    return self.city1 + "->" + self.city2 + ":" + str(self.distance)

for lines in array:
  matchUp = re.match("(.*) to (.*) = (\d*)",lines)
  if matchUp:
    print "test"
    city1 = matchUp.group(1)
    city2 = matchUp.group(2)
    distance = int(matchUp.group(3))
    foundFirst = False
    foundSecond = False
    for city in cities:
      if city.name == city1:
        city.distances.append(Distance(city1,city2,distance))
        foundFirst = True
      if city.name == city2:
        city.distances.append(Distance(city2,city1,distance))
        foundSecond = True
    if not foundFirst:
      newCity = City(city1)
      newCity.distances.append(Distance(city1,city2,distance))
      cities.append(copy.copy(newCity))
    if not foundSecond:
      newCity = City(city2)
      newCity.distances.append(Distance(city2,city1,distance))
      cities.append(copy.copy(newCity))

value = 0
for city in cities:
  city.printDistances()
  thisValue = city.getShorterDistance([])
  if thisValue > value or value == 0:
    value = thisValue
  print thisValue
print "answer" , value

