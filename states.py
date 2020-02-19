
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
        color = {"red":(255,0,0),"blue":(0,0,255)}[self.tables.getTeamColor()]
        self.dic["frame"].fill(color)
        self.dic["turret"].fill(color)
        self.pixels.show()
    def run(self):
        pass
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

