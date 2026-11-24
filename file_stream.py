# Opening Learning_Outcomes_PCAP-31-03.md in read mode, returning it as a file object:

stream = open("Learning_Outcomes_PCAP-31-03.md", "rt", encoding = "utf-8")

print(stream.read()) # printing the content of the file

#====================

from os import strerror

try:
    cnt = 0
    s = open('Learning_Outcomes_PCAP-31-03.md', "rt", encoding = "utf-8")
    ch = s.read(1)
    while ch != '':
        print(ch, end='')
        cnt += 1
        ch = s.read(1)
    s.close()
    print("\n\nCharacters in file:", cnt)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))

#====================

# Checking the encoding (BOM) of a file before reading it

import codecs


def detect_encoding(filename):
    # Read raw bytes before choosing how to decode the text.
    with open("Learning_Outcomes_PCAP-31-03.md", "rb") as file:
        header = file.read(4)

    # Check UTF-32 first: its little-endian BOM starts
    # with the same two bytes as the UTF-16 little-endian BOM.
    if header.startswith((codecs.BOM_UTF32_LE, codecs.BOM_UTF32_BE)):
        return "utf-32"

    if header.startswith((codecs.BOM_UTF16_LE, codecs.BOM_UTF16_BE)):
        return "utf-16"

    if header.startswith(codecs.BOM_UTF8):
        return "utf-8-sig"

    # No BOM: assume UTF-8.
    return "utf-8"


filename = "Learning_Outcomes_PCAP-31-03.md"
encoding = detect_encoding(filename)

with open(filename, encoding=encoding) as file:
    text = file.read()

print("Encoding selected:", encoding)
print("Character count:", len(text))


#====================

# Reading whole file at once and printing it to the console:
# Not recommended for large files, as it may consume a lot of memory or crash the program.
#
from os import strerror

try:
    cnt = 0
    s = open('Learning_Outcomes_PCAP-31-03.md', "rt", encoding = "utf-8")
    content = s.read()
    for ch in content:
        print(ch, end='')
        cnt += 1
    s.close()
    print("\n\nCharacters in file:", cnt)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))


#====================

# using readlines() method to read the file line by line and print it to the console:

from os import strerror

try:
    ccnt = lcnt = 0
    s = open('Learning_Outcomes_PCAP-31-03.md', 'rt', encoding = "utf-8")
    lines = s.readlines(20)
    while len(lines) != 0:
        for line in lines:
            lcnt += 1
            for ch in line:
                print(ch, end='')
                ccnt += 1
        lines = s.readlines(10)
    s.close()
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))


#====================

# reading the file line by line using a for loop and printing it to the console:

from os import strerror

try:
	ccnt = lcnt = 0
	for line in open('Learning_Outcomes_PCAP-31-03.md', 'rt', encoding = "utf-8"):
		lcnt += 1
		for ch in line:
			print(ch, end='')
			ccnt += 1
	print("\n\nCharacters in file:", ccnt)
	print("Lines in file:     ", lcnt)
except IOError as e:
	print("I/O error occurred: ", strerror(e.errno))

#====================

# Writing to a file (creating a new file and writing to it):
# writes characters one by one to the file, using the write() method of the file object.

from os import strerror

try:
	fo = open('newtext.txt', 'wt') # A new file (newtext.txt) is created.
	for i in range(10):
		s = "line #" + str(i+1) + "\n"
		for ch in s:
			fo.write(ch)
	fo.close()
except IOError as e:
	print("I/O error occurred: ", strerror(e.errno))

#====================

# Writing to a file (creating a new file and writing to it) using the write() method of the file object:
# writes whole lines to the file, using the write() method of the file object.

from os import strerror

try:
    fo = open('newtext.txt', 'wt')
    for i in range(10):
        fo.write("line #" + str(i+1) + "\n")
    fo.close()
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))


#====================


# Writing to a file (creating a new file and writing to it) using the 'x' mode:
# using the 'x' mode will raise a FileExistsError if the file already exists, preventing overwriting.

try:
    with open('newtext.txt', 'x', encoding='utf-8') as fo:
        for i in range(10):
            fo.write(f"new line #{i + 1}\n")
except FileExistsError:
    print("The file already exists; choose another filename.")
except OSError as e:
    print("I/O error occurred:", e)

#====================

