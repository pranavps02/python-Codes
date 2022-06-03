print("1.Know the year when you will turn 100 ")
print("2.Know age in particular year")
opt = int(input())
age = int(input("Enter your age or Year of Birth : "))
if opt == 1:
    if age > 999 :
         print(f"Your year of Birth is {age}.")
         if (2022-age) > 100:
              print("You are Immortal !!!")
         else :
              print(f"You will be of age 100 in year {age+100}")

    elif age <101 :
        print(f"Your age is {age}.")
        print(f"You will be of age 100 in year {2022-age+100}")

    else :
        print("Invalid Age or Year!!!")

if opt == 2:
    year = int(input("Enter the year in which you want to kow your age: "))

    if age > 999:
         print(f"Your year of Birth is {age}.")
         if age > year:
              print("Really ?!!!! . You Enterered year  which is before Your Birth")
         else :
              print(f"Your Age will be {year-age} in year {year}")

    elif age <101 :
        print(f"Your age is {age}.")
        print(f"Your Age will be {year-2022-age} in year {year}")

    else :
        print("Invalid Age or Year!!!")

else:
    print("Invalid Option!!!")


