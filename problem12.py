import json
from inputs.input12 import input
string = input()
test = '[1,2,3]'

def getIntSumInObject(object):
  value = 0
  for stuff in object:
    if type(object) == list:
      if type(stuff) == list:
        value += getIntSumInObject(stuff)
      elif type(stuff) == int:
        value += stuff
      elif type(stuff) == dict:
        value += getIntSumInObject(stuff)
    elif type(object) == dict:
      if type(object[stuff]) == list:
        value += getIntSumInObject(object[stuff])
      elif type(object[stuff]) == int:
        value += object[stuff]
      elif type(object[stuff]) == dict:
        value += getIntSumInObject(object[stuff])

  return value


jsonObject = json.loads(test)
print getIntSumInObject(jsonObject)
