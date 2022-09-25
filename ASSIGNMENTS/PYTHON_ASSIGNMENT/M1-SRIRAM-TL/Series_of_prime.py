def prime(n):
    num = 2
    while (num <= n):
        count = 0
        if (num > 1):
            for i in range(1, num+1):
                if (num % i == 0):
                    count = count+1
        if (count == 2):
            print(num)
        num = num+1


n = int(input())
prime(n)
