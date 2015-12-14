from inputs.input13 import input
import re
import copy
string = input()
array = string.splitlines()
value = 0
persons = []

class Person:
  def __init__(self,name):
    self.name = name
    self.distances = []
  def printDistances(self):
    string = self.name
    for distance in self.distances:
      string += "(" + distance.printDistance() + ")"
    print string
  def getBestDistance(self,done):
    value = 0
    short = ""
    done.append(self.name)
    for distance in self.distances:
      if not distance.person in done:
        #Find Person
        for person in persons:
          if person.name == distance.person:
            FoundPerson = person
        #Call FoundPerson getShorterDistance with
        doneAttempt = copy.copy(done)
        thisValue = FoundPerson.getBestDistance(doneAttempt)
        #GetPointsToAddWithNext
        addedValue = thisValue + distance.distance
        #GetPointsToAddWithPrevious
        Index = 0
        i = 0
        for person in persons:
          if person.name == FoundPerson.name:
            Index = i
          i += 1
        #NOT FIRST
        if Index != 0:
          for otherDistance in persons[Index].distances:
            if otherDistance.person == self.name:
              addedValue += otherDistance.distance
        if addedValue > value:
          value = addedValue
    #Deal with first
    if len(done) == len(persons):
      for person in persons: #Last to me
        if person.name == done[0]:
          for otherDistance in person.distances:
            if otherDistance.person == self.name:
              value += otherDistance.distance
          for distance in self.distances:#Me to last
            if distance.person == person.name:
              value += distance.distance
      for distance in self.distances:#Me to previous
        if distance.person == done[len(done) - 1]:
          value += distance.distance
    print done,value
    return value

class Distance:
  def __init__(self,person,distance):
    self.person = person
    self.distance = distance
  def printDistance(self):
    return self.person + "->" + ":" + str(self.distance)

for lines in array:
  matchUp = re.match("(.+) would (.+) (\d+) happiness units by sitting next to (.+).",lines)
  if matchUp:
    person1 = matchUp.group(1)
    person2 = matchUp.group(4)
    gain = int(matchUp.group(3))
    if matchUp.group(2) == "lose":
      gain *= -1
    found = False
    for person in persons:
      if person.name == person1:
        person.distances.append(Distance(person2,gain))
        found = True
    if not found:
      newPerson = Person(person1)
      newPerson.distances.append(Distance(person2,gain))
      persons.append(copy.copy(newPerson))

value = 0
for person in persons:
  person.printDistances()
value = persons[0].getBestDistance([])
print "answer" , value

