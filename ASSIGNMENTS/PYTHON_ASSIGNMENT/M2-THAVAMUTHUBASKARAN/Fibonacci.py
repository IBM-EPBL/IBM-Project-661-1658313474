number = int(input())
number1, number2 = 0, 1
count = 0
if number <= 0:
    print("Please enter a positive integer")
elif number == 1:
    print("Fibonacci sequence upto", number, ":")
    print(number1)
else:
    print("Fibonacci sequence:")
    while count < number:
        print(number1)
        nth = number1 + number2
        number1 = number2
        number2 = nth
        count += 1
