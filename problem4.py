import hashlib
input = "iwrupvqb"
i = 0
found = False
while not found:
  hash = hashlib.md5()
  hash.update(input + str(i))
  found = hash.hexdigest()[:6] == "000000"
  if not found:
    i += 1
print i, hash.hexdigest(), input + str(i), hash.hexdigest()[:6] == "00000", found
