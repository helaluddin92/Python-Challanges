# Write a function that returns the number of prime numbers that exist upto including a given number.


def prime_number(num):
    prime = [2]
    x = 3
    if num <= 2:
        return 0
    while x <= num:
        for y in prime:
            if x % y == 0:
                x += 2
                break
        else:
            prime.append(x)
            x += 2
    return prime


result = prime_number(100)
print(result)
