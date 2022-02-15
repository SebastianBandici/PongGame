import turtle
import winsound

window = turtle.Screen()
window.title("Pong Game by Sebi")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("yellow")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("green")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.4
ball.dy = -0.4

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Mami: 0       Sebi: 0", align="center", font=("Courier", 24, "normal"))


# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 25
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 25
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 25
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 25
    paddle_b.sety(y)
# Keyboard binding
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")

# Main game loop

while True: 
    window.update()

    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        #winsound.PlaySound("456563__bumpelsnake__bounce1.wav", winsound.SND_ASYNC)

    if paddle_a.ycor() > 250:
        paddle_a.sety(250)

    if paddle_a.ycor() < -250:
        paddle_a.sety(-250)

    if paddle_b.ycor() > 250:
        paddle_b.sety(250)

    if paddle_b.ycor() < -250:
        paddle_b.sety(-250)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        #winsound.PlaySound("456563__bumpelsnake__bounce1.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        ball.dx = 0.4
        ball.dy = -0.4
        pen.clear()
        pen.write("Mami: {}       Sebi: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        ball.dx = 0.4
        ball.dy = -0.4
        pen.clear()
        pen.write("Mami: {}       Sebi: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and Ball colisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        ball.dx *= 1.1
        ball.dy *= 1.1
        #winsound.PlaySound("456563__bumpelsnake__bounce1.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        #winsound.PlaySound("456563__bumpelsnake__bounce1.wav", winsound.SND_ASYNC)

    