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

def CountIngredient(index,used,remaining,capacity,durability,flavor,texture):
  capacity += ingredients[index].capacity * used
  durability += ingredients[index].durability * used
  flavor += ingredients[index].flavor * used
  texture += ingredients[index].texture * used
  remaining -= used
  if index == len(ingredients) - 1: #Last one
    final = 1
    final *= capacity if capacity > 0 else 0
    final *= durability if durability > 0 else 0
    final *= flavor if flavor > 0 else 0
    final *= texture if texture > 0 else 0
    final *= 0 if remaining != 0 else 1
    if capacity >= 0 and durability >= 0 and texture >= 0 and remaining == 0 and flavor >= 0:
      print "capacity" , capacity, "durability", durability, "flavor", flavor, "texture", texture, "final", final, "remaining", remaining
  else:
    final = 0
    for i in range(0,remaining + 1):
      thisValue = CountIngredient(index + 1,i,remaining,capacity,durability,flavor,texture)
      final = thisValue if thisValue > final else final
  return final


for i in range(0,101): #First ingredient
  thisValue = CountIngredient(0,i,100,0,0,0,0)
  print i
  value = thisValue if thisValue > value else value

for ingredient in ingredients:
  print ingredient.name, ingredient.capacity, ingredient.durability, ingredient.flavor, ingredient.texture

print "answer" , value

