# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
PLACE_HOLDER = "[name]"
invitees = []
with open("./Input/Names/invited_names.txt", mode="r") as names_file:
    names = names_file.readlines()
for name in names:
    invitees.append(name.strip())
with open("./Input/Letters/starting_letter.txt", mode="r") as letter_file:
    letter_content = letter_file.read()
for invitee in invitees:
    personal_letter = letter_content.replace(PLACE_HOLDER,invitee)
    with open(f"./Output/ReadyToSend/letter_for_{invitee}.txt", mode="w") as completed_letter:
        completed_letter.write(personal_letter)

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
