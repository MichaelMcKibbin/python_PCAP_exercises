import math


class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    def __init__(self, line_number, line, reason):
        message = (
            f"Bad data on line {line_number}: {reason}. "
            f"Content: {line!r}"
        )
        super().__init__(message)


class FileEmpty(StudentsDataException):
    def __init__(self):
        super().__init__("The source file is empty.")


def read_students(filename):
    students = {}

    with open(filename, "r", encoding="utf-8-sig") as file:
        for line_number, line in enumerate(file, start=1):
            fields = line.split()

            if len(fields) != 3:
                raise BadLine(
                    line_number,
                    line.rstrip("\r\n"),
                    "expected a first name, last name, and points"
                )

            first_name, last_name, points_text = fields

            try:
                points = float(points_text)
            except ValueError:
                raise BadLine(
                    line_number,
                    line.rstrip("\r\n"),
                    f"invalid points value {points_text!r}"
                ) from None

            if not math.isfinite(points):
                raise BadLine(
                    line_number,
                    line.rstrip("\r\n"),
                    "points must be a finite number"
                )

            name = (first_name, last_name)
            total = students.get(name, 0.0) + points

            if not math.isfinite(total):
                raise BadLine(
                    line_number,
                    line.rstrip("\r\n"),
                    "the accumulated points exceed the supported range"
                )

            students[name] = total

    if not students:
        raise FileEmpty()

    return students


def main():
    filename = input("Enter Prof. Jekyll's filename: ")

    try:
        students = read_students(filename)

    except StudentsDataException as error:
        print("Data error:", error)

    except UnicodeError as error:
        print("Encoding error: the file could not be read as UTF-8.", error)

    except (OSError, ValueError) as error:
        print("File error:", error)

    else:
        for (first_name, last_name), total in sorted(students.items()):
            print(f"{first_name} {last_name}\t{total}")


if __name__ == "__main__":
    main()



# Scenario
#
# Prof. Jekyll conducts classes with students and regularly makes notes in a text file.
# Each line of the file contains three elements:
# - the student's first name,
# - the student's last name,
# - and the number of points the student received during certain classes.
#
# The elements are separated with white spaces.
# Each student may appear more than once inside Prof. Jekyll's file.
#
# The sample file (jekyll-notes.txt) contains the following lines:
#
# John	Smith	5
# Anna	Boleyn	4.5
# John	Smith	2
# Anna	Boleyn	11
# Andrew	Cox	1.5


# Solution:
#
# The important parts are:
# - line.split() handles spaces, tabs, and repeated whitespace.
# - enumerate(file, start=1) provides line numbers for error messages.
# - (first_name, last_name) is a tuple used as the dictionary key.
# - students.get(name, 0.0) + points adds points to the student’s previous total.
# - sorted(students.items()) sorts by first name, then last name.
# - Raising BadLine immediately stops reading. The exception is caught in main(), an error is printed, and the program ends without displaying a partial report.
# An empty file raises FileEmpty.
# A blank line raises BadLine, because it does not contain the required three fields.
# Negative points are accepted because the scenario doesn’t prohibit them.