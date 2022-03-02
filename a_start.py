import math

Left=[0,-1]
Right=[0,1]
Up=[-1,0]
Down=[1,0]
class Point:
    def __init__(self, x, y, distance=0):
        self.x=x
        self.y=y
        self.distance=distance
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
    def heuristic(self, end):
        heuris=(self.x-end.x)*(self.x-end.x)+(self.y-end.y)*(self.y-end.y)
        return math.sqrt(heuris)


class PointDirect:
    def __init__(self, point, direct):
        if not isinstance(point, Point):            
            return NotImplemented
        self.point= Point(point.x, point.y, point.distance)
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
class PriorityQueue:
    def __init__(self):
        self.queue = []
    def empty(self):
        return len(self.queue) == 0
  
  
    def insert(self,f,pointdirect):
        if not isinstance(pointdirect, PointDirect):
            return NotImplemented
                    
        for i in range(len(self.queue)):
            if (pointdirect.point==self.queue[i][1].point):
                if(f >=self.queue[i][0]):
                    return
        self.queue.append((f, pointdirect))
  
    def pop(self):
        
        try:
            min = 0
            for i in range(len(self.queue)):
                if self.queue[i][0] < self.queue[min][0]:
                    min = i
            item = self.queue[min]
            del self.queue[min]
            return item[1]
        except IndexError:
            print()
            exit()

def a_start(a, start, end):
    if(len(a)<=0 and len(a[0])<=0 and not isinstance(start, Point) and not isinstance(end, Point)):
        return None
    start.distance=0
    b= [[None for i in range(0,len(a[0]))] for j in range(0,len(a))]
    queue = PriorityQueue()
    f=start.heuristic(end)+start.distance
    queue.insert(f,PointDirect(start, 0))
    while not queue.empty():
        checkPoint=queue.pop()
        if(b[checkPoint.point.x][checkPoint.point.y]!=None): continue
        previousPoint=checkPoint.findPreviousPoint()
        b[checkPoint.point.x][checkPoint.point.y]=previousPoint
        if(checkPoint.point ==end): 
            return (b,checkPoint.point.distance)
            
        if(checkPoint.point.moveLeft(a,b)):
            leftPoint=Point(checkPoint.point.x+Left[0], checkPoint.point.y+Left[1],checkPoint.point.distance+1)

            f=leftPoint.heuristic(end)+leftPoint.distance
            queue.insert(f,PointDirect(leftPoint,1))
        if(checkPoint.point.moveRight(a,b)):
            rightPoint=Point(checkPoint.point.x+Right[0], checkPoint.point.y+Right[1],checkPoint.point.distance+1)
            f=rightPoint.heuristic(end)+rightPoint.distance
            queue.insert(f,PointDirect(rightPoint,2))
        if(checkPoint.point.moveUp(a,b)):
            upPoint=Point(checkPoint.point.x+Up[0], checkPoint.point.y+Up[1],checkPoint.point.distance+1)
            f=upPoint.heuristic(end)+upPoint.distance
            queue.insert(f,PointDirect(upPoint,3))
        if(checkPoint.point.moveDown(a,b)):
            downPoint=Point(checkPoint.point.x+Down[0], checkPoint.point.y+Down[1],+checkPoint.point.distance+1)
            f=downPoint.heuristic(end)+downPoint.distance
            queue.insert(f,PointDirect(downPoint,4))
    return (b,-1)
def findPath(b, end):
    if(b!=None and not isinstance(end, Point)):
        return (False,None)
    path=[["0" for i in range(0,len(b[0]))] for j in range(0,len(b))]
    prevPoint=None
    point=end 
    while(b[point.x][point.y]!=None and point.x>=0 and point.y>=0):
        if(point.x==-1 and point.y==-1): break
        if(prevPoint!=None):
            if(prevPoint.x-point.x>0):
                path[point.x][point.y]="V"
            else:
                if(prevPoint.x-point.x<0):
                    path[point.x][point.y]="^"
                else:
                    if(prevPoint.y-point.y>0):
                        path[point.x][point.y]=">"
                    else:
                        if(prevPoint.y-point.y<0):
                            path[point.x][point.y]="<"
        prevPoint=point
        point=b[point.x][point.y]
    if(point.x==-1 and point.y==-1): return (True,path)
    return (False,None)
a=[ [0,0,0,0,0,0,0,0,0,0],
    [1,1,0,1,1,1,0,0,0,0],
    [0,1,0,1,0,1,1,1,1,0],
    [0,1,0,1,0,1,1,0,1,0],
    [0,1,1,1,0,1,1,0,1,0],
    [0,1,1,1,1,1,1,0,1,0],
    [0,1,0,1,1,0,0,1,1,0],
    [0,1,1,1,1,0,0,0,1,0],
    [0,1,1,1,1,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0]]
start=Point(6,8)
end=Point(1,0)
(b,distance)=a_start(a,start, end)

(check,path)=findPath(b, end)
for i in range(0, len(path)):
    for j in range(0, len(path[0])):
        print(path[i][j], end=" ")
    print()
if(check): print("Having the way with distance: ", distance)
else: print("Not Having the way")
        