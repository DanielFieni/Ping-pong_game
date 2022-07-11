from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.right_score = 0
        self.left_score = 0
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.left_score}", align='center', font=('Courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(f"{self.right_score}", align='center', font=('Courier', 80, 'normal'))
    
    def left_point(self):
        self.left_score += 1
        self.update_score()
    
    def right_point(self):
        self.right_score += 1
        self.update_score() 