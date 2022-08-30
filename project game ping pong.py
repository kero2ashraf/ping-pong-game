#imported turtle module
import turtle

wind = turtle.Screen() #to intialize screen
wind.title("ping pong by kero") #set the tittle of the window
wind.bgcolor("white")
wind.setup( width=800 , height=600) #set the demensions
wind.tracer(0) #stops the window from updating auto

#madrab1
madrab1 = turtle.Turtle() #intializes turtle object(shape)
madrab1.speed(0) #set the spped of the animation
madrab1.shape("square") #set the shape of the object
madrab1.color("blue")  #set the color of the shape
madrab1.shapesize(stretch_wid=5 , stretch_len=1) #streches the shape to meet the size
madrab1.penup() #stops the object from drowing lines
madrab1.goto(-350,0)  #set the position of the object
#madrab2
madrab2 = turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("red")
madrab2.shapesize(stretch_wid=5 , stretch_len=1)
madrab2.penup() 
madrab2.goto(350,0) 

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("black")
ball.penup() 
ball.goto(0,0)
ball.dx = 0.2
ball.dy = 0.2

#score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("black")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write(" player1 :0 player2 : 0" , align="center" , font=("courier", 24 ,"normal" ))

#fucntions
def madrab1_up():
    y = madrab1.ycor() #set the y coordinate of madrab1
    y += 20 #set the y to increase by 20
    madrab1.sety(y) #set the y of the madrab1 to the new y coordinate

def madrab1_down():
    y = madrab1.ycor()
    y -= 20  #set the y to decrease by 20
    madrab1.sety(y)

def madrab2_up():
    y = madrab2.ycor()
    y += 20
    madrab2.sety(y)

def madrab2_down():
    y = madrab2.ycor()
    y -= 20
    madrab2.sety(y)

#keybord bindings
wind.listen() #tell the window to expect input
wind.onkeypress(madrab1_up,"w") # when pressing w the function madrab1_up is invoked
wind.onkeypress(madrab1_down,"s")
wind.onkeypress(madrab2_up,"Up")
wind.onkeypress(madrab2_down,"Down")
#main game loop
while True:
    wind.update() #update the screen everytime


    #move the ball
    ball.setx(ball.xcor() + ball.dx) #ball starts at 0 and everytime loop run ...> +0.3 xaxis
    ball.sety(ball.ycor() + ball.dy) #ball starts at 0 and everytime loop run ...> +0.3 yaxis
    
    #border check , top border +300px , bottom border -300px , ball is 20 px
    if ball.ycor() > 290: # if ball is at top border
        ball.sety(290) #set y coordinate +290
        ball.dy *= -1 #reverse direction , making +0.3 .....> -0.3


    if ball.ycor() < -290: #if ball is at bottom border
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390 : # if ball is at right border
        ball.goto(0,0) #return ball to center
        ball.dx *= -1 #reverse the x direction
        score1 +=1
        score.clear()
        score.write(" player1 :{} player2 : {}".format(score1,score2) , align="center" , font=("courier", 24 ,"normal" ))

    if ball.xcor() < -390 : # if ball is at left border
        ball.goto(0,0)
        ball.dx *= -1
        score2 +=1
        score.clear()
        score.write(" player1 :{} player2 : {}".format(score1,score2) , align="center" , font=("courier", 24 ,"normal" ))
    
    #tasdom madrab and ball
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < madrab2.ycor() + 40 and ball.ycor() > madrab2.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < madrab1.ycor() + 40 and ball.ycor() > madrab1.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1