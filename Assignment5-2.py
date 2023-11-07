import math
n = int(input("Enter the lenght: "))
m = int(input("Enter the widgh: "))

for i in range(n):
   for j in range(m):

      if (i + j) %2 ==0:
         print("#", end= "")
      else:
         print("*", end= "")
   print()
