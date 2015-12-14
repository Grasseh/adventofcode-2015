from inputs.input14 import input
import re
import copy
string = input()
array = string.splitlines()
value = 0
reindeers = []

class Reindeer:
  def __init__(self,name,speed,dashtime,rest):
    self.name = name
    self.speed = int(speed)
    self.dashtime = int(dashtime)
    self.resttime = int(rest)
    self.isDashing = True
    self.timeForStatus = int(dashtime)
    self.distance = 0
  def getDistanceAfterTime(self,time):
    for i in range(0,time):
      if self.isDashing:
        self.distance += self.speed
      self.timeForStatus -= 1
      if self.timeForStatus == 0:
        self.isDashing = not self.isDashing
        if self.isDashing:
          self.timeForStatus = self.dashtime
        else:
          self.timeForStatus = self.resttime
    return self.distance


for lines in array:
  matchUp = re.match("(.+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.",lines)
  if matchUp:
    reindeers.append(Reindeer(matchUp.group(1),matchUp.group(2),matchUp.group(3),matchUp.group(4)))

value = 0
for reindeer in reindeers:
  thisValue = reindeer.getDistanceAfterTime(2503)
  if thisValue > value or value == 0:
    value = thisValue
  print reindeer.name , thisValue
print "answer" , value

