# Python program to display all the prime numbers within an interval
#Adumoah Isaac 10977636


lower = 1
upper = 1000


print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

print('done')