# Introduction:
print("\033[47m")
print("\033[1;91m/ᐠ. .ᐟ\ฅ".center(70))
print("\033[0m")
print("\033[1;33mWRITE YOUR LIFE\033[0;36m".center(80))
quote = "\x1B[3m" + "live one line at a time.." + "\x1B[0m"
print(quote.center(78))
print("\033[43m")
print("⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆"* 5)
print("\nPlease enter a line that is anything about life.\nI will compile it in a file named as mylife for you\nLive your life!\n")
print("⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆"* 5)
print("\033[0m")

with open("mylife.txt", "a") as output_file:
        import pyfiglet
        result = pyfiglet.figlet_format("My Life...", font = "digital" )
        output_file.write(result)   

def write_input():
# Open myfile.txt (append).
    with open("mylife.txt", "a") as output_file:
        
# Ask for user's input and store it as input_line.
        user_input = input("\n\033[47mEnter line: \033[0m")
# Write the user's input to myfile.txt.
        output_file.write(user_input + "\n")

write_input()

while True:
# Ask the user if they have more lines to enter.
        user_decision = input("\n\033[1;35mAre there more lines y/n? ")
# If yes, repeat the procedure.
        if user_decision == "y":
                write_input()
# If no, the program is done.
        elif user_decision == "n":
                print("\n\033[4;33mYour inputs are saved in the file named \033[1;32mmylife\033[4;33m. You can check it in your directory.\n\033[0m")
                print("\033[47mThank you for sharing bits of your life with me.")
                print("    ᐢ⑅ᐢ".center(40))
                print("꒰ ˶• ༝ •˶꒱".center(40))
                print("./づ~ ♡".center(40))
                break
        else:
              print("\033[1;31mPlease type in only y or n.")
              continue