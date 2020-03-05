import random, math
from time import sleep

def end(self):
    for a in self.dic:
        self.dic[a].fill((0,0,0))
    self.pixels.show()

class fancyidle:
    def __init__(self,dictOfGroups,tables,pixels):
        self.dic = dictOfGroups
        self.tables = tables
        self.pixels = pixels
        self.currentColor = (0,255,0)
        self.state = False
    def start(self):
        self.currentColor = {True:(255,0,0),False:(0,0,255)}.get(self.tables.getTeamColor(),(0,255,0))
    def run(self):
        if self.state:
            done = self.dic["frame"].fillOverTimeAsOne(self.currentColor, numberPerLoop = 1)
        else:
            done = self.dic["frame"].invertedFillOverTimeAsOne((255, 255, 255), numberPerLoop = 1)
        if done:
            self.state = not self.state
            self.dic["frame"].reset()
    def teamChange(self, team):
        self.currentColor = {True:(255,0,0),False:(0,0,255)}.get(self.tables.getTeamColor(),(0,255,0))
    end = end

class randomColors:
    def __init__(self,dictOfGroups,tables,pixels):
        self.dic = dictOfGroups
        self.tables = tables
        self.pixels = pixels
    def start(self):
        self.dic["frame"].fill((255, 255, 255))
        self.pixels.show()
    def run(self):
        self.pixels[math.floor(random.random()*len(self.pixels)-1)] = (math.floor(random.random()*255), math.floor(random.random()*255), math.floor(random.random()*255))
    def teamChange(self, team):
        pass
    end = end

class idle:
    def __init__(self,dictOfGroups,tables,pixels):
        self.dic = dictOfGroups
        self.tables = tables
        self.pixels = pixels
    def start(self):
        color = {True:(255,0,0),False:(0,0,255)}.get(self.tables.getTeamColor(),(0,255,0))
        self.dic["frameLeft"].fill(color)
        self.dic["frameRight"].fill(color)
        self.pixels.show()
    def run(self):
        pass
    def teamChange(self, team):
        color = {True:(255,0,0),False:(0,0,255)}.get(team,(0,255,0))
        self.dic["frameLeft"].fill(color)
        self.dic["frameRight"].fill(color)
        self.pixels.show()
    end = end

class grade:
    def __init__(self,dictOfGroups,tables,pixels):
        self.dic = dictOfGroups
        self.tables = tables
        self.pixels = pixels
    def start(self):
        self.dic["frame"].grade((255,0,0),(0,0,255))
        self.pixels.show()
    def run(self):
        pass
    def teamChange(self, team):
        pass
    end = end

class fight:
    def __init__(self,dictOfGroups,tables,pixels):
        self.dic = dictOfGroups
        self.tables = tables
        self.pixels = pixels
        self.state = False
    def start(self):
        color = (0, 0, 255)
        self.dic["frame"].fill(color)
        self.pixels.show()
    def run(self):
        if self.state:
            done = self.dic["frame"].fillOverTimeAsOne((0, 0, 255), numberPerLoop = 1)
        else:
            done = self.dic["frame"].invertedFillOverTimeAsOne((255, 0, 0), numberPerLoop = 1)
        if done:
            self.state = not self.state
            self.dic["frame"].reset()
        
    def teamChange(self, team):
        pass
    end = end
    
class off:
    def __init__(self,dictOfGroups,tables,pixels):
        self.dic = dictOfGroups
        self.tables = tables
        self.pixels = pixels
    start = end
    run = end
    def teamChange(self,team):
        pass
    end = end
    

class init:
    numberOfStates = 3
    def __init__(self, dictOfGroups, tables, pixels):
        self.dic = dictOfGroups
        self.tables = tables
        self.pixels = pixels
        self.stage = 0
    def start(self):
        pass
    def run(self):
        sleep(0.01)
        if self.stage == 0:
            bools = [
            self.dic["frame"].fillOverTimeAsOne((20, 0, 0), numberPerLoop = 1)
            ]
        elif self.stage == 1:
            bools = [
            self.dic["frame"].fillOverTimeAsOne((0, 0, 55), numberPerLoop = 1)
            ]
        elif self.stage == 2:
            bools = [
            self.dic["frame"].fillOverTimeAsOne((100, 100, 100), numberPerLoop = 1)
            ]
        else:
            bools = [True]
        changeMode = True
        for bool in bools:
            if not bool:
                changeMode = False
        if changeMode:
            self.stage += 1
            if self.stage >= self.numberOfStates:
                self.stage = 0
                return True
            self.dic["frame"].reset()
        return False
    def teamChange(self, team):
        pass
    end = end
        
