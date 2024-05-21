from turtle import Screen
from paddle import Paddle
from ball import Ball
from brick import Brick
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout!")
screen.tracer(0)

paddle = Paddle()
ball = Ball()
scoreboard = Scoreboard()
bricks = Brick()

screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")

ball.reset_position()
bricks.create_bricks()
game_is_on = True

while game_is_on:
    screen.update()
    ball.move()
    # Detect collision with side walls
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.bounce_x()

    # Detect collision with paddle
    if ball.distance(paddle) < 65 and ball.ycor() < -220:
        ball.bounce_y()

    # Detect collision with top wall
    if ball.ycor() > 290:
        ball.bounce_y()

    # Detect paddle miss
    if ball.ycor() < -290:
        ball.reset_position()
        scoreboard.lose_life()

    # Detect collision with brick
    for brick in bricks.all_bricks:
        if brick.distance(ball) < 35 and brick.color()[1] == "green":
            scoreboard.update_score(4)
            brick.goto(800, 800)
            bricks.all_bricks.remove(brick)
            ball.bounce_y()
        elif brick.distance(ball) < 35 and brick.color()[1] == "yellow":
            scoreboard.update_score(5)
            brick.goto(800, 800)
            bricks.all_bricks.remove(brick)
            ball.bounce_y()
        elif brick.distance(ball) < 35 and brick.color()[1] == "orange":
            scoreboard.update_score(6)
            brick.goto(800, 800)
            bricks.all_bricks.remove(brick)
            if ball.speed == 2:
                ball.speed *= 4
            ball.bounce_y()
        elif brick.distance(ball) < 35 and brick.color()[1] == "red":
            brick.goto(800, 800)
            bricks.all_bricks.remove(brick)
            scoreboard.update_score(7)
            if ball.speed == 2:
                ball.speed *= 4
            ball.bounce_y()

    # Check lives and end game if lives = 0
    if scoreboard.lives == 0:
        game_is_on = False
        scoreboard.you_lose()

    # Check if score is maxed or bricks are all gone
    if scoreboard.score == 440 or len(bricks.all_bricks) == 0:
        game_is_on = False
        scoreboard.you_win()

screen.exitonclick()
