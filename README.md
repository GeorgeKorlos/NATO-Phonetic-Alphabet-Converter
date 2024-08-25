# NATO Phonetic Alphabet Converter: A Python Script Using Pandas

This repository contains a Python script that reads the NATO phonetic alphabet from a CSV file and converts a user-provided word into its corresponding NATO phonetic code. This project is a practical example for those learning about file handling, dictionary creation, and list comprehensions in Python, as well as using the Pandas library.

## Description

The script performs the following operations:

1. **Reads data from a CSV file:**
    - The script uses Pandas to read `nato_phonetic_alphabet.csv`, which contains the NATO phonetic alphabet.

2. **Creates a dictionary:**
    - The data from the CSV file is processed into a dictionary where each letter of the alphabet is mapped to its corresponding NATO phonetic code.

3. **Processes user input:**
    - The user is prompted to enter a word. The script converts this word into its NATO phonetic equivalent using the dictionary created earlier.

4. **Outputs the phonetic code:**
    - The script prints a list of NATO phonetic codes corresponding to each letter of the user's input.

### How It Works

1. **CSV File Reading:**
    - The script reads the CSV file `nato_phonetic_alphabet.csv` into a Pandas DataFrame.

2. **Dictionary Creation:**
    - The script iterates over the DataFrame to create a dictionary where each key is a letter, and the corresponding value is the NATO phonetic code.

3. **User Input Handling:**
    - The user inputs a word, and the script converts each letter to uppercase and looks it up in the dictionary to get the corresponding phonetic code.

4. **Output:**
    - The final output is a list of NATO phonetic codes representing the input word.

### Example

**CSV File Content (nato_phonetic_alphabet.csv):**

| letter | code   |
|--------|--------|
| A      | Alpha  |
| B      | Bravo  |
| C      | Charlie|
| ...    | ...    |

**Input:**

```bash
Enter a word: Hello
