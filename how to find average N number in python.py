# How to find average N number in python

num = int(input("How many number? "))
total_sum = 0

for n in range(num):
    number = int(input("Enter any number "))
    total_sum += number

avg = total_sum/num

print(avg)
