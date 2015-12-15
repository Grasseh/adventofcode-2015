from inputs.input15 import input
import re
import copy
string = input()
array = string.splitlines()
value = 0
ingredients = []

class Ingredient:
  def __init__(self,name,capacity,durability,flavor,texture,calories):
    self.name = name
    self.capacity = int(capacity)
    self.durability = int(durability)
    self.flavor = int(flavor)
    self.texture = int(texture)
    self.calories = int(calories)

for lines in array:
  matchUp = re.match("(.+): capacity (.+), durability (.+), flavor (.+), texture (.+), calories (.+)",lines)
  if matchUp:
    ingredients.append(Ingredient(matchUp.group(1),matchUp.group(2),matchUp.group(3),matchUp.group(4),matchUp.group(5),matchUp.group(6)))

value = 0

def CountIngredient(index,used):
  return ingredients[index].capacity


for i in range(0,101): #First ingredient
  thisValue = CountIngredient(0,i)
  value = thisValue if thisValue > value else value

print "answer" , value

