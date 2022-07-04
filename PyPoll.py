#connection to election results file
from ast import With
from importlib import resources
from importlib.resources import Resource
import datetime

import csv
from wsgiref import headers
dir(csv)
import os
import csv

#KEEP CODE
#file_to_load = 'Resources/election_results.csv'

file_to_load='C:/Users/sean4/Election_Analysis/Resources/election_results.csv'

#KEEP CODE

file_to_save='C:/Users/sean4/Election_Analysis/Resources/election_analysis.txt'

outfile = open(file_to_save,'w')
outfile.write("Hello World")
outfile.close()

#KEEP CODE

file_to_save='C:/Users/sean4/Election_Analysis/Resources/election_analysis.txt'
with open(file_to_save,"w") as txt_file:
    txt_file.write("Arapahoe\nDenver\nJefferson")
txt_file.close()

#KEEP CODE

file_to_load='C:/Users/sean4/Election_Analysis/Resources/election_results.csv'

file_to_save='C:/Users/sean4/Election_Analysis/Resources/election_analysis.txt'

with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)

    for row in file_reader:
                print(row)


# Create a filename variable to a direct or indirect path to the file.
    file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")