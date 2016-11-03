import os
import random
import commands

files = []
classes = {
        'sport': 511,
        'tech': 401,
        'politics': 417,
        'entertainment': 386,
        'business': 510
        }

def getInput():
    isEmpty = commands.getoutput("ls ./Input/sport")
    if isEmpty != '':
        for types in classes.keys():
            filePath = './Input/' + types
            os.system("mv %s/* ./datasets/%s/" %(filePath, types))
        for types in classes.keys():
            while len(files) < 50:
                fileNumber = random.randint(1, classes[types])
                fileName = "{0:03}".format(fileNumber) + '.txt'
                if fileName not in files:
                    files.append(fileName)
                    filePath = './datasets/' + types + '/' + fileName
                    os.system("mv %s ./Input/%s" %(filePath, types))
            del files[:]
    else:
        for types in classes.keys():
            while len(files) < 50:
                fileNumber = random.randint(1, classes[types])
                fileName = "{0:03}".format(fileNumber) + '.txt'
                if fileName not in files:
                    files.append(fileName)
                    filePath = './datasets/' + types + '/' + fileName
                    os.system("mv %s ./Input/%s" %(filePath, types))
            del files[:]

getInput()
