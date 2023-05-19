class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"({self.x}, {self.y})")
    
    def set(self,x,y):
        self.x = x
        self.y = y

    def get(self):
        return (self.x, self.y)

class Rectangle:
    def __init__(self,x1,y1,x2,y2):
        self.__lt = Point(x1,y1)
        self.__rb = Point(x2,y2)

    def show(self):
        self.__lt.show()
        self.__rb.show()
    
    def getWidth(self):
        w = self.__rb.x - self.__lt.x 
        return w
    
    def getHeight(self):
        h = self.__rb.y - self.__lt.y
        return h
    
    def getArea(self):
        return self.getWidth() * self.getHeight()

    def getPerimeter(self):
        return self.getWidth() + self.getWidth() + self.getHeight() + self.getHeight()
    
r1 = Rectangle(5,5,20,10)
a = r1.getArea()
p = r1.getPerimeter()

r1.show()
print(f"\n넓이는 {a}, 둘레는 {p}")
