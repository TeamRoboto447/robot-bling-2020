import math, inspect
class quadratic:
    def __init__(self, a, b, c):
        self.a=a
        self.b=b
        self.c=c
    def __repr__(self):
        return("quadratic({a},{b},{c})".format(**self.__dict__))
    def __str__(self):
        return("{a}x^2+{b}x+{c}".format(**self.__dict__))
    def __add__(self,oth):
        if type(oth)==type(self):
            return(quadratic(self.a+oth.a,self.b+oth.b,self.c+oth.c))
        else:
            return(quadratic(self.a,self.b,self.c+oth))
    def __sub__(self,oth):
        if type(oth)==type(self):
            return(quadratic(self.a-oth.a,self.b-oth.b,self.c-oth.c))
        else:
            return(quadratic(self.a,self.b,self.c-oth))
    def __mul__(self,oth):
        if type(oth)==type(self) and oth.a==0 and self.a==0:
            a = oth.b*self.b
            b = oth.b*self.c+oth.c*self.b
            c = oth.c*self.c
            return quadratic(a,b,c)
        if type(oth)==type(self) or type(oth).__name__=='str':
            raise TypeError("unsupported operand type(s) for *: '{}' and '{}'".format(type(self).__name__,type(oth).__name__))
        try:
            return(quadratic(self.a*oth,self.b*oth,self.c*oth))
        except TypeError:
            raise TypeError("unsupported operand type(s) for *: '{}' and '{}'".format(type(self).__name__,type(oth).__name__))
    def __div__(self,oth):
        if type(oth)==type(self) and (oth == self.factors()[0] or oth == self.factors()[1]):
            a=self.factors()
            return a[[1,0][a.index(oth)]]
        if type(oth)==type(self) or type(oth).__name__=='str':
            raise TypeError("unsupported operand type(s) for /: '{}' and '{}'".format(type(self).__name__,type(oth).__name__))
        try:
            return(quadratic(self.a/oth,self.b/oth,self.c/oth))
        except TypeError:
            raise TypeError("unsupported operand type(s) for /: '{}' and '{}'".format(type(self).__name__,type(oth).__name__))
    def __eq__(self,oth):
        return(type(oth)==type(self) and oth.a==self.a and oth.b==self.b and oth.c==self.c)
    def __call__(self,x):
        return(x**2*self.a+x*self.b+self.c)
    def __pos__(self):
        return(quadratic(self.a,self.b,self.c))
    def __neg__(self):
        return(quadratic(-self.a,-self.b,-self.c))
    def solve(self,y=0):
        if isinstance(y,quadratic):
            return (self-y).solve()
        c=self.c-y
        if self.a == 0 and self.b==0:
            raise ValueError("Can not solve for a constant y value")
        if self.a == 0:
            return -self.c/self.b
        try:
            first=(-self.b+math.sqrt(self.b**2-4*self.a*c))/(self.a*2)
        except ValueError:
            first=None
        try:
            second=(-self.b-math.sqrt(self.b**2-4*self.a*c))/(self.a*2)
        except ValueError:
            second=None
        return first, second
    def factors(self):
        out=()
        try:
            first=(-self.b+math.sqrt(self.b**2-4*self.a*self.c))/(self.a*2)
            out=out+(quadratic(0,1,first),)
        except ValueError:
            first=None
        try:
            second=(-self.b-math.sqrt(self.b**2-4*self.a*self.c))/(self.a*2)
            out=out+(quadratic(0,1,second),)
        except ValueError:
            second=None
        return out
    __truediv__ = __div__
    __floordiv__ = __div__
class wave:
    def __init__(self, wlen=2*math.pi, amp=1, respos=0, phase=0):
        self.wlen=wlen
        self.amp=amp
        self.respos=respos
        self.phase=phase
    def __repr__(self):
        return "wave({wlen},{amp},{respos},{phase})".format(**self.__dict__)
    def __str__(self):
        return "sin(pi/{wlen}+{phase})*{amp}+{respos}".format(**self.__dict__)
    def __add__(self, oth):
        return wave(self.wlen, self.amp, self.respos+oth,self.phase)
    def __sub__(self, oth):
        return wave(self.wlen, self.amp, self.respos-oth,self.phase)
    def __mul__(self, oth):
        return wave(self.wlen, self.amp*oth, self.respos*oth,self.phase)
    def __div__(self, oth):
        return wave(self.wlen, self.amp/oth, self.respos/oth,self.phase)
    def __eq__(self,oth):
        return(type(oth)==type(self) and oth.amp==self.amp and oth.respos==self.respos and oth.phase==self.phase)
    def __call__(self,x):
        return math.sin(x*math.pi/self.wlen+self.phase)*self.amp+self.respos
    def __pos__(self):
        return wave(self.wlen, self.amp, self.respos,self.phase)
    def __neg__(self):
        return wave(self.wlen, -self.amp, -self.respos,self.phase)
    def move(self,i = 1):
        self.phase += i
    __truediv__ = __div__
    __floordiv__ = __div__
    __radd__ = __add__
class waveInter:
    def __init__(self,*inwaves):
        self.waves=[self._getWave(awave) for awave in inwaves]
    def _getWave(self,awave):
        if isinstance(awave,wave):
            return awave
        elif isinstance(awave,list) or isinstance(awave, tuple):
            return wave(*awave)
        elif isinstance(awave,dict):
            return wave(**awave)
        else:
            raise TypeError("{} is not a wave. Try wave, list, tuple, or dict".format(type(awave).__name__))
    def __repr__(self):
        return "waveInter("+",".join(repr(item) for item in self.waves)+")"
    def __str__(self):
        return " + ".join(str(item) for item in self.waves)
    def __call__(self,x):
        return sum(item(x) for item in self.waves)
    def __add__(self,oth):
        return waveInter(self.waves[0]+oth,*self.waves[1:])
    def __sub__(self,oth):
        return waveInter(self.waves[0]-oth,*self.waves[1:])
    def __mul__(self,oth):
        return waveInter(*[item*oth for item in self.waves])
    def __div__(self,oth):
        return waveInter(*[item/oth for item in self.waves])
    def move(self,*xs):
        waves=[]
        if len(xs)==1:
            xs=[xs[0]]*len(self.waves)
        if len(self.waves) != len(xs):
            raise ValueError("move needs to have one x or the same number of x's as waves")
        for wave, x in zip(self.waves,xs):
            waves.append(wave+x)
        self.waves=waves
    __truediv__ = __div__
    __floordiv__ = __div__
def __notBuiltIn(out):
    a = inspect.isroutine(out) or isinstance(out,int) or isinstance(out,float) or isinstance(out,str)
    return a
def mathEval(expr):
    a=dict(inspect.getmembers(math,__notBuiltIn))
    return eval(expr,a)
 
if __name__=="__main__":
    q=quadratic(1,1,-1)
    print(repr(q))
    print(q-q)
    print(q.solve())















