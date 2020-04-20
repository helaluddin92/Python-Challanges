# Guessing Game Challange Solution
# Use While Loop To Solve the problem

# The Challange:
"""
Write the program that picks a random integer for 1 to 100, and has players gueess the numbers. The rules are:
    1.If a player guess less than 1 and greater than 100, say "OUT OF BOUNDS".
    2.On player's first run if their guess is 
        ->Within 10 of the number return "WARM!".
        ->Further than 10 away number return "COLD!".
    3.On all subsequent terms if a guess is 
        ->closer to the number than the previous guess, return "WARMER!".
        ->further to the number than the previous guess, return "COLDER!".
    4.When the player guess equal to the number, tell them they have guess correctly and how many guess it took!
"""


# Solution:

# first pick a random integer from 1 to 100 using the random module and assign it to a variable
import random
num = random.randint(1, 100)

# print and introduction to the game and explain the rules
print("Welcome to the guess me!")
print("I'm thinking of a number between 1 to 100")
print("If your guess is more than 10 away from my number than I'll tell you COLD!")
print("If your guess is within 10 in my number than I'll tell you WARM!")
print("If your guess is further than your most recent guess than I'll say you're getting COLDER!")
print("If your guess is closer than your most recent guess than I'll say you're getting WARMER!")

# Create a list to store guess
# Hints: Zero is a good placeholder value. It's useful because it evaluates to False.

guesses = [0]

# Write a while loop that compares the players guess to our number
while True:
    # Input placeholder takes the player guess
    guess = int(
        input("I'm thinking of a number between 1 to 100. \nWhat is your guess? "))

    if guess < 1 or guess > 100:
        print("Out of Bounds. Please try again!")
        continue
    # Here we compare the player guess to the number
    if guess == num:
        print(
            f"Congratulations, you guess it in only {len(guesses)} attempts!")
        break

    # if guess is incorrect add guess to the list
    guesses.append(guess)

    # when testing the first guess, guesses[-2]==0, which evaluates to False
    # and brings us down to the second section

    if guesses[-2]:
        if abs(num-guess) < abs(num-guesses[-2]):
            print('WARMER!')
        else:
            print('COLDER!')

    else:
        if abs(num-guess) <= 10:
            print('WARM!')
        else:
            print('COLD!')
