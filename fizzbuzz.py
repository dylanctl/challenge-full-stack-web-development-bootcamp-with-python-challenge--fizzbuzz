num = input("Enter a number: ")
num = int(num)

if num%15==0:
    print("FizzBuzz")
elif num%3==0:
    print("Fizz")
elif num%5==0:
    print("Buzz")
else:
    print(num)