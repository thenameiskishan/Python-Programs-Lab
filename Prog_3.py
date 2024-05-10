n = 4
if n%2==0:
    print("number is even")
else:
    print("number is odd")
    
    
############


count = 0
no = 5

for i in range(2, no+1):
    if no%i==0:
        count +=1
    
if count != 0 or count > 0:
    print(f"{no} is not a prime number")
else:
    print(f"{no} is a prime number")
    
    
############


fact = 1

num = 5

for i in range(1,num+1):
    fact *= i
    
print(f"factorial of {num} is {fact}")