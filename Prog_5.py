def facts(n):
    
    fact = 1
    fact*=n
    if n>=1:
    
        return fact * facts(n-1)
    else:
        return 1
    
    
print(facts(5))


########



#Reverse String

text = "hello"

rev = text[::-1]

print(rev)

# Palindrom String

text1 = "Kishan"

if text1 == text1[::-1]:
    print("is Palindrom")
else:
    print("not Palindrom")





############



words = ["fg", "erhrh", "rwgrhb", "asfae"]

words.sort()

print(words)




###########

import string

line = "Hello!! there i don't know you.."


sentence = "".join(c for c in line if c not in string.punctuation)

