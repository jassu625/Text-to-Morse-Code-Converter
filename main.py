TEXT_TO_MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.',
                 'D': '-..', 'E': '.', 'F': '..-.',
                 'G': '--.', 'H': '....', 'I': '..',
                 'J': '.---', 'K': '-.-', 'L': '.-..',
                 'M': '--', 'N': '-.', 'O': '---',
                 'P': '.--.', 'Q': '--.-', 'R': '.-.',
                 'S': '...', 'T': '-', 'U': '..-',
                 'V': '...-', 'W': '.--', 'X': '-..-',
                 'Y': '-.--', 'Z': '--..',

                 '0': '-----', '1': '.----', '2': '..---',
                 '3': '...--', '4': '....-', '5': '.....',
                 '6': '-....', '7': '--...', '8': '---..',
                 '9': '----.',

                 ',': '--..--', '.': '.-.-.-', '?': '..--..',
                 '/': '-..-.', '-': '-....-', '(': '-.--.',
                 ')': '-.--.-'
                 }


def get_text() -> str:
    text = input("Enter the text you want to  convert into morse code:\n")
    return text


def to_morse(text: str) -> str:
    code = ''
    for letter in text:
        if letter == " ":
            # 2 spaces implies a different word
            code = code + (" " * 2)
        else:
            code = code + TEXT_TO_MORSE.get(letter.upper()) + " "  # space between every letter
    return code


def main():
    repeat = True  # for translating multiple times
    while repeat:
        text = get_text()
        code = to_morse(text=text)
        print(code)
        ans = input("Do you want to  translate once more?( type N/n if no and Y/y if yes)\n")
        if ans.upper() == 'N':
            repeat = False
        elif ans.upper() == 'Y':
            repeat = True


# Standard boilerplate to run as a script and not as a module
if __name__ == '__main__':
    main()
