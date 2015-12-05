from inputs.input5 import input
import copy
input()
string = input()
array = string.splitlines()
value = 0
for i in array:
  Check1 = False
  Check2 = False
  #Check 1 -- 2 sequences that repeat, but doesn't overlap
  sequences = []
  previous = ""
  for character in i:
    if previous + character in sequences:
      if sequences.index(previous + character) != len(sequences) - 1:
        Check1 = True
    sequences.append(copy.copy(previous + character))
    previous = character
  sequences = []
  #Check 2 -- one letter that repeats, with one in between
  twoago = ""
  previous = ""
  for character in i:
    if character == twoago:
      Check2 = True
    twoago = previous
    previous = character
  nice = Check1 and Check2
  if nice:
    value += 1

print value
