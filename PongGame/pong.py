# Simple Pong in Python 3 for Beginners (Turtle Python Module)

import turtle
import time

wn = turtle.Screen()
wn.title("Pong by Benjamin Ortiz Jr.")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score 
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("limegreen")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("limegreen")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("limegreen")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = -0.3                   #Ball speed - Low number is slow, higher number is faster. Both ball.dx and ball.dy should be the same. Ranges = 0.1 - 0.9 || 1 - 9.

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("limegreen")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player1: 0  Player2: 0", align="center", font=("Courier", 24, "bold"))

pen1 = turtle.Turtle()
pen1.speed(0)
pen1.color("limegreen")
pen1.penup()
pen1.hideturtle()
pen1.goto(0, -290)
pen1.write("Created By: Benjamin Ortiz Jr.", align="center", font=("Courier", 10, "normal"))

# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player1: {}  Player2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))
        if score_a == 10:
            pen2 = turtle.Turtle()
            pen2.speed(0)
            pen2.color("limegreen")
            pen2.penup()
            pen2.hideturtle()
            pen2.goto(0, -30)
            pen2.write("  Game Over\nPlayer1 Wins!", align="center", font=("Courier", 24, "bold"))
            time.sleep(10)
            quit()
             
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player1: {}  Player2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))
        if score_b == 10:
            pen2 = turtle.Turtle()
            pen2.speed(0)
            pen2.color("limegreen")
            pen2.penup()
            pen2.hideturtle()
            pen2.goto(0, -30)
            pen2.write("  Game Over\nPlayer2 Wins!", align="center", font=("Courier", 24, "bold"))
            time.sleep(10)
            quit()
            
    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1