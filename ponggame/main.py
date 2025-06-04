from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

dx = 5
dy = 5

def flytta_upp1():
    y = spelfigur1.ycor()
    y += 40
    spelfigur1.sety(y)

def flytta_ned1():
    y = spelfigur1.ycor()
    y -= 40
    spelfigur1.sety(y)

def flytta_upp2():
    y = spelfigur2.ycor()
    y += 40
    spelfigur2.sety(y)

def flytta_ned2():
    y = spelfigur2.ycor()
    y -= 40
    spelfigur2.sety(y)

spelfigur1 = Turtle()
spelfigur1.shape("square")
spelfigur1.shapesize(stretch_wid=5, stretch_len=1)
spelfigur1.color("white")
spelfigur1.penup()
spelfigur1.setposition(350, 0)

spelfigur2 = Turtle()
spelfigur2.shape("square")
spelfigur2.shapesize(stretch_wid=5, stretch_len=1)
spelfigur2.color("white")
spelfigur2.penup()
spelfigur2.setposition(-350, 0)

bollen = Turtle()
bollen.shape("circle")
bollen.color("white")
bollen.penup()
bollen.setposition(0, 0)

score1 = 0
score2 = 0

scoreboard = Turtle()
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 260)
scoreboard.write(f"{score2}   {score1}", align="center", font=("Courier", 24, "normal"))

def update_score():
    scoreboard.clear()
    scoreboard.write(f"{score2}   {score1}", align="center", font=("Courier", 24, "normal"))

screen.listen()
screen.onkey(flytta_upp1, "Up")
screen.onkey(flytta_ned1, "Down")
screen.onkey(flytta_upp2, "w")
screen.onkey(flytta_ned2, "s")

while_game_is_running = True
while while_game_is_running:
    screen.update()
    time.sleep(0.02)

    bollen.setx(bollen.xcor() + dx)
    bollen.sety(bollen.ycor() + dy)

    if bollen.ycor() > 290 or bollen.ycor() < -290:
        dy *= -1

    if bollen.xcor() > 390:
        score2 += 1
        update_score()
        bollen.goto(0, 0)
        dx *= -1

    if bollen.xcor() < -390:
        score1 += 1
        update_score()
        bollen.goto(0, 0)
        dx *= -1

    if (bollen.xcor() > 340 and bollen.xcor() < 350) and (bollen.ycor() < spelfigur1.ycor() + 50 and bollen.ycor() > spelfigur1.ycor() - 50):
        dx *= -1
        bollen.setx(340)

    if (bollen.xcor() < -340 and bollen.xcor() > -350) and (bollen.ycor() < spelfigur2.ycor() + 50 and bollen.ycor() > spelfigur2.ycor() - 50):
        dx *= -1
        bollen.setx(-340)
