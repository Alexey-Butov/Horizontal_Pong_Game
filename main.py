import turtle


def main():
    wn = turtle.Screen()
    wn.title("Pong by Alexey Butov")
    wn.bgcolor('black')
    wn.setup(1024, 768, 250, 0)
    wn.addshape('assets/pingpongbat.gif')
    wn.addshape('assets/pingpongball.gif')
    wn.tracer(0)

    # Score
    score_a = 0
    score_b = 0
    status_bar = "Player A : {}       |        Player B : {}"
    underline = "______________________________________________________"

    # Status Bar
    status = turtle.Turtle()
    status.speed(0)
    status.shape("square")
    status.color("white")
    status.hideturtle()
    status.goto(0, 340)
    status.penup()
    status.clear()
    status.write(status_bar.format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    status.write(underline, align="center", font=("Courier", 24, "normal"))

    # bat A
    bat_a = turtle.Turtle()
    bat_a.speed(0)
    bat_a.shape('assets/pingpongbat.gif')
    bat_a.penup()
    bat_a.goto(0, -350)
    bat_a.clear()

    # bat B
    bat_b = turtle.Turtle()
    bat_b.speed(0)
    bat_b.shape('assets/pingpongbat.gif')
    bat_b.penup()
    bat_b.goto(0, 300)
    bat_b.clear()

    # Ball
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape('assets/pingpongball.gif')
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 0.2
    ball.dy = 0.2
    ball.clear()

    canvas = turtle.getcanvas()

    # Functions
    def paddle_a_right():
        x = bat_a.xcor()
        x += 20
        bat_a.setx(x)

    def paddle_a_left():
        x = bat_a.xcor()
        x -= 20
        bat_a.setx(x)

    def paddle_b_right():
        x = bat_b.xcor()
        x += 20
        bat_b.setx(x)

    def paddle_b_left():
        x = bat_b.xcor()
        x -= 20
        bat_b.setx(x)

    # Keyboard bindings
    wn.listen()
    wn.onkeypress(paddle_a_right, "d")
    wn.onkeypress(paddle_a_left, "a")
    wn.onkeypress(paddle_b_right, "Right")
    wn.onkeypress(paddle_b_left, "Left")

    # Main game loop
    while True:
        wn.update()

        if canvas.winfo_exists():
            bat_a.setx(canvas.winfo_pointerx() - 800)
        else:
            canvas.destroy()

        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border checking

        # Top and bottom
        if ball.xcor() > 485:
            ball.setx(485)
            ball.dx *= -1

        elif ball.xcor() < -490:
            ball.setx(-490)
            ball.dx *= -1

        # Left and right
        if ball.ycor() > 290:
            score_a += 1
            status.clear()
            status.write(status_bar.format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
            status.write(underline, align="center", font=("Courier", 24, "normal"))
            ball.goto(0, 0)
            ball.dy *= -1

        elif ball.ycor() < -335:
            score_b += 1
            status.clear()
            status.write(status_bar.format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
            status.write(underline, align="center", font=("Courier", 24, "normal"))
            ball.goto(0, 0)
            ball.dy *= -1

        # Paddle and ball collisions
        if ball.ycor() < -325 and bat_a.xcor() + 70 > ball.xcor() > bat_a.xcor() - 70:
            ball.dy *= -1

        elif ball.ycor() > 280 and bat_b.xcor() + 70 > ball.xcor() > bat_b.xcor() - 70:
            ball.dy *= -1

        # AI Player
        if bat_b.xcor() < ball.xcor() and abs(bat_b.xcor() - ball.xcor()) > 20:
            paddle_b_right()

        elif bat_b.xcor() > ball.xcor() and abs(bat_b.xcor() - ball.xcor()) > 20:
            paddle_b_left()


if __name__ == "__main__":
    main()
