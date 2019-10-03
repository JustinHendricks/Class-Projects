#Directions were to create a guess the number game where the user is guessing and the computer tells the user if they are getting hotter or colder
#I'm uploading because I made a similar program over the summer, and the code for it was a lot more convoluted. Using a list to track distances was a big help.

import random

i = 0 

number = random.randint(0, 100)

guess = int(input("Guess the number "))
distances = []
distances.append(abs(int(number - guess)))

while guess != number:
    if len(distances) > 1:
        if distances[i] < distances[i - 1]:
            print("You are getting warmer")
        elif distances[i] > distances[i - 1]:
            print("You are getting colder")
    if distances[i] < 10:
        print("You are red hot")
    elif distances[i] >= 10 and distances[i] <= 20:
        print("You are warm")
    elif distances[i] > 20:
        print("You are cold")
    guess = int(input("Guess the number "))
    distances.append(abs(int(number - guess)))
    i += 1

print("You are correct! You got it after " + str(len(distances)) , "guesses.")
