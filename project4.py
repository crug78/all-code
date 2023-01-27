import random

trialnum = 0 
a = 0 
b = 0
c = 0 
d = 0 
e = 0 
f = 0 
g = 0
h = 0 
i = 0 
j = 0 
while trialnum < 1000:
    x = (random.randint(1, 10))
    if x == 1:
        a = a + 1
    elif x == 2:
        b = b + 1
    elif x == 3:
        c = c + 1
    elif x == 4:
        d = d + 1
    elif x == 5:
        e = e + 1
    if x == 6:
        f = f + 1
    elif x == 7:
        g = g + 1
    elif x == 8:
        h = h + 1
    elif x == 9:
        i = i + 1
    elif x == 10:
        j = j + 1
    trialnum = trialnum + 1

print("number of trials", trialnum)
print("number of ones", a)
print("number of twos", b)
print("number of threes", c)
print("number of fours", d)
print("number of fives", e)
print("number of 6", f)
print("number of 7", g)
print("number of 8", h)
print("number of 9", i)
print("number of 10", j)