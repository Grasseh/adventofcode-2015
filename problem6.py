from inputs.input6 import input
string = input()
array = string.splitlines()
value = 0
grid = []
#Fill grid @off
for i in range(0, 1000):
  grid.append([])
  for j in range(0, 1000):
    grid[i].append(False)
#Run commands
for command in array:
  firstSeparator = command.find(",")
  secondSeparator = command.find(",",firstSeparator + 1)
  y1 = command[firstSeparator + 1:command.find(" ",firstSeparator + 1)]
  x2 = command[command.find(" ",firstSeparator + 5) + 1:secondSeparator]
  y2 = command[secondSeparator + 1:]
  if command.find("turn on") != -1:
    x1 = command[8:firstSeparator]
    for i in range(int(x1),int(x2)+1):
      for j in range(int(y1),int(y2)+1):
        grid[i][j] = True
  elif command.find("turn off") != -1:
    x1 = command[9:firstSeparator]
    for i in range(int(x1),int(x2)+1):
      for j in range(int(y1),int(y2)+1):
        grid[i][j] = False
  elif command.find("toggle") != -1:
    x1 = command[7:firstSeparator]
    for i in range(int(x1),int(x2)+1):
      for j in range(int(y1),int(y2)+1):
        grid[i][j] = not grid[i][j]

#Count
for i in range(0,1000):
  for j in range(0,1000):
    value += grid[i][j] if 1 else 0
print value
