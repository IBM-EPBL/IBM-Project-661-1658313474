def prime(n):
    number = 2
    while (number <= n):
        count = 0
        if (number > 1):
            for i in range(1, number+1):
                if (number % i == 0):
                    count = count+1
        if (count == 2):
            print(number)
        number = number+1


n = int(input())
prime(n)
