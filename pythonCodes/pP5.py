
def next_palindrome(n):
       if n > 10:
           n = n + 1
           while not is_palindrome(n):
               n += 1
           return n
       else:
           return n



def is_palindrome(n):
    return str(n) == str(n)[::-1]

if __name__ == '__main__':
    t = int(input("enter No. Of test Cases :"))
    numbers = []
    pali = []
    for i in range(t):
        number = int(input("Enter the number:\n"))
        numbers.append(number)

    for i in range(t):
        pali.append(next_palindrome(numbers[i]))

    print(pali)




