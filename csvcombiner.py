__author__ = 'LV-JYOO'

"""
Appending a new Row with Column Name
"""

from os import listdir
from os.path import isfile, join
import csv
import os

mypath = "C:\Users\LV-JYOO\Documents\GitHub\draftkings\week2014"

onlyfiles = [ os.getcwd()+"\\week2014\\"+f for f in listdir(mypath) if isfile(join(mypath,f)) ]

weeknum = 1

for csvfile in onlyfiles:
    with open(csvfile, 'rb') as fin, open('newcsv_week'+str(weeknum)+'.csv', 'wb') as fout:
        reader = csv.reader(fin, delimiter=',')
        writer = csv.writer(fout, delimiter=',')

        all = []
        row = next(reader)
        row.insert(0, 'week')
        all.append(row)
        for row in reader:
            row.insert(0, weeknum)
            all.append(row)
        writer.writerows(all)
    weeknum += 1
########################################################################################################################

from glob import glob

with open('singleDataFile.csv', 'a') as singleFile:
    for csvFile in glob('*.csv'):
        for line in open(csvFile, 'r'):
            singleFile.write(line)


import os
os.getcwd()

fout = open(os.getcwd()+"\\2014new.csv","wb")
# first file:
for line in open("newcsv_week01.csv"):
    fout.write(line)
# now the rest:
for num in range(2,18):
    f = open("newcsv_week"+str(num)+".csv")
    for line in f:
         fout.write(line)
    f.close() # not really needed
fout.close()