import csv


def pathString(filenamestring, test_split):
   with open(filenamestring) as csvfile:
     reader = csv.reader(csvfile, delimiter=' ')
     rowLeaders = []
     for row in reader:
       if len(row) != 0:
         row = row[0].split(',')
         rowLeaders.append(row)
     rowLeaders = rowLeaders[1:-1]
     valueList = []
     for index in range(len(rowLeaders)):
         valueList.append((index, rowLeaders[index][2]))
     index = int(len(valueList) * test_split) - 1
     testList = valueList[0: index + 1]
     trainList = valueList[index + 1:]
     trainTuple = [[x[0],float(x[1])] for x in trainList]
     testTuple = [[x[0],float(x[1])] for x in testList]
     return trainTuple, testTuple


