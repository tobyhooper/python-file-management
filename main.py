import string

# Ask the user for their choice
option = input(
    "Enter 1 to print the entire line,\n2 to print the first and last letters only,\nor 3 to store words in a list: ")

# Convert the input to an integer
option = int(option)

# Initialize an empty list to store words if option 3 is chosen
words_list = []

alphabet = lowercase_alphabet = list(string.ascii_lowercase)
alphabet.extend(list(string.ascii_uppercase))

# Open the file for reading
with open("mytextfile.txt", "r") as myfile:
    # Process the file line by line for Option 1 and Option 2
    if option == 1:
        # Option 1: Print the entire file
        myfile.seek(0)  # Reset the file pointer to the start
        print(myfile.read())  # Print the entire file

    if option == 2:
        # Option 2: Print the first and last letters of each line
        myfile.seek(0)  # Reset the file pointer to the start
        lines = myfile.readlines()  # Read all lines at once
        for line in lines:
            stripped_line = line.strip()  # Remove leading/trailing whitespaces
            if stripped_line:  # If the line is not empty
                first_letter = stripped_line[0]  # First letter
                last_letter = stripped_line[-1]  # Last letter
                if last_letter not in alphabet:
                    last_letter = stripped_line[-1-1]
                print(f"First letter: {first_letter}, Last letter: {last_letter}")
            else:
                print("Empty line")

    if option == 3:
        #BROKEN
        file = str(myfile.read())
        words = []
        words = file.split(file)
        for word in words:
            for char in range(len(word)):
                if char not in alphabet:
                    char.remove(char)
        print(words)


    else:
        print("Invalid option. Please enter 1, 2, or 3.")