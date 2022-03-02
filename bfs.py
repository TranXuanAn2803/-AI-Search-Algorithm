Left=[0,-1]
Right=[0,1]
Up=[-1,0]
Down=[1,0]
class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def __eq__(self, other): 
        if not isinstance(other, Point):            
            return NotImplemented
        return self.x == other.x and self.y == other.y
    def moveLeft(self, a, b):
        if(self.x+Left[0]>=0 and self.x+Left[0]<len(a[self.y]) and self.y+Left[1]>=0 and self.y+Left[1]<len(a)):
            if(a[self.x+Left[0]][self.y+Left[1]]!=0 and b[self.x+Left[0]][self.y+ Left[1]]==None):
                return True
        return False
    def moveRight(self, a, b):
        if(self.x+Right[0]>=0 and self.x+Right[0]<len(a[self.y]) and self.y+Right[1]>=0 and self.y+Right[1]<len(a)):
            if(a[self.x+Right[0]][self.y+Right[1]]!=0 and b[self.x+Right[0]][self.y+ Right[1]]==None):
                return True
        return False
    def moveUp(self, a, b):
        if(self.x+Up[0]>=0 and self.x+Up[0]<len(a[self.y]) and self.y+Up[1]>=0 and self.y+Up[1]<len(a)):
            if(a[self.x+Up[0]][self.y+Up[1]]!=0 and b[self.x+Up[0]][self.y+ Up[1]]==None):
                return True
        return False
    def moveDown(self, a, b):
        if(self.x+Down[0]>=0 and self.x+Down[0]<len(a[self.y]) and self.y+Down[1]>=0 and self.y+Down[1]<len(a)):
            if(a[self.x+Down[0]][self.y+Down[1]]!=0 and b[self.x+Down[0]][self.y+ Down[1]]==None):
                return True
        return False
class PointDirect:
    def __init__(self, point, direct):
        if not isinstance(point, Point):            
            return NotImplemented
        self.point= Point(point.x, point.y)
        self.direct=direct
    def __eq__(self, other): 
        if not isinstance(other, PointDirect):            
            return NotImplemented
        return self.point == other.point and self.direct == other.direct

    def findPreviousPoint(self):
        x=-1
        y=-1
        if(self.direct==1):
            x=self.point.x-Left[0]
            y=self.point.y-Left[1]
        if(self.direct==2):
            x=self.point.x-Right[0]
            y=self.point.y-Right[1]
        if(self.direct==3):
            x=self.point.x-Up[0]
            y=self.point.y-Up[1]
        if(self.direct==4):
            x=self.point.x-Down[0]
            y=self.point.y-Down[1]
        return Point(x,y)
def bfs(a, start, end):
    if(len(a)<=0 and len(a[0])<=0 and not isinstance(start, Point) and not isinstance(end, Point)):
        return None
    b= [[None for i in range(0,len(a[0]))] for j in range(0,len(a))]
    queue=[]
    queue.append(PointDirect(start, 0))
    while (len(queue)>0):
        checkPoint=queue.pop(0)
        if(b[checkPoint.point.x][checkPoint.point.y]!=None): continue
        previousPoint=checkPoint.findPreviousPoint()
        b[checkPoint.point.x][checkPoint.point.y]=previousPoint
        if(checkPoint.point ==end): 
            return b
        if(checkPoint.point.moveLeft(a,b)):
            queue.append(PointDirect(Point(checkPoint.point.x+Left[0], checkPoint.point.y+Left[1]),1))
        if(checkPoint.point.moveRight(a,b)):
            queue.append(PointDirect(Point(checkPoint.point.x+Right[0], checkPoint.point.y+Right[1]),2))
        if(checkPoint.point.moveUp(a,b)):
            queue.append(PointDirect(Point(checkPoint.point.x+Up[0], checkPoint.point.y+Up[1]),3))
        if(checkPoint.point.moveDown(a,b)):
            queue.append(PointDirect(Point(checkPoint.point.x+Down[0], checkPoint.point.y+Down[1]),4))


    return b
def findPath(b, end):
    if(b!=None and not isinstance(end, Point)):
        return (False,None)
    path=[[False for i in range(0,len(b[0]))] for j in range(0,len(b))]
    point=end 

    while(b[point.x][point.y]!=None and point.x>=0 and point.y>=0):
        path[point.x][point.y]=True
        point=b[point.x][point.y]
    if(point.x==-1 and point.y==-1): return (True,path)
    return (False,None)

a=[ [0,0,0,0,0,0,0,0,0,0],
    [0,0,1,0,1,1,1,1,1,0],
    [0,1,1,1,0,0,1,0,1,0],
    [0,1,0,1,1,0,1,1,0,0],
    [0,0,1,1,0,1,1,1,1,0],
    [0,1,1,1,1,1,0,1,0,0],
    [0,0,0,1,1,1,0,1,1,1],
    [0,1,1,1,0,1,1,0,0,0],
    [0,1,1,1,1,1,1,1,1,0],
    [0,1,0,1,0,1,0,1,1,0],
    [0,0,0,0,0,0,0,0,0,0]]
start=Point(5,3)
end=Point(6,9)
b=bfs(a,start, end)
(check,path)=findPath(b, end)
if(check): print("Having the way")
else: print("Not Having the way")
        