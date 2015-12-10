def LookAndSay(sequence):
  i = 0
  string = ""
  previous = sequence[0]
  count = 0
  while i < len(sequence):
    if sequence[i] == previous:
      count += 1
    else:
      string += str(count) + previous
      previous = sequence[i]
      count = 1
    i += 1
  string += str(count) + previous
  return string

string = "1321131112"
for i in range(0,50):
  string = LookAndSay(string)
print len(string)
