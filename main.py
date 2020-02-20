#!/usr/bin/python3
import board, neopixel, time
from group import LEDSection, SectionGroup
import networkTables, states, settings

sett = settings.getSettings()

NUM_LED = 60 * 5
NEO_PIN = board.D18

pixels = neopixel.NeoPixel(NEO_PIN, NUM_LED, auto_write = False, brightness = 0.25)
pixels.show()

tables = networkTables.tables()

frameLeft = LEDSection(pixels,0,10)
frameRight = LEDSection(pixels,10,20,True)
frameFront = LEDSection(pixels,20,30)
frameBack = LEDSection(pixels,30,40, True)

turretRight = LEDSection(pixels,40,45)
turretLeft = LEDSection(pixels,45,50,True)

groups = {
    "frameLeft": frameLeft,
    "frameRight": frameRight,
    "frameFront": frameFront,
    "frameBack": frameBack,
    "frame": SectionGroup(frameLeft, frameFront, frameRight, frameBack),
    "turretRight": turretRight,
    "turretLeft": turretLeft,
    "turret": SectionGroup(turretLeft,turretRight)
}

statesDict = {
    "init": states.init(groups, tables, pixels),
    "idle": states.idle(groups, tables, pixels),
    "grade": states.grade(groups, tables, pixels),
    "fight": states.fight(groups, tables, pixels)
}

state = statesDict["init"]
state.start()
time.sleep(1)

def changeState(key, value, isNew):
    global state, statesDict
    if key == sett["NetworkTables"]["BlingSelect"]:
        state.end()
        state = statesDict[value]
        state.start()
    elif key == sett["NetworkTables"]["TeamColor"]:
        state.teamChange(value)

tables.EventListener(changeState)

try:
    while True:
        state.run()
        time.sleep(0.001)
finally:
    state.end()
