"""
Read and Write a File in Python
"""

# Need close the file
file = open("my_file.txt")
print(file.read())
file.close()

def readFile(file_name):
    # No need to close the file
    with open(file_name) as file:
        print(file.read())


with open("my_file2.txt", mode="w") as file:
    file.write("new line here")

readFile("my_file2.txt")
print("")

with open("my_file2.txt", mode="a") as file:
    file.write("\nappend 2nd line here")

readFile("my_file2.txt")