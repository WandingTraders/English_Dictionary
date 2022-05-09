import csv

def returnTable():

    csvFile = open(
        r"C:\Users\18104\OneDrive - Wellington College\2022 13 DTS\English_Dictionary\templates\Vocab_List.csv")

    tableData = csv.reader(csvFile, delimiter=",")

    data = []

    for row in tableData:
        data.append(row)

    return data