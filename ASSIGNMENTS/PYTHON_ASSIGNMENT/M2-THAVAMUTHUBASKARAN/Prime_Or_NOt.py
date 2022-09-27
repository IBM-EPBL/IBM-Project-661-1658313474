def is_prime(number):
    count = 0
    if (number > 1):
        for i in range(1, number+1):
            if (number % i == 0):
                count = count+1
    if (count == 2):
        print("Prime")
    else:
        print("Not Prime")


number = int(input())
is_prime(number)
