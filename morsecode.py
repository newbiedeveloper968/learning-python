import sys

morse_code_dict: dict[str, str] = {
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


def morse_to_standard(code) -> str:
    words: list = code.split(" / ")
    standard_form = []
    for word in words:
        letters: list = word.split(" ")
        code_to_letter = [morse_code_dict.get(letter, "?") for letter in letters]
        standard_form.append("".join(code_to_letter))
    return " ".join(standard_form)


invert_dict: dict = {value: key for key, value in morse_code_dict.items()}


def standard_to_morse(standard) -> str:
    words: list = standard.upper().split(" ")
    morse_form = []
    for word in words:
        letter_to_code: list = [invert_dict.get(letter, "?") for letter in word]
        morse_form.append(" ".join(letter_to_code))
    return " / ".join(morse_form)


while True:
    try:
        option: str = input(
            """1. Morse code to standard
2. Standard to morse code
Option: """
        )
        if int(option) == 1:
            user_input: str = input("Morse code: ")
            print(morse_to_standard(user_input))
            break
        elif int(option) == 2:
            user_input: str = input("Standard text: ")
            print(standard_to_morse(user_input))
            break
    except:
        print("Not an option!")
