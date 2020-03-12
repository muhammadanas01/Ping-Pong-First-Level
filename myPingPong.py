import turtle

wn = turtle.Screen()
wn.title("Ping Pong by @muhammadanas")
wn.bgcolor("white")
wn.setup(width = 800, height=600)
wn.tracer(0)


score = 0
life = 5
level = 1


# paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.shapesize(stretch_wid=1 ,stretch_len=5 )
paddle.penup()
paddle.goto(0, -250)




# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0,0)


# ball movement setting
ball.dx = -0.1605
ball.dy = 0.125



# scoring
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write(f"LEVEL: {level}  Score: 0   Balls Left: 5", align="center", font=('Courier',24,'bold'))



# functions
def paddle_left():
    x = paddle.xcor()
    x -=20
    paddle.setx(x)

def paddle_right():
    x = paddle.xcor()
    x +=20
    paddle.setx(x)



# key binding
wn.listen()
wn.onkeypress(paddle_left, "Left")
wn.onkeypress(paddle_right, "Right")
wn.onkeypress(paddle_left, "a")
wn.onkeypress(paddle_left, "d")





# main game loop
while True:
    wn.update()

    # moving ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)



    #makinf borders
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.goto(0,0)
        ball.dy *= -1
        life -=1
        pen.clear()
        pen.write(f"LEVEL: {level}  Score: {score}   Balls Left: {life}", align="center", font=('Courier',24,'bold'))
        if life == -1:
            break

    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *=-1

    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *=-1

    # paddle and ball coliding
    if (ball.ycor() < -240 and ball.ycor() > -250) and (ball.xcor() > paddle.xcor() - 40 and ball.xcor() < paddle.xcor() +40):
            ball.sety(-240)
            ball.dy *= -1 
            score += 1
            pen.clear()
            pen.write(f"LEVEL: {level}  Score: {score}   Balls Left: {life}", align="center", font=('Courier',24,'bold'))

