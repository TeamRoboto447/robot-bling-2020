from networktables import NetworkTables as NT
import time

NT.startServer(persistFilename='networktables.ini', listenAddress='192.168.137.1', port=1735)

blingSelect = NT.getTable("Bling").getEntry("blingSelect")
blingSelect.setString("idle")
NT.getTable("FMSInfo").getEntry("IsRedAlliance").setBoolean(True)

print("Server started and values set")

while True:
    blingSelect.setString(input("blingSelect: "))
