#!/usr/bin/python3
from networktables import NetworkTables as NT
from time import sleep

blingTable = None
blingSelect = None
def initServer():
	global blingTable, blingSelect
	NT.initialize(server='roborio-447-frc.local')
	print("Connecting...")
	while(not NT.isConnected()):
		sleep(0.1)
	print("Connected")
	blingTable = NT.getTable("Bling")
	blingSelect = blingTable.getEntry("blingSelect")
	return NT

def getBlingSelect:
	blingSelect.getString("idle")
