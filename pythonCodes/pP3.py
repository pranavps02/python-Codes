lst = []
n = int(input("Enter number of elements in list of Calories : "))
print(f"Enter {n} Elements :")

for i in range(0, n):
    ele = int(input())
    lst.append(ele)

lst.reverse()
r1=lst
lst.reverse
lst[::-1]
r2=lst


for i in range(n):
        j = n-i-1
        x = lst[i]
        y = lst[j]
        lst[i] = x
        lst[j] = y

print(r1)
print(r2)
print(lst)

if r1 == r2 == lst :
    print("list =", end=" ")
    print(lst)
else:
    print("Daya !!! Kuch to gadbad hai !!")







