import random

a = int(input("How many number do you want? "))
n = []
for i in range(a):
    b = (random.randint(1, 200))
    if b not in n:
        n.append(b)

print(n)