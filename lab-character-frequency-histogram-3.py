filename = input("Enter the input filename: ")
counts = {}

try:
    with open(filename, "r", encoding="utf-8-sig") as file:
        for line in file:
            for character in line:
                if "A" <= character <= "Z" or "a" <= character <= "z":
                    letter = character.lower()
                    counts[letter] = counts.get(letter, 0) + 1
except OSError as error:
    print("Could not read the file:", error)
except UnicodeError as error:
    print("Could not decode the file as UTF-8:", error)
else:
    for letter in sorted(counts):
        print(f"{letter} -> {counts[letter]}")
