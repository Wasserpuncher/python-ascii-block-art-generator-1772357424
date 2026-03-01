#!/usr/bin/env python3

"""
main.py

This script provides an ASCII Art Generator that converts text into block letters.
It includes character mappings, functions for generating art, and a main execution loop.
"""

# Define ASCII characters as lists of strings (5 lines each, consistent width).
# Using a fixed width of 5 characters for each block for visual consistency.
_A = [" AAA ", "A   A", "AAAAA", "A   A", "A   A"]
_B = ["BBBB ", "B   B", "BBBB ", "B   B", "BBBB "]
_C = [" CCCC", "C    ", "C    ", "C    ", " CCCC"]
_D = ["DDDD ", "D   D", "D   D", "D   D", "DDDD "]
_E = ["EEEEE", "E    ", "EEEEE", "E    ", "EEEEE"]
_F = ["EEEEE", "E    ", "EEEEE", "E    ", "E    "]
_G = [" GGGG", "G    ", "G GG ", "G   G", " GGGG"]
_H = ["H   H", "H   H", "HHHHH", "H   H", "H   H"]
_I = ["IIIII", "  I  ", "  I  ", "  I  ", "IIIII"]
_J = ["JJJJJ", "  J  ", "  J  ", "J J  ", " JJ  "]
_K = ["K  K ", "K K  ", "KK   ", "K K  ", "K  K "]
_L = ["L    ", "L    ", "L    ", "L    ", "LLLLL"]
_M = ["M   M", "MM MM", "M M M", "M   M", "M   M"]
_N = ["N   N", "NN  N", "N N N", "N  NN", "N   N"]
_O = [" OOO ", "O   O", "O   O", "O   O", " OOO "]
_P = ["PPPP ", "P   P", "PPPP ", "P    ", "P    "]
_Q = [" QQQ ", "Q   Q", "Q Q Q", "Q  Q ", " QQQQ"]
_R = ["RRRR ", "R   R", "RRRR ", "R R  ", "R  RR"]
_S = [" SSS ", "S    ", " SSS ", "    S", " SSS "]
_T = ["TTTTT", "  T  ", "  T  ", "  T  ", "  T  "]
_U = ["U   U", "U   U", "U   U", "U   U", " UUU "]
_V = ["V   V", "V   V", "V   V", " V V ", "  V  "]
_W = ["W   W", "W   W", "W W W", "WW WW", "W   W"]
_X = ["X   X", " X X ", "  X  ", " X X ", "X   X"]
_Y = ["Y   Y", " Y Y ", "  Y  ", "  Y  ", "  Y  "]
_Z = ["ZZZZZ", "   Z ", "  Z  ", " Z   ", "ZZZZZ"]

_0 = [" 000 ", "0   0", "0 0 0", "0   0", " 000 "]
_1 = ["  1  ", " 11  ", "  1  ", "  1  ", " 111 "]
_2 = [" 222 ", "2   2", "  22 ", " 2   ", "22222"]
_3 = [" 333 ", "3   3", "  33 ", "3   3", " 333 "]
_4 = ["4   4", "4   4", "44444", "    4", "    4"]
_5 = ["55555", "5    ", "5555 ", "    5", "5555 "]
_6 = [" 666 ", "6    ", "6666 ", "6   6", " 666 "]
_7 = ["77777", "    7", "   7 ", "  7  ", " 7   "]
_8 = [" 888 ", "8   8", " 888 ", "8   8", " 888 "]
_9 = [" 999 ", "9   9", " 9999", "    9", " 999 "]

_SPACE = ["     ", "     ", "     ", "     ", "     "]
_UNSUPPORTED = [" ??? ", "?   ?", "  ?  ", "?   ?", " ??? "] # Placeholder for unsupported characters

ASCII_CHARS = {
    'A': _A, 'B': _B, 'C': _C, 'D': _D, 'E': _E, 'F': _F, 'G': _G, 'H': _H, 'I': _I,
    'J': _J, 'K': _K, 'L': _L, 'M': _M, 'N': _N, 'O': _O, 'P': _P, 'Q': _Q, 'R': _R,
    'S': _S, 'T': _T, 'U': _U, 'V': _V, 'W': _W, 'X': _X, 'Y': _Y, 'Z': _Z,
    '0': _0, '1': _1, '2': _2, '3': _3, '4': _4, '5': _5, '6': _6, '7': _7, '8': _8, '9': _9,
    ' ': _SPACE,
    'UNSUPPORTED': _UNSUPPORTED
}

CHAR_SEPARATOR = "  " # Separator between ASCII art blocks of characters

def get_char_art(char: str) -> list[str]:
    """
    Retrieves the ASCII art representation for a single character.

    Converts the input character to uppercase to match the keys in ASCII_CHARS.
    If the character is not found, it returns the 'UNSUPPORTED' character art.

    Args:
        char: The single character for which to retrieve ASCII art.

    Returns:
        A list of strings, where each string is a line of the character's ASCII art.
    """
    # Convert to uppercase to handle case-insensitivity for letters
    char = char.upper()
    return ASCII_CHARS.get(char, ASCII_CHARS['UNSUPPORTED'])

def generate_ascii_art(text: str) -> str:
    """
    Generates ASCII art for the given text.

    Converts input text into large block letters using predefined ASCII character maps.
    Each character's ASCII representation is stacked horizontally, with a separator.

    Args:
        text: The input string to convert to ASCII art.

    Returns:
        A multi-line string representing the ASCII art of the input text.

    Raises:
        TypeError: If the input text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("Input 'text' must be a string.")
    if not text:
        return ""

    # Determine the height of the ASCII art blocks.
    # Using 'A' as a reference, assuming all character arts have the same height.
    if not ASCII_CHARS or not ASCII_CHARS.get('A'):
        # Fallback if ASCII_CHARS is empty or 'A' is not defined (unlikely given the setup).
        return ""
    
    lines_per_char = len(ASCII_CHARS['A'])
    if lines_per_char == 0:
        return ""

    # Initialize result lines, one for each row of the ASCII art output.
    result_lines = [""] * lines_per_char

    for char_index, char in enumerate(text):
        char_art = get_char_art(char)
        for i in range(lines_per_char):
            # Concatenate the current character's art line with the corresponding result line.
            result_lines[i] += char_art[i]
            # Add separator only if it's not the last character.
            if char_index < len(text) - 1:
                result_lines[i] += CHAR_SEPARATOR

    return "\n".join(result_lines)

def main():
    """
    Main function to run the ASCII art generator application.

    Prompts the user for text input, generates ASCII art, and prints it to the console.
    Includes error handling for invalid input types and general exceptions.
    """
    print("Welcome to the ASCII Art Generator!")
    print("Enter text to convert into block letters.")
    print("Supported characters: A-Z, 0-9, Space.")
    print("Unsupported characters will be shown as '???'.")
    print("""""""""""""""""""""""""""""""""""""""""""""""""""""
Example:
PPPP   Y   Y  TTTTT  H   H  OOOOO  N   N
P   P   Y Y     T    H   H  O   O  NN  N
PPPP     Y      T    HHHHH  O   O  N N N
P        Y      T    H   H  O   O  N  NN
P        Y      T    H   H  OOOOO  N   N
"""""""""""""""""""""""""""""""""""""""""""""""""""""
    try:
        user_input = input("\nEnter your text: ")
        
        ascii_output = generate_ascii_art(user_input)
        
        print("\n" + "="*80)
        print("Generated ASCII Art:")
        print(ascii_output)
        print("="*80 + "\n")
        
    except TypeError as e:
        print(f"Error: Invalid input. {e}")
        print("Please ensure you enter text (a string).")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
