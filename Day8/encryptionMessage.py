
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

isEnd = "Y"


def createSecretMessage(action, message, shiftValue):
    cyrptText = ""
    for char in message:
        if char in letters:
            letterIndex = letters.index(char)
            if action == "encode":
                cyrptText += letters[(letterIndex+shiftValue) % 25]
            elif action == "decode":
                cyrptText += letters[(letterIndex-shiftValue) % 25]
        else:
            cyrptText += char
    print(cyrptText)


while isEnd == "Y":
    message_action = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt: \n")
    message = input("Type your secret message \n").lower()
    shift_value = int(input("Type shift value as a number \n"))

    createSecretMessage(message_action, message, shift_value)
    isEnd = input("Do you want to continue ? Y or N \n")
