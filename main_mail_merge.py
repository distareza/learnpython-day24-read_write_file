# Challenge: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

invited_names = []

# Return all lines in the file, as a list where each line is an item in the list object:
with open("Input/Names/invited_names.txt", mode="r") as invited_files:
    invited_names = invited_files.readlines()
    print(invited_names)

email_template = None
with open("Input/Letters/starting_letter.txt", mode="r") as file_template:
    email_template = file_template.read()

for name in invited_names:
    name_trim = name.strip()
    content = email_template.replace("[name]", name_trim)
    with open(f"Output/ReadyToSend/{name_trim}.txt", mode="w") as file_to_send:
        file_to_send.write(content)

