def write_input():
# Open myfile.txt (append).
    with open("myfile.txt", "a") as output_file:
# Ask for user's input and store it as input_line.
        user_input = input("Enter line: ")
# Write the user's input to myfile.txt.
        output_file.write(user_input + "\n")

write_input()

# Ask the user if they have more lines to enter.
# If yes, repeat the procedure.
# If no, the program is done.
