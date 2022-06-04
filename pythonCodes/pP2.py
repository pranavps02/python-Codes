n = int(input("Enter The VAlue of n : "))
min = int(input("Enter the Lowest value in Range : "))
max = int(input("Enter the Highest value in Range : "))


if min == max or min > max :
    print("Invalid Range !!!")

else:
    for i in range(min,max+1):
        if n%i == 0:
            print(f"{n} is divisible by {i}")
            print()

        else:
            print(f"{n} is not divisible by {i}")
            print()

