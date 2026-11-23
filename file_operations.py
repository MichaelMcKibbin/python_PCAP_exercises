import sys

# importing the sys module gives us access to some pre-opened streams, including sys.stdin, sys.stdout, and sys.stderr, which are file-like objects that represent the standard input, output, and standard error streams, respectively.
#
# sys.stdin
# stdin (as standard input)
# the stdin stream is normally associated with the keyboard, pre-open for reading and regarded as the primary data source for the running programs;
# the well-known input() function reads data from stdin by default.
#
# sys.stdout
# stdout (as standard output)
# the stdout stream is normally associated with the screen, pre-open for writing, regarded as the primary target for outputting data by the running program;
# the well-known print() function outputs the data to the stdout stream.
#
# sys.stderr
# stderr (as standard error output)
# the stderr stream is normally associated with the screen, pre-open for writing, regarded as the primary place where the running program should send information on the errors encountered during its work;
# we haven't presented any method to send the data to this stream (we will do it soon, we promise)
# the separation of stdout (useful results produced by the program) from the stderr (error messages, undeniably useful but does not provide results) gives the possibility of redirecting these two types of information to the different targets. More extensive discussion of this issue is beyond the scope of our course. The operation system handbook will provide more information on these issues.
#



#
# # Create a new file for writing (will fail if the file already exists)
# try:
#     stream = open("file.txt", "x") # x mode is for exclusive creation, failing if the file already exists
#     # Processing goes here.
#     stream.close()
# except Exception as exc:
#     print("Cannot open the file:", exc)
#

# Open an existing file for reading
try:
    stream = open("file.txt", "rt") # Syntax: open(file_name, mode=open_mode, encoding=text_encoding)
    # Processing goes here.
    stream.close()
except Exception as exc:
    print("Cannot open the file:", exc)


# Diagnosing stream problems
from os import strerror

try:
    s = open("nofile.txt", "rt")
    # Actual processing goes here.
    s.close()
except Exception as exc:
    print("The file could not be opened:", strerror(exc.errno))

# If the file does not exist the program will print the following message:
# The file could not be opened: No such file or directory


# another file open error example:
import errno

try:
    stream = open("file", "rb")
    print("exists")
    stream.close()
except IOError as error:
    if error.errno == errno.ENOENT:
        print("absent")
    else:
        print("unknown")
