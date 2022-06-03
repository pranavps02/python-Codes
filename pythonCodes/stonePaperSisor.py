import random

i = 0
u = 0
p = 0

list = ["s","w","g"]


while(i!=10) :
     user = input("Enter your Chance :")
     pc = random.choice(list)
     print("user : ", user ,"   PC : " ,pc)
     if user == "s" and pc == "w":
        u = u+1
     if user == "s" and pc == "g":
        p = p+1
        print()
     if user == "g" and pc == "w":
        p = p+1
     if user == "w" and pc == "s":
        p = p+1
     if user == "g" and pc == "s":
        u = u+1
     if user == "w" and pc == "g":
        u = u+1
     i=i-1

print("PC won %d times",p)
print("USER won %d times",u)
if p > u :
    print("Final Winner PC")
if u > p :
    print("Final Winner USER")



