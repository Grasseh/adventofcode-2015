class Item:
  def __init__(self,regEx):
    matchUp = re.match("(.+)\s+(\d+)\s+(\d+)\s+(\d+)",regEx)
    if matchUp:
      self.name = matchUp.group(1)
      self.cost = matchUp.group(2)
      self.damage = matchUp.group(3)
      self.armor = matchUp.group(4)

class Entity:
  def __init__(self,name,hitPoints,armor,damage):
    self.name = name
    self.hitPoints = hitPoints
    self.currentHitPoints = hitPoints
    self.armor = armor
    self.damage = damage


def Fight(entity1,entity2):
  bothAlive = True
  Winner = False
  while bothAlive:
    damage = entity1.damage - entity2.armor
    damage = 1 if damage < 1 else damage
    entity2.currentHitPoints -= damage
    #print (entity1.name + " attacks " + entity2.name + " for " + str(damage) + " hit points (" + str(entity2.currentHitPoints) + "/" + str(entity2.hitPoints) + ")")
    if entity2.currentHitPoints <= 0:
      bothAlive = False
      Winner = True
    else:
      damage = entity2.damage - entity1.armor
      damage = 1 if damage < 1 else damage
      entity1.currentHitPoints -= damage
      #print (entity2.name + " attacks " + entity1.name + " for " + str(damage) + " hit points (" + str(entity1.currentHitPoints) + "/" + str(entity1.hitPoints) + ")")
      if entity1.currentHitPoints <= 0:
        bothAlive = False
  return Winner


import re
bosshealth = 104
bossarmor = 1
bossdamage = 8
weapons = []
for line in open('inputs/problem21/weapons.txt', 'r').read().splitlines():
  weapons.append(Item(line))
armors = []
for line in open('inputs/problem21/armor.txt', 'r').read().splitlines():
  armors.append(Item(line))
armors.append(Item("NONE 0 0 0"))
rings = []
for line in open('inputs/problem21/rings.txt', 'r').read().splitlines():
  rings.append(Item(line))
rings.append(Item("NONE 0 0 0"))

value = -1
print len(rings)
for w in weapons:
  for a in armors:
    for r1 in rings:
      for r2 in rings:
        cost =  int(w.cost) + int(a.cost) + int(r1.cost) + int(r2.cost)
        armor = int(w.armor) + int(a.armor) + int(r1.armor) + int(r2.armor)
        damage = int(w.damage) + int(a.damage) + int(r1.damage) + int(r2.damage)
        if value == -1 or cost < value:
          Player = Entity("Player",100,armor,damage)
          Boss = Entity("Boss",bosshealth,bossarmor,bossdamage)
          if(Fight(Player,Boss)):
            print cost
            value = cost

print "answer" , value
print Fight(Entity("Player",8,5,5),Entity("Boss",12,2,7))
