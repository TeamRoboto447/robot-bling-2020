#!/usr/bin/python3
from networktables import NetworkTables as NT
from time import sleep
import settings

sett = settings.getSettings("NetworkTables")

class tables:
    def __init__(self):
        if not sett['Deployed']:
            NT.initialize(server=sett['HostAddress'])
        else:
            NT.initialize(f"roboRIO-{sett['TeamNumber']}-FRC.local")
        print("Connecting...")
        while(not NT.isConnected()):
                sleep(0.1)
        print("Connected")
        self.blingSelect = NT.getEntry(sett["BlingSelect"])
        self.teamColor = NT.getEntry(sett["TeamColor"])
        self.stationNumb = NT.getEntry(sett["stationNumb"])
    def getBlingSelect(self):
        return self.blingSelect.value
    def getTeamColor(self):
        return self.teamColor.value
    def getStatonNumb(self):
        return self.stationNumb.value
    def EventListener(self,listener):
        NT.addEntryListener(listener)
