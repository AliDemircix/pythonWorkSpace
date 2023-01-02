# Create diagram in https://app.diagrams.net
import random
wordList = ["Pilot", "Car", "Apartment", "Element"]


def selectRandomWord():
    return random.choice(wordList)


def createWordArea(word):
    areaSpace = len(word)
    area = []
    for _ in range(1, areaSpace+1):
        area.append("_")
    return area


def getLetterFromUser():
    letter = input("Make your guess with a letter \n")
    return letter


def checkUserLetter(letter, selectedWord):
    if letter in selectedWord:
        return True
    else:
        return False


def updateArea(letter, word, area):
    for index, char in enumerate(word):
        if char == letter:
            area[index] = letter
    print(area)
    return area


def startGame():
    life = 6
    notFullFilled = True
    selectedWord = selectRandomWord()
    wordArea = createWordArea(selectedWord)
    wrongLetters = []
    print(wordArea)
    while notFullFilled:
        userLetter = getLetterFromUser()
        isInclude = checkUserLetter(userLetter, selectedWord)
        if isInclude:
            updateArea(userLetter, selectedWord, wordArea)
            if "_" not in wordArea:
                notFullFilled = False
                print("You win.")
        else:
            if life == 0:
                notFullFilled = False
                print("Game Over")
                return
            life -= 1
            wrongLetters.append(userLetter)
            print(f"{life} life left. Wrong letters was {wrongLetters} ")


startGame()
