def write_input():
# Open myfile.txt (append).
    with open("myfile.txt", "a") as output_file:
# Ask for user's input and store it as input_line.
        user_input = input("Enter line: ")
# Write the user's input to myfile.txt.
        output_file.write(user_input + "\n")

write_input()

while True:
# Ask the user if they have more lines to enter.
        user_decision = input("Are there more lines y/n? ")
# If yes, repeat the procedure.
        if user_decision == "y":
                write_input()
# If no, the program is done.
        elif user_decision == "n":
                print("Your inputs are saved in the file named mylife.")
                break
