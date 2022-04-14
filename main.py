"""
Read and Write a File in Python
"""

# Need close the file
file = open("my_file.txt")
print(file.read())
file.close()

def readFile(file_name):
    # No need to close the file
    try:
        with open(file_name) as my_file:
            print(my_file.read())
    except:
        print(f"Not able to find file \"{file_name}\"")

# Write override content of file
with open("my_file2.txt", mode="w") as file:
    file.write("new line here")

readFile("my_file2.txt")
print("")

# Write append content a file
with open("my_file2.txt", mode="a") as file:
    file.write("\nappend 2nd line here")

readFile("my_file2.txt")
print("")

readFile("missing_file.txt")