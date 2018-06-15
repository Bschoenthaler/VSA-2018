# Create a program that will play the 'cows and bulls' game with the user. The game works
# like this:
#
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every
# digit that the user guessed correctly in the correct place, they have a 'cow'. For
# every digit the user guessed correctly in the wrong place is a 'bull.' Every time the
# user makes a guess, tell them how many 'cows' and 'bulls' they have. Once the user
# guesses the correct number, the game is over. Keep track of the number of guesses the
# user makes throughout the game and tell the user at the end.
#
# Say the number generated by the computer is 1038. An example interaction could look like
# this:
#
#   Welcome to the Cows and Bulls Game!
#   Enter a number:
#   >>> 1234
#   2 cows, 0 bulls
#   >>> 1256
#   1 cow, 1 bull

# Until the user guesses the number.



import random
number = str(random.randint(1000,9999)) #random 4 digit number
y = True
empty = []
empty1 = []
cows = 0
bulls = 0
while y:
    q = raw_input("Input a four digit number or 00 to exit.")
    if q == "00":
        y = False
    empty.append(q)
    empty1.append(number)
    for number in range(0,4):
        if empty == empty1:
            cows = cows + 1
            empty[q] = "%"
            empty1[number] = "$"
    for item1 in empty: