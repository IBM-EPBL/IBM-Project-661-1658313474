number = int(input())
count = 0
if (number > 1):
    for i in range(1, number+1):
        if (number % i == 0):
            count = count+1
    if (count == 2):
        print("Prime")
    else:
        print("Not Prime")
else:
    print("Enter the number above 1")
