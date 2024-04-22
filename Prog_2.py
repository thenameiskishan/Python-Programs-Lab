x=2
y=3

print(x,y)

x,y = y,x

print(x,y)



#######


c=21

f = (c*9/5)+32
print(f"{c} degree celcius to fehrenhite: {f}")


#######


import calendar
year = 2024
print(calendar.calendar(year))

#####
n=1

if n==0:
    print("number is equal to zero")
elif n>0:
    print("number is positive")
else:
    print("number is negative")