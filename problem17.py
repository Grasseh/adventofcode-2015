string = """33
14
18
20
45
35
16
35
1
13
18
13
50
44
48
6
24
41
30
42
"""
array = string.splitlines()
value = 0
neededSum = 150

def NoSuchThingAsTooMuch(i,sum,on):
    global value
    if i < len(array):
        sum += int(array[i]) if on else 0
        if sum < neededSum:
            NoSuchThingAsTooMuch(i+1,sum,True)
            NoSuchThingAsTooMuch(i+1,sum,False)
        elif sum == neededSum:
            value += 1

NoSuchThingAsTooMuch(0,0,True)
NoSuchThingAsTooMuch(0,0,False)
print "answer" , value
