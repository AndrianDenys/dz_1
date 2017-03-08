#1
class Classroom(Object):
    def __init__(self, number, capacity, equipment):
        self.number = number
        self.capacity = capacity
        self.equipment = equipment
    def is_larger(self, classroom):
        if self.capacity is > classroom.capacity:
            return True
        else:
            return False
    def equipment_differences(self, classroom):
        i = 0
        res = []
        while i < len(self.equipment):
            if self.equipment[i] is not in classroom.equipment:
                res.append(self.equipment[i])
                i+= 1
            else:
                i += 1
    def str(self):
        print "Classroom %s has a capacity of %s persons and has the following equipment: %s. " % (self.number, self.capacity, self.equipment)
    def repr(self):
        a = "Classroom(%s, %s, %s)" %(self.number, self.capacity, self.equipment)
        return a
#2
class AcademicBuilding(Building):
    def __init__(self, adress, classrooms):
        super(self.__class__, self).__init__(adress)
        self.classrooms = classrooms
    def total_equipment(self, classrooms):
        total = []
        i = 0
        j = 0
        while i < len(classrooms):
            while j < len(self.classrooms[i].equipment)
                total.append(self.classrooms[i].equipment[j])
                j += 1
            i += 1
            j = 0
    def str(self, classrooms):
        print(self.adress)
        i = 0
        while i < len(self.classrooms):
            classrooms[i].repr()
            i += 1

#3
class Point:
    'Represents a point in two-dimensional geometric coordinates'
    def __init__(self, x=0, y=0):
        '''Initialize the position of a new point. The x and y coordinates can be
        specified. If they are not, the point defaults to the origin.'''
        self.move(x, y)
    def move(self, x, y):
        "Move the point to a new location in 2D space."
        self.x = x
        self.y = y
    def rotate(self, beta, other_point):
        'Rotate point around other point’
        dx = self.x - other_point.get_xposition()
        dy = self.y - other_point.get_yposition()
        beta = radians(beta)
        xpoint3 = dx * cos(beta) - dy * sin(beta)
        ypoint3 = dy * cos(beta) + dx * sin(beta)
        xpoint3 = xpoint3 + other_point.get_xposition()
        ypoint3 = ypoint3 + other_point.get_yposition()
        return self.move(xpoint3, ypoint3)
    def get_xposition(self):
        return self.x
    def get_yposition(self):
        return self.y
#Whatthehell
#    def add(self):
#        pass
#    def iadd(self):
#        pass
#    def sub(self):
#        pass
#    def isub(self):
#        pass

#4
class Triangle(Object):
    def __init__(self, point1, point2, point3):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
    def is_triangle(self):
        #(x - x1)/(x2 - x1) == (y - y1)/(y2 - y1)
        # There is always triangle between 3 points EXCEPT this points are on th one line
        if (point3.get_xposition() - point1.get_xposition()) / (point2.get_xposition - point1.get_xposition()) == (point3.get_yposition() - point1.get_yposition()) / (point2.get_yposition - point1.get_yposition()):
            return False
        else:
            return True
    def perimeter(self):
        import Math
        #line = sqrt((x1 - x2)^2 + (y1 - y2)^2)
        pass
#5
class Building(Object):
    def __init__(self, building, adress):
        self.building = building
        self.adress = adress
class House(Building):
    def __init__(self, adress, rooms):
        super(self.__class__, self).__init__(adress)
        self.rooms = rooms
