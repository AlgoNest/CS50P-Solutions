import sys
import csv
from tabulate import tabulate
lst = []
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

if ".csv" not in sys.argv[1]:
    sys.exit("Not a CSV file")

with open(f"{sys.argv[1].rstrip()}") as file:
    reader = csv.reader(file)
    print(tabulate(reader, headers = "firstrow",tablefmt="grid"))

