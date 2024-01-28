import sys
import getopt
import json
import ast

def correctUsage():
    print("usage: py clDatabase.py -a firstName lastName phoneNumber email -l -f arg2 -d arg3")
    sys.exit()

def readJSON():
    file = open('db.json', "r")
    existingData = json.loads(file.read())
    file.close()
    return existingData

def writeJSON(existingData):
    file = open('db.json', 'w')
    file.write(json.dumps(existingData))
    file.close()

def createJSON():
    writeJSON([])

try:
    file = open("db.json", "r")
except FileNotFoundError:
    createJSON()

try:
    opts, args = getopt.getopt(sys.argv[1:], "alf:d:")
    if len(sys.argv) == 1:
        correctUsage()
    if opts[0][0] == "-a":
        if len(args) >= 4:
            fNameInput = args[0]
            lNameInput = args[1]
            phoneNumInput = args[2]
            emailInput = args[3]
            newData = {
                "fName": f'{fNameInput}',
                "lName": f'{lNameInput}',
                "phoneNum": f'{phoneNumInput}',
                "email": f'{emailInput}'
            }
            existingData = readJSON()
            existingData.append(newData)
            writeJSON(existingData)
            print(f"{fNameInput} {lNameInput} was added")
        else:
            correctUsage()

    elif opts[0][0] == "-l":
        existingData = readJSON()
        for i in range(len(existingData)):
            print(f"{existingData[i]['fName']} {existingData[i]['lName']}, {existingData[i]['phoneNum']}, {existingData[i]['email']}\n")

    elif opts[0][0] == "-f":
        searchParam = opts[0][1]
        existingData = readJSON()
        for i in range(len(existingData)):
            if existingData[i]['fName'] == searchParam or existingData[i]['lName'] == searchParam:
                print(f"{existingData[i]['fName']} {existingData[i]['lName']}, {existingData[i]['phoneNum']}, {existingData[i]['email']}")
                break
            elif i == len(existingData)-1:
                print(f"{searchParam} not found")

    elif opts[0][0] == "-d":
        searchParam = opts[0][1]
        existingData = readJSON()
        for i in range(len(existingData)):
            if existingData[i]['fName'] == searchParam or existingData[i]['lName'] == searchParam:
                print(f"{existingData[i]['fName']} {existingData[i]['lName']} was deleted")
                del existingData[i]
                writeJSON(existingData)
                break
            elif i == len(existingData)-1:
                print(f"{searchParam} not found")

except FileNotFoundError:
    print("db.json not found")
    sys.exit()
except getopt.GetoptError:
    correctUsage()
