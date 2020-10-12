# Time is used for stopping the program for a few seconds after each morse code letter
import time

# playsound is a library for playing sound files
from playsound import playsound

# Create a dictionary linking each letter to the correct morse code combination
codes = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    ' ': ' '
}
# When you said take text as input, I didnt know what you ment so I did both
try:
    with open("output.txt") as f:
        # take the file contents and clean it up
        inputString = f.readline().strip().upper()
    if len(inputString) == 0:
        print("output text file empty")
        inputString = input("Enter message\n:").upper()
except:
    # Take user input and convert to uppercase
    print("output file not found")
    inputString = input("Enter message\n:").upper()

# This was an easter egg. During competition it played an audio file saying "noice"
#try:
    #if ((1 + 1 + 1 + 1 + 1) * (1 + 1 + 1 + 1 + 1 + 1 + 1) * (1 + 1)) - 1 == int(inputString):
        #playsound("Helpful.wav")
#except:
    #print("Conversion starting")

# If the inputted string contains just . and -, the input must be morse code
temp = inputString.replace(" ", "")
if temp.count(".") + temp.count("-") == len(temp):
    # "Flip" the dictionary. Each letter and code is flipped as morsecode will need to be translated to letters
    codes = {code: letter for letter, code in codes.items()}
    inputList = inputString.split()

# Create a list of the user input, including spaces. The last element will also be a space, so remove it
else:
    inputList = [x for y in inputString.split() for x in (y, ' ')][:-1]

message = ""
try:
    for i in inputList:
        # if the dictionary is set for english to morse code
        if codes.get('A') is not None:
            code = list(i)
            for j in code:
                j = codes.get(j)
                # concatenate each morse code to the rest
                message += j + ' '
                # Go through each character, playing the necessary sound file if dash or dot
                for k in list(j):
                    if k == '-':
                        playsound("Dash.wav")
                    elif k == '.':
                        playsound("Dot.wav")

                # Wait one second between letters
                time.sleep(0.50)
        else:
            # If dictionary is set morse code to english, concatonate the letters translated
            message += codes.get(i) + ' '
    print(message)
    with open("output.txt", "w") as f:
        f.write(message)
# If any error comes up, try and display a useful error message
except:
    print("An error has occurred")
    if codes.get('A') is None:
        print("Please make sure you type a space between every morse code letter")
