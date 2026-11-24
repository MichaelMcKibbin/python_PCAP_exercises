from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

# read bytes from the stream:
# take care that the contents of the file will fit in the memory of the computer, otherwise the program will crash with a MemoryError exception

try:
    bf = open('file.bin', 'rb')
    data_read = bytearray(bf.read())
    bf.close()

    # print each byte in the bytearray as a hexadecimal number
    for b in data_read:
        print("\nbyte: " + hex(b), end=' ')

    # print the list of bytes read from the file
    print("\nList of bytes read from file:", list(data_read))

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))


#====================

# specifying the number of bytes to read from the stream:
#
# potential uses of this technique include reading a file in chunks,
# processing each chunk, and then reading the next chunk,
# which is useful for large files that cannot fit into memory all at once.
#
# also useful for reading a specific number of bytes from a file, such as reading a header, BOM, or a fixed-size record.

try:
    bf = open('file.bin', 'rb')
    data = bytearray(bf.read(5))
    bf.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))


#====================

