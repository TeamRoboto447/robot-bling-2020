
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
        self.dic["frame"].fill(color, show = True)
        self.dic["turret"].fill(color, show = True)
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
            bools = [
            self.dic["frameLeft"].fillOverTime((0, 0, 255), numberPerLoop = 1),
            self.dic["frameRight"].invertedFillOverTime((0, 0, 255), numberPerLoop = 1),
            self.dic["frameFront"].fillOverTime((255, 0, 0), numberPerLoop = 1),
            self.dic["frameBack"].invertedFillOverTime((255, 0, 0), numberPerLoop = 1)
            ]
        else:
            bools = [
            self.dic["frameLeft"].invertedFillOverTime((255, 0, 0), numberPerLoop = 1),
            self.dic["frameRight"].fillOverTime((255, 0, 0), numberPerLoop = 1),
            self.dic["frameFront"].invertedFillOverTime((0, 0, 255), numberPerLoop = 1),
            self.dic["frameBack"].fillOverTime((0, 0, 255), numberPerLoop = 1)
            ]
        changeMode = True
        for bool in bools:
            if not bool:
                changeMode = False
        if changeMode:
            self.state = not self.state
            self.dic["frameLeft"].reset()
            self.dic["frameRight"].reset()
            self.dic["frameFront"].reset()
            self.dic["frameBack"].reset()

        
    def teamChange(self, team):
        pass
    end = end
    
class init:
    def __init__(self, dictOfGroups, tables, pixels):
        self.dic = dictOfGroups
        self.tables = tables
        self.pixels = pixels
    def start(self):
        self.dic["frame"].fill((0, 55, 0), show = True)
        self.dic["turret"].fill((0, 55, 0), show = True)
        self.dic["frame"].fill((155, 0, 155), show = True)
        self.dic["turret"].fill((155, 0, 155), show = True)
        self.dic["frame"].fill((255, 255, 255), show = True)
        self.dic["turret"].fill((255, 255, 255), show = True)
    def run(self):
        pass
    end = end
