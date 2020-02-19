
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
        color = {True:(255,0,0),False:(0,0,255)}.get(self.tables.getTeamColor(),(0,255,0))
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
    end = end

class fight:
    def __init__(self,dictOfGroups,tables,pixels):
        self.dic = dictOfGroups
        self.tables = tables
        self.pixels = pixels
        self.iter = 0
    def start(self):
        color = (0, 255, 0)
        self.dic["frameLeft"].fill(color)
        self.dic["frameRight"].fill(color)
        self.dic["frameFront"].fill(color)
        self.dic["frameBack"].fill(color)
        self.pixels.show()
    def run(self):
        if self.iter%2 is 0:
            self.dic["frameLeft"].fill((0, 0, 255), show = True)
            self.dic["frameRight"].invertedFill((0, 0, 255), show = True)
            self.dic["frameFront"].fill((255, 0, 0), show = True)
            self.dic["frameBack"].invertedFill((255, 0, 0), show = True)
        else:
            self.dic["frameLeft"].invertedFill((255, 0, 0), show = True)
            self.dic["frameRight"].fill((255, 0, 0), show = True)
            self.dic["frameFront"].invertedFill((0, 0, 255), show = True)
            self.dic["frameBack"].fill((0, 0, 255), show = True)
        self.iter += 1
    end = end
