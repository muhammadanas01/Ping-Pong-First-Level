
import turtle

wn = turtle.Screen()
wn.title("Ping Pong by @muhammadanas")
wn.bgcolor("white")
wn.setup(width = 800, height=600)
wn.tracer(0)


score = 0
life = 10
level = 2

# paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.shapesize(stretch_wid=1 ,stretch_len=8 )
paddle.penup()
paddle.goto(0, -250)


# ball A
ball_a = turtle.Turtle()
ball_a.speed(0)
ball_a.shape("circle")
ball_a.color("red")
ball_a.penup()
ball_a.goto(0,0)

        # ball B movement setting
ball_a.dx = -0.1000123
ball_a.dy = 0.102


ball_b = turtle.Turtle()
ball_b.speed(0)
ball_b.shape("circle")
ball_b.color("blue")
ball_b.penup()
ball_b.goto(0,0)

        # ball B movement setting
ball_b.dx = -0.1605
ball_b.dy = 0.125






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
wn.onkeypress(paddle_right, "d")






# main game loop
while True:
        wn.update()
        

        # moving ball
        ball_a.setx(ball_a.xcor() + ball_a.dx)
        ball_a.sety(ball_a.ycor() + ball_a.dy)

        ball_b.setx(ball_b.xcor() + ball_b.dx)
        ball_b.sety(ball_b.ycor() + ball_b.dy)



        #makinf borders for ball A
        if ball_a.ycor() > 290:
            ball_a.sety(290)
            ball_a.dy *= -1

        if ball_a.ycor() < -290:
            ball_a.goto(0,0)
            ball_a.dy *= -1
            life -=1
            pen.clear()
            pen.write(f"LEVEL: {level}  Score: {score}   Balls Left: {life}", align="center", font=('Courier',24,'bold'))
            if life == -1:
                break

        if ball_a.xcor() > 390:
            ball_a.setx(390)
            ball_a.dx *=-1

        if ball_a.xcor() < -390:
            ball_a.setx(-390)
            ball_a.dx *=-1

        # Making borders for ball B
        if ball_b.ycor() > 290:
            ball_b.sety(290)
            ball_b.dy *= -1

        if ball_b.ycor() < -290:
            ball_b.goto(0,0)
            ball_b.dy *= -1
            life -=1
            pen.clear()
            pen.write(f"LEVEL: {level}  Score: {score}   Balls Left: {life}", align="center", font=('Courier',24,'bold'))
            if life == -1:
                break

        if ball_b.xcor() > 390:
            ball_b.setx(390)
            ball_b.dx *=-1

        if ball_b.xcor() < -390:
            ball_b.setx(-390)
            ball_b.dx *=-1




        # paddle and ball coliding
        if (ball_a.ycor() < -240 and ball_a.ycor() > -250) and (ball_a.xcor() > paddle.xcor() - 40 and ball_a.xcor() < paddle.xcor() +40):
                ball_a.sety(-240)
                ball_a.dy *= -1 
                score += 1
                pen.clear()
                pen.write(f"LEVEL: {level}  Score: {score}   Balls Left: {life}", align="center", font=('Courier',24,'bold'))


        if (ball_b.ycor() < -240 and ball_b.ycor() > -250) and (ball_b.xcor() > paddle.xcor() - 40 and ball_b.xcor() < paddle.xcor() +40):
                ball_b.sety(-240)
                ball_b.dy *= -1 
                score += 1
                pen.clear()
                pen.write(f"LEVEL: {level}  Score: {score}   Balls Left: {life}", align="center", font=('Courier',24,'bold'))

