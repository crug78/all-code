print("Hello, world! This is Python 3!")
## my name is cameron young. the purpose of this code is to find the gravation between 2 objects. the only sources i used were wikipedia to get the formula. 
##50, 40, 30, 1.48e-10
##import math function
import math
print("this calculator is for universal gravation. i will need 2 masses and a radius, or the distance between these 2 masses. ")
ma = float(input("what is mass 1?"))
## ask for first mass
mb = float(input("what is mass 2?"))
## ask for second mass
r = float(input("what is the radius?"))
## ask fr radius
r = (pow(r, 2))
## square the radius
g = float(6.67*(pow(10, -11)))
## gravitational constant
mr = ((ma * mb)/r)
## multiply the 2 masses and then divide by the radius 
f = (g * mr)
## multiply by the gravitional constant
f = round(f, 12)
#round the answer
print("the answer is")
print(f)
