# stripping out the vowels from a text file:

for line in open("file-operations.md", "rt"):
    for char in line:
        if char.lower() not in "aeiouy ":
            print(char, end='')