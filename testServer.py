#!/usr/bin/python3
from networktables import NetworkTables as NT
from time import sleep
import settings

NT.initialize()

blingSelect = NT.getEntry("/Bling/blingSelect")
teamColor = NT.getEntry("/FMSInfo/IsRedAlliance")
stationNumb = NT.getEntry("/FMSInfo/StationNumber")

blingSelect.setString("idle")
teamColor.setBoolean(True)
stationNumb.setNumber(1)

def changeMode():
    print("Changing Mode")
    mode = input("Select A Mode> ")
    print(f"Selected mode: '{mode}'")
    blingSelect.setString(mode)

def changeColor():
    print("Changing Color")
    validColor = False
    while not validColor:
        color = input("Select A Color:\nR = Red\nB = Blue\nC = Cancel\n> ")
        if color == "R":
            validColor = True
            print("Selected Color: Red")
            teamColor.setBoolean(True)
        elif color == "B":
            validColor = True
            print("Selected Color: Blue")
            teamColor.setBoolean(False)
        elif color == "C":
            validColor = True
            print("Color Not Changed")
        else:
            validColor = False
            print("Not A Valid Color")
            
def changeStation():
    validStation = False
    while not validStation:
        station = input("Select A Station: 1, 2, 3, Cancel\n> ")
        if station == "1":
            validStation = True
            print("Selected Station: 1")
            teamNumber.setNumber(1)
        elif station == "2":
            validStation = True
            print("Selected Station: 2")
            teamNumber.setNumber(2)
        elif station == "3":
            validStation = True
            print("Selected Station: 3")
            teamNumber.setNumber(3)
        elif station == "Cancel":
            validStation = True
            print("Station Not Changed")
        else:
            validStation = False
            print("Not A Valid Station")

while True:
    selectChange = input("M = Mode\nC = Color\nS = Station Number\n> ")
    if selectChange == "M":
        changeMode()
    elif selectChange == "C":
        changeColor()
    elif selectChange == "S":
        changeStation()
    else:
        print("Invalid Selection")
