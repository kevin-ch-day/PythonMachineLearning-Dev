import numpy as np

# test static data
#dice_rolls = np.array([3, 1, 5, 2, 5, 1, 1, 5, 1, 4, 2, 1, 4, 5, 3, 4, 5, 2, 4, 2, 6, 6, 3, 6, 2, 3, 5, 6, 5])
#print(len(dice_rolls))

NUMBER_DICE_ROLLS = 100000
MIN_DICE_RESULT = 2
MAX_DICE_RESULT = 12

def displayRollResults(resultsList):
    print("Dice Roll Results ")
    print() # new line

    for index in range (2, 12): # exclusive
        print(index, ": ", len(resultsList[resultsList == index]))
    # for
    print() # new line

    for index in range (1, 12): # exclusive
        totalRolls = len(resultsList[resultsList > index])
        print("Roll Results > {x}: {y}".format(x=index, y=totalRolls))
    # for
    print() # newline
# function

dice = np.random.randint(MIN_DICE_RESULT, MAX_DICE_RESULT+1, NUMBER_DICE_ROLLS)
# print(dice)
displayRollResults(dice)
