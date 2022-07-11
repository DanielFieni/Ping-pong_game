from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Ping Pong')
screen.tracer(0)

paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkeypress(paddle_right.move_up, 'Up')
screen.onkeypress(paddle_right.move_down, 'Down')
screen.onkeypress(paddle_left.move_up, 'w')
screen.onkeypress(paddle_left.move_down, 's')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.reverse_y()
    
    if ball.distance(paddle_right) < 40 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.reverse_x()

    if ball.xcor() > 380:
        ball.reset_ball()
        score.left_point()

    if ball.xcor() < -380:
        ball.reset_ball()
        score.right_point()

screen.exitonclick()
