from inputs.input5 import input
input()
string = input()
array = string.splitlines()
value = 0
for i in array:
  Check1 = False
  Check2 = False
  Check3 = True
  #Check 1 -- At least 3 vowels
  vowels = 0
  for character in i:
    if character in ["a","e","i","o","u"]:
      vowels += 1
  Check1 = vowels >= 3
  #Check 2 -- Two characters in a row
  previous = ""
  for character in i:
    if character == previous:
      Check2 = True
    previous = character
  #Check 3 -- Does not contain ab, cd, pq, or xy
  previous = ""
  for character in i:
    if previous + character in ["ab","cd","pq","xy"]:
      Check3 = False
    previous = character
  nice = Check1 and Check2 and Check3
  if nice:
    value += 1
print value
