# read an image file, robie_robot.png, into a bytearray and copy it to a new file called robie_copy.png:

try:
    stream = open("robie_robot.png", "rb")
    image = bytearray(stream.read())
    stream.close()
except IOError:
    print("failed")
else:
    try:
        stream = open("robie_copy.png", "wb")
        stream.write(image)
        stream.close()
    except IOError:
        print("failed")
    else:
        print("success")