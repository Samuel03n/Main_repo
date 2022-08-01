import turtle

class polygon():
    def __init__(self, sides, name):
        self.sides = sides
        self.name = name
        self.angle = (self.sides - 2)*180/self.sides

    def draw_polygon(self):
        for i in range(self.sides):
            turtle.forward(100)
            turtle.right(180 - self.angle)

    def draw_diamond(self):
        i = 1
        for i in range(self.sides):
            if i in range(1, 4, 2):
                turtle.forward(75)
                turtle.right(60)
                i += 1
            else:
                turtle.forward(100)
                turtle.right(120)
                i += 1


square = polygon(4, "square")
pentagon = polygon(5, "pentagon")
diamond = polygon(4, "diamond")
diamond.draw_diamond()
