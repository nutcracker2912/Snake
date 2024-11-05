from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(x=0, y=270)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", move=False, align="center",
                   font=("Courier", 20, "normal"))

    def game_over(self):
        game_over = Turtle()
        game_over.color("white")
        game_over.hideturtle()
        game_over.write(f"Game Over your score is {self.score}", move=False, align="center",
                        font=("Arial", 20, "normal"))

    def add_one_to_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
