num = int(input("Son kiriting: "))
for i in range(2, num):
    count = 0
    for j in range(2, i//2 + 1):
        if i % j == 0:
            count += 1
    if count == 0:
        print(i)
