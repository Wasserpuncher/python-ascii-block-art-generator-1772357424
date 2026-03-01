# Python ASCII Block Art Generator

## Project Description
This is a high-quality Python project designed to convert standard text input into visually appealing block letter ASCII art. It's built with professionalism in mind, incorporating advanced concepts such as robust error handling, comprehensive docstrings, and a modular design. The generator supports uppercase letters (A-Z), numbers (0-9), and spaces, gracefully handling unsupported characters with a distinctive placeholder.

## Features
*   **Text to ASCII Art Conversion**: Transforms any given string into block-style ASCII art.
*   **Wide Character Support**: Includes mappings for all uppercase English letters (A-Z), numbers (0-9), and spaces.
*   **Error Handling**: Robust input validation to ensure stability and user-friendliness, catching `TypeError` for invalid input types.
*   **Graceful Unsupported Character Handling**: Displays a clear "???" block for any character not explicitly mapped, preventing program crashes and informing the user.
*   **Modular Design**: Clear separation of concerns with functions for retrieving character art and generating the full ASCII output.
*   **Docstrings**: Comprehensive documentation for all functions, explaining their purpose, arguments, and return values.
*   **Unit Tests**: A dedicated test suite (`test_main.py`) to ensure the core logic functions as expected.

## Installation

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/python-ascii-block-art-generator.git
    cd python-ascii-block-art-generator
    ```

2.  **Create a Virtual Environment (Optional but Recommended)**:
    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies**:
    This project uses only standard Python libraries, so there are no external dependencies to install. However, if you were to add any, you would install them like this:
    ```bash
    pip install -r requirements.txt
    ```
    (Note: `requirements.txt` is intentionally empty for this project as no external libraries are used).

## Usage

1.  **Run the Main Application**:
    Execute the `main.py` file from your terminal.
    ```bash
    python main.py
    ```

2.  **Enter Your Text**:
    The program will prompt you to enter the text you wish to convert.
    ```
    Welcome to the ASCII Art Generator!
    Enter text to convert into block letters.
    Supported characters: A-Z, 0-9, Space.
    Unsupported characters will be shown as '???'.
    Enter your text: HELLO WORLD
    ```

3.  **View the ASCII Art Output**:
    The generated ASCII art will be printed directly to your console.

### Example Output

```
Enter your text: PYTHON
================================================================================
Generated ASCII Art:
PPPP   Y   Y  TTTTT  H   H  OOOOO  N   N
P   P   Y Y     T    H   H  O   O  NN  N
PPPP     Y      T    HHHHH  O   O  N N N
P        Y      T    H   H  O   O  N  NN
P        Y      T    H   H  OOOOO  N   N
================================================================================
```

## Running Tests

To ensure everything is working correctly, you can run the provided unit tests:

1.  **Navigate to the project directory** (if not already there).
2.  **Execute the test file**:
    ```bash
    python test_main.py
    ```
    You should see output indicating that all tests have passed.

## Error Handling

The `generate_ascii_art` function explicitly raises a `TypeError` if the input is not a string, providing clear feedback to the developer or user. The `main` function wraps its execution in a `try-except` block to gracefully handle this and other potential unexpected errors, printing informative messages to the console.

## Contributing
While this is a standalone project, contributions such as expanding the character set, adding new font styles, or improving performance would be welcome in a real-world scenario.
