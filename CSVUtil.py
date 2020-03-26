# -*- coding: utf-8 -*-
import csv
import string
import pprint
import os

def getOnlyDirs(path):
    retDirs = [o for o in os.listdir(path) if os.path.isdir(os.path.join(path,o))]
    return retDirs

def getOnlyCSV(path):
    ret = [o for o in os.listdir(path) if o.endswith(".csv")]
    return ret
def __removeHeader(reader):
    headers = next(reader, None)
    return reader
def getRowsByColumn(csvObj, columnName, columnValue):
    """Returns the list of columns by name
    :columnName: the column name
    :columnValue: the value in the column
    :returns: the list of rows containing the value
    """
    ret = []
    valueToTake = 0
    for i in range(len(csvObj['header'])):
        if csvObj['header'][i] == columnName.lower():
            valueToTake = i
    for row in csvObj['listRows']:
        currentColumnValue = row[valueToTake]
        if currentColumnValue == columnValue:
            ret.append(row)
    return ret

def getColumns(csvObj, columnName):
    """Returns the columns by name

    :csvObj: the object
    :columnName: the name of the column
    :returns: the values
    """
    columns = []
    idColumn = getIndexColumn(csvObj, columnName)
    columns = [r[idColumn] for r in  csvObj['listRows']]
    return columns

def getIndexColumn(csvObj, headerValue):
    """Returns the column Index
    :returns: the index of column
    """
    ret = -1
    for i in range(len(csvObj['header'])):
        if csvObj['header'][i] == headerValue.lower():
            ret = i
    return ret

def getColumnInRow(csvObj, r, nameColumn):
    """Returns the column value in row

    :r: the row
    :nameColumn: the name of the column
    :returns: the value in the row
    """
    indexColumn = getIndexColumn(csvObj, nameColumn)
    return r[indexColumn]

def readCSV(csvName, delimiter = ";"):
    """Parse a csv for create the state machine, returns the list of rows and the header"""
    line_count = 0
    listRows = []
    header = None
    with open(csvName, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = delimiter)
        # Use for loop to print csv row by row
        for row in csv_reader:
            if line_count != 0:
                listRows.append(row)
            else:
                header = row
            line_count = line_count + 1
    header = [h.lower() for h in header]
    # # Use Sniffer to figure out csv dialect
    #     dialect = csv.Sniffer().sniff(csv_file.read(1024), delimiter)
    #     csv_file.seek(0)
    #     # pass the dialect to filereader to read the file
    #     # reader = csv.reader(csv_file, dialect)
    #     reader = csv.reader(csv_file, dialect)
    #     reader = __removeHeader(reader)
    #     for i in reader:
    #         # listRows.append([i[0], i[1]])
    #         listRows.append(i)
    return {
            'header' : header,
            'listRows' : listRows
          }
