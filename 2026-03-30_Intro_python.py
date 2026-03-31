name="daniel"

blood_type = "0+, is my blood type"
type(blood_type)
print(type(blood_type))
age = 31
print(type(age))
height = 180.21356
print(type(height))
print (f"Helloy, my name is {name}")

if height >180:
    print("Good for you")
else:
    pass

#< # less than
#> # more than 
#<= #less than equal to
#>= # more than equal to
#== #equal to
#!= #not equal to
#% #modulo - division to give remainder
#// #float divison, oposite from modulo

if name=="daniel" and age==31:
    print("thats our teacher")
else:
    print("who is that")
#or

#loops

#for loops
for n in range(age):
    print(f"This is the {age}")

#while loops
while age<35:
    print("You are less than 35")
    age += 1 #also for -, *, /

for c in name:
    print(c[0])
