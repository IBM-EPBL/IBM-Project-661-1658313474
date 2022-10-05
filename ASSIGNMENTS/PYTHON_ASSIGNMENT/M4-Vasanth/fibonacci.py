m = int(input())
m1, m2 = 0, 1
count = 0
if m <= 0:
    print("Please enter a positive integer")
elif m == 1:
    print("Fibonacci sequence upto", m, ":")
    print(m1)
else:
    print("Fibonacci sequence:")
    while count < m:
        print(m1)
        nth = m1 + m2
        m1 = m2
        m2 = nth
        count += 1
