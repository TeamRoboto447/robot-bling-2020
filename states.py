
def end(self):
    for a in self.dic:
        self.dic[a].fill((0,0,0))
    self.pixels.show()

class idle:
    def __init__(self,dictOfGroups,tables,pixels):
        self.dic = dictOfGroups
        self.tables = tables
        self.pixels = pixels
    def start(self):
        color = {True:(255,0,0),False:(0,0,255)}.get(self.tables.getTeamColor(),(0,255,0))
        self.dic["frame"].fill(color)
        self.dic["turret"].fill(color)
        self.pixels.show()
    def run(self):
        pass
    def teamChange(self, team):
        color = {True:(255,0,0),False:(0,0,255)}.get(team,(0,255,0))
        self.dic["frame"].fill(color)
        self.dic["turret"].fill(color)
        self.pixels.show()
    end = end

class grade:
    def __init__(self,dictOfGroups,tables,pixels):
        self.dic = dictOfGroups
        self.tables = tables
        self.pixels = pixels
    def start(self):
        self.dic["frame"].grade((255,0,0),(0,0,255))
        self.dic["turret"].grade((255,0,0),(0,255,0))
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
        color = (0, 255, 0)
        self.dic["frameLeft"].fill(color)
        self.dic["frameRight"].fill(color)
        self.dic["frameFront"].fill(color)
        self.dic["frameBack"].fill(color)
        self.dic["turret"].fill(0)
        self.pixels.show()
    def run(self):
        if self.state:
            print("normal")
            done = self.dic["frame"].fillOverTimeAsOne((0, 0, 255), numberPerLoop = 2)
        else:
            print("inverted")
            done = self.dic["frame"].invertedFillOverTimeAsOne((255, 0, 0), numberPerLoop = 2)
        
        if done:
            self.state = not self.state
            self.dic["frame"].reset()

        
    def teamChange(self, team):
        pass
    end = end
    
class init:
    def __init__(self, dictOfGroups, tables, pixels):
        self.dic = dictOfGroups
        self.tables = tables
        self.pixels = pixels
        self.stage = 0
    def start(self):
        pass
    def run(self):
        if self.stage == 0:
            bools = [
            self.dic["frame"].fillOverTimeAsOne((0, 10, 0), numberPerLoop = 1),
            self.dic["turret"].fillOverTimeAsOne((0, 10, 0), numberPerLoop = 1)
            ]
            #print("stage0")
        elif self.stage == 1:
            bools = [
            self.dic["frame"].fillOverTimeAsOne((55, 0, 55), numberPerLoop = 1),
            self.dic["turret"].fillOverTimeAsOne((55, 0, 55), numberPerLoop = 1)
            ]
            #print("stage1")
        elif self.stage == 2:
            bools = [
            self.dic["frame"].fillOverTimeAsOne((255, 255, 255), numberPerLoop = 1),
            self.dic["turret"].fillOverTimeAsOne((255, 255, 255), numberPerLoop = 1)
            ]
            #print("stage2")
        changeMode = True
        for bool in bools:
            if not bool:
                changeMode = False
        if changeMode:
            self.stage += 1
            self.dic["frameLeft"].reset()
            self.dic["frameRight"].reset()
            self.dic["frameFront"].reset()
            self.dic["frameBack"].reset()
        #self.dic["frame"].fill((0, 10, 0), show = True)
        #self.dic["turret"].fill((0, 10, 0), show = True)
    def teamChange(self, team):
        pass

    end = end
