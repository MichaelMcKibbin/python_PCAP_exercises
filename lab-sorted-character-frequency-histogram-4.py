filename = input("Enter the input filename: ")
counts = {}

try:
    with open(filename, "r", encoding="utf-8-sig") as file:
        for line in file:
            for character in line:
                if "A" <= character <= "Z" or "a" <= character <= "z":
                    letter = character.lower()
                    counts[letter] = counts.get(letter, 0) + 1

    sorted_counts = sorted(
        counts.items(),
        key=lambda item: (-item[1], item[0]) # sort by frequency descending, then by letter ascending

        # to sort only by frequency descending, you can use:
        # key=lambda item: item[1]
        # reverse=True
    )

    output_filename = filename + ".hist"

    with open(output_filename, "w", encoding="utf-8") as file:
        for letter, count in sorted_counts:
            file.write(f"{letter} -> {count}\n")

    print("Histogram saved to:", output_filename)

except OSError as error:
    print("File error:", error)

except UnicodeError as error:
    print("Encoding error:", error)