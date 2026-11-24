from os import strerror

srcname = input("Enter the source file name: ")
try:
    src = open(srcname, 'rb')
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)

dstname = input("Enter the destination file name: ")
try:
    dst = open(dstname, 'wb')
except Exception as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    src.close()
    exit(e.errno)

buffer = bytearray(65536)
total = 0
try:
    readin = src.readinto(buffer)
    while readin > 0:
        written = dst.write(buffer[:readin])
        total += written
        readin = src.readinto(buffer)
except IOError as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    exit(e.errno)

print(total, 'byte(s) succesfully written')
src.close()
dst.close()


#====================
# check the copy by reading the destination file and printing its contents to the console:

try:
    bf = open('filecopy.bin', 'rb')
    data_read = bytearray(bf.read())
    bf.close()

    # print each byte in the bytearray as a hexadecimal number
    for b in data_read:
        print("\nbyte: " + hex(b), end=' ')

    # print the list of bytes read from the file
    print("\nList of bytes read from file:", list(data_read))

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))