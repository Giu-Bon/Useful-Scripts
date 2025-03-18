# Define the path to the NATO and German alphabet .txt files
file_path_nato = 'nato_alphabet.txt'
file_path_german = 'german_alphabet.txt'

# Function to read and parse an alphabet from a file
def load_alphabet(file_path):
    alphabet = {}
    with open(file_path, 'r') as file:
        for line in file:
            # Remove any surrounding whitespace and commas
            line = line.strip().strip(',')
            # Split the line into key-value pairs
            if line:
                key, value = line.split(':')
                # Remove any extra quotes and whitespace
                key = key.strip().strip("'")
                value = value.strip().strip("'")
                alphabet[key.upper()] = value
    return alphabet

# Load the NATO and German alphabets from the .txt files
nato_alphabet = load_alphabet(file_path_nato)
german_alphabet = load_alphabet(file_path_german)

# Take input from the user
word = input("Enter a word: ")

# Convert the word to uppercase for matching keys in the dictionary
word_upper = word.upper()

# Function to format the output table row for each letter
def format_row(letter, german_word, nato_word, original_letter):
    return f"|   {letter:<1}       |-|       {german_word:<10}  |-|       {nato_word:<10}  |-|     {original_letter:<1}  |"

# Prepare the output
header = (
    "\n   |------------------------------------------------------------------|\n"
    "   |   Letter  |-|       German      |-|       English     |-|        |\n"
    "   |------------------------------------------------------------------|"
)

footer = (
    "   |------------------------------------------------------------------|\n"
)

# Generate the rows for the word
rows = []
for i, letter in enumerate(word_upper):
    german_word = german_alphabet.get(letter, "N/A")
    nato_word = nato_alphabet.get(letter, "N/A")
    original_letter = word[i]
    rows.append(format_row(letter, german_word, nato_word, original_letter))

# Combine everything into the final output
output = header + "\n" + "\n".join(rows) + "\n" + footer

# Print the final output
print(output)
