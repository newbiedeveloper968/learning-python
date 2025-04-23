import sys

morse_code_dict = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
    "-----": "0",
    ".-.-.-": ".",
    "--..--": ",",
    "..--..": "?",
    "-.-.--": "!",
    "-..-.": "/",
    "-.--.": "(",
    "-.--.-": ")",
    ".-..-.": '"',
    "-.-.-.": ";",
    "-...-": "=",
    ".-.-.": "+",
    "-....-": "-",
    "..--.-": "_",
    ".-..-.": '"',
    "...-..-": "$",
    ".--.-.": "@",
}


def morse_to_standard(code):
    words = code.split(" / ")
    decoded = []
    for word in words:
        letters = word.split(" ")
        code_to_letter = [morse_code_dict.get(letter, "") for letter in letters]
        decoded.append("".join(code_to_letter))
    return " ".join(decoded)


invert_dict = {value: key for key, value in morse_code_dict.items()}


def standard_to_morse(standard):
    words = standard.upper().split(" ")
    standard_form = []  # [.-. . --.. .-], [.- ... .... .], [-. .- .."]
    for word in words:
        letter_to_code = [invert_dict.get(letter) for letter in word]
        standard_form.append(" ".join(letter_to_code))
    return " / ".join(standard_form)


option = input(
    """Which one?
1. Morse code to standard
2. Standard to morse code\n"""
)

try:
    if int(option) == 1:
        user_input = input("Morse code: ")
        print(morse_to_standard(user_input))
    elif int(option) == 2:
        user_input = input("Standard text: ")
        print(standard_to_morse(user_input))
except:
    sys.exit("Not an option!")
