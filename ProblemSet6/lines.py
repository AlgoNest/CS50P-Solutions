import sys
import csv
# takes one command line argv only
if len(sys.argv) < 2:
    sys.exit("Too few argvments")
elif len(sys.argv) > 2:
    sys.exit("Too many argvments")
elif ".py" not in sys.argv[1]:
    sys.exit("Not a Python file")
else:
    if sys.argv[1].endswith(".py"):
        lst = []
        count = 0
        with open(f"{sys.argv[1]}") as file:
            for row in file.readlines():
                if row.lstrip().startswith("#"):
                    pass

                elif row.isspace():
                    pass
                else:
                    count += 1

    print(count)


# return number of line of code in the program
# without adding commments and blank lines
# if command line argv is not given or the file doesn't end with .py
# or the user doesn't give specfic file that doesn't exist
    # then exist the program
# if the line start with '#' or extra spaces
