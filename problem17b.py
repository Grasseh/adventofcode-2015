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
smallest = 100
value = 0
neededSum = 150

def NoSuchThingAsTooMuch(i,sum,on,j):
    global value
    global smallest
    if i < len(array):
        sum += int(array[i]) if on else 0
        if sum < neededSum:
            NoSuchThingAsTooMuch(i+1,sum,True,j+1)
            NoSuchThingAsTooMuch(i+1,sum,False,j)
        elif sum == neededSum:
            if j < smallest:
                value = 1
                smallest = j
            elif j == smallest:
                value += 1

NoSuchThingAsTooMuch(0,0,True,1)
NoSuchThingAsTooMuch(0,0,False,0)
print "answer" , value
