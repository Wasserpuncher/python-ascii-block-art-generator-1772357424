import unittest
from main import generate_ascii_art, ASCII_CHARS, CHAR_SEPARATOR

class TestAsciiArtGenerator(unittest.TestCase):
    """
    Unit tests for the ASCII Art Generator functions in main.py.
    """

    def test_generate_ascii_art_empty_string(self):
        """
        Test that an empty string input returns an empty string output.
        """
        self.assertEqual(generate_ascii_art(""), "")

    def test_generate_ascii_art_single_char(self):
        """
        Test generation for a single character (e.g., 'A').
        """
        expected_art = "\n".join(ASCII_CHARS['A'])
        self.assertEqual(generate_ascii_art("A"), expected_art)

    def test_generate_ascii_art_multiple_chars(self):
        """
        Test generation for multiple characters (e.g., 'HI').
        """
        char_h_art = ASCII_CHARS['H']
        char_i_art = ASCII_CHARS['I']
        
        expected_lines = []
        for i in range(len(char_h_art)):
            expected_lines.append(char_h_art[i] + CHAR_SEPARATOR + char_i_art[i])
        
        self.assertEqual(generate_ascii_art("HI"), "\n".join(expected_lines))

    def test_generate_ascii_art_unsupported_char(self):
        """
        Test generation with an unsupported character (e.g., '!').
        """
        unsupported_art = ASCII_CHARS['UNSUPPORTED']
        expected_art = "\n".join(unsupported_art)
        self.assertEqual(generate_ascii_art("!"), expected_art)

    def test_generate_ascii_art_mixed_case(self):
        """
        Test generation with mixed-case input (should convert to uppercase).
        """
        char_a_art = ASCII_CHARS['A']
        expected_art = "\n".join(char_a_art)
        self.assertEqual(generate_ascii_art("a"), expected_art)

    def test_generate_ascii_art_with_numbers_and_spaces(self):
        """
        Test generation with numbers and spaces.
        """
        text = "HI 1"
        char_h_art = ASCII_CHARS['H']
        char_i_art = ASCII_CHARS['I']
        char_space_art = ASCII_CHARS[' ']
        char_1_art = ASCII_CHARS['1']
        
        expected_lines = []
        for i in range(len(char_h_art)):
            line = char_h_art[i] + CHAR_SEPARATOR + char_i_art[i] + CHAR_SEPARATOR + char_space_art[i] + CHAR_SEPARATOR + char_1_art[i]
            expected_lines.append(line)
        
        self.assertEqual(generate_ascii_art(text), "\n".join(expected_lines))

    def test_generate_ascii_art_type_error(self):
        """
        Test that non-string input raises a TypeError.
        """
        with self.assertRaises(TypeError):
            generate_ascii_art(123)
        with self.assertRaises(TypeError):
            generate_ascii_art(None)
        with self.assertRaises(TypeError):
            generate_ascii_art(['A'])

if __name__ == '__main__':
    unittest.main()
