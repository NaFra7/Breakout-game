from turtle import Turtle


class Brick:
    def __init__(self):
        self.all_bricks = []

    def create_bricks(self):
        for num in range(80):
            x_val = num * 40
            x_cor = -380 + x_val
            if num <= 20:
                brick_g = Turtle("square")
                brick_g.color("black", "green")
                brick_g.shapesize(stretch_wid=2, stretch_len=2, outline=1)
                brick_g.penup()
                brick_g.goto(x_cor, 0)
                self.all_bricks.append(brick_g)
            if num <= 40:
                brick_y = Turtle("square")
                brick_y.color("black", "yellow")
                brick_y.penup()
                brick_y.goto(x_cor, 40)
                brick_y.shapesize(stretch_wid=2, stretch_len=2, outline=1)
                self.all_bricks.append(brick_y)
            if num <= 60:
                brick_o = Turtle("square")
                brick_o.color("black", "orange")
                brick_o.penup()
                brick_o.goto(x_cor, 80)
                brick_o.shapesize(stretch_wid=2, stretch_len=2, outline=1)
                self.all_bricks.append(brick_o)
            if num <= 80:
                brick_r = Turtle("square")
                brick_r.color("black", "red")
                brick_r.penup()
                brick_r.goto(x_cor, 120)
                brick_r.shapesize(stretch_wid=2, stretch_len=2, outline=1)
                self.all_bricks.append(brick_r)

