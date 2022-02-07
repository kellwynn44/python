#pong python game made with @TokyoEdTech's YouTube tutorial
import turtle
import winsound
#import os -> for linux and apple
#use with: os.system("aplay bounce.wav&") OR os.system("afplay bounce.wav&")
#sound file needs to be in same folder as this file

win = turtle.Screen()
win.title("Pong by @kellwynn44")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(1) #maximum speed
paddle_a.shape("square")
paddle_a.color("green")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0) #start position

#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(1)
paddle_b.shape("square")
paddle_b.color("yellow")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = .2  #speed that the ball moves right 
ball.dy = .2  #speed that the ball moves up 

#scores
score_a = 0
score_b = 0

#pen (scoreboard)
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()   #so you don't see a moving line
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

#functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20    #adds 20px to y
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20    #subtracts 20px from y
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20    #adds 20px to y
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20    #subtracts 20px from y
    paddle_b.sety(y)

#keyboard binding
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")      #up arrow key
win.onkeypress(paddle_b_down, "Down")  #down arrow key

#main game loop
while True:
    win.update()    
    ball.setx(ball.xcor() + ball.dx)    #move x coordinate of ball
    ball.sety(ball.ycor() + ball.dy)    #move y coordinate of ball
    if ball.ycor() > 290:   #adding a top border for the ball
        ball.sety(290)
        ball.dy *= -1       #reverses ball's position
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC) #add bounce sound
    if ball.ycor() < -290:  #adding a bottom border for the ball
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if ball.xcor() > 425:   #what to do if the ball goes off the right side
        ball.goto(0,0)      #send ball back to the middle of the screen
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    if ball.xcor() < -425:  #what to do if the ball goes off the left side
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)