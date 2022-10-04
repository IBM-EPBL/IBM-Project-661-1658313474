def prime(start, end):
    while (start <= end):
        count = 0
        if (start > 1):
            for i in range(1, start+1):
                if (start % i == 0):
                    count = count+1
        if (count == 2):
            print(start)
        start += 1


start = int(input())
end = int(input())
prime(start, end)
