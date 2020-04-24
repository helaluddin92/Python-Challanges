# How to find average N number in python


def avg_n(num):
    total_sum = 0
    for n in range(num):
        number = int(input("Enter any number "))
        total_sum += number
    avg = total_sum / num
    return avg


result = avg_n(int(input("How many number?")))
print(result)
