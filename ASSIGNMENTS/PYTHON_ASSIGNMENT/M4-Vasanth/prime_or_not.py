def is_prime(n):
    temp = 0
    if (n > 1):
        for i in range(1, n+1):
            if (n % i == 0):
                temp = temp+1
    if (temp == 2):
        print("Prime")
    else:
        print("Not Prime")


n = int(input())
is_prime(n)
