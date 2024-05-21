from turtle import Turtle


class Brick(Turtle):

    def __init__(self, color, border):
        super().__init__()
        self.shape("square")
        self.color(border, color)
        self.shapesize(stretch_wid=2, stretch_len=2, outline=1)
        self.penup()

    def delete(self):
        self.goto(800, 800)

    def create_bricks(self):
        for num in range(80):
            x_val = num * 40
            x_cor = -380 + x_val
            if num <= 20:
                brick_g = Turtle()
                brick_g.color("green", "black")
                brick_g.goto(x_cor, 20)
            if num <= 40:
                brick_y = Brick("yellow", "black")
                brick_y.goto(x_cor, 60)
            if num <= 60:
                brick_o = Brick("orange", "black")
                brick_o.goto(x_cor, 100)
            if num <= 80:
                brick_r = Brick("red", "black")
                brick_r.goto(x_cor, 140)