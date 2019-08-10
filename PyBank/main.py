#import modules
import os
import csv

#get file path
csv_file_path = os.path.join("c:/Users/mbocc/COLNYC20190716DATA/02-Homeworks/03-Python/Instructions/PyBank/Resources/budget_data.csv")

#open file and read header
with open(csv_file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")
