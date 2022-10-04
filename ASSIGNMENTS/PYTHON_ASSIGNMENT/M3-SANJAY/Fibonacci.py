totalNoOfTerms = int(input())
integer1, integer2 = map(int, input().split())
count = 0
if totalNoOfTerms <= 0:
    print("Please enter a positive integer")
elif totalNoOfTerms == 1:
    print("Fibonacci sequence upto", totalNoOfTerms, ":")
    print(integer1)
else:
    print("Fibonacci sequence:")
    while count < totalNoOfTerms:
        print(integer1)
        nth = integer1 + integer2
        integer1 = integer2
        integer2 = nth
        count += 1
