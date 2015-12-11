def NextPassword(sequence):
  Okay = False
  string = list(sequence)
  position = len(sequence) - 1
  while(not Okay):
    if(string[position] != "z"):
      string[position] = chr(ord(string[position]) + 1)
      Okay = True
    else:
      string[position] = "a"
      if position == 0:
        string = ["a"] + string
        Okay = True
      else:
        position -= 1
  return "".join(string)

def IsPasswordValid(string):
  check = True
  check = check and IsCheck1(string)
  check = check and IsCheck2(string)
  check = check and IsCheck3(string)
  return check

def IsCheck1(string):
  check = False
  previous = 0
  twoBack = 0
  for character in string:
    check = check or (ord(character) - 1 == previous and ord(character) - 2 == twoBack)
    twoBack = previous
    previous = ord(character)
  return check

def IsCheck2(string):
  check = True
  check = check and not "i" in string
  check = check and not "l" in string
  check = check and not "o" in string
  return check

def IsCheck3(string):
  #Two different pairs
  pairOne = ""
  pairTwo = ""
  previous = ""
  for character in string:
    if character == previous:
      if pairOne == "":
        pairOne = character
      else:
        if character != pairOne:
          pairTwo = character
    previous = character
  return pairTwo != ""

string = "hepxxyzz"
string = NextPassword(string)
i = 0
while not IsPasswordValid(string):
  string = NextPassword(string)
  i += 1
  if (i % 1000 == 0):
    print string
print string
