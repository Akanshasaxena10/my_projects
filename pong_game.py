import turtle
import tkinter as TK
import os

'''create a window'''
wn = turtle.Screen()
wn.title('Pong_Game by akki')
wn.bgcolor('black')
wn.setup(width=800,height=600)
wn.tracer(0)

''''score'''
score_a = 0
score_b = 0

 
'''Paddle A'''
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('green')
paddle_a.shapesize(stretch_wid = 5,stretch_len = 1)
paddle_a.penup()
paddle_a.goto(-350,0)


'''paddle B'''
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('green')
paddle_b.shapesize(stretch_wid = 5,stretch_len = 1)
paddle_b.penup()
paddle_b.goto(350,0)


'''ball'''
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('red')
ball.penup()###when the movement will happen it will draw a line so using penup will solve the line formation.
ball.goto(0,0)
ball.dx = 1 #1 pixel right movement
ball.dy = -1 #1 pixel up diagonal movement

'''Pen'''
pen  = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write('Player A: 0   Player B: 0',align = 'center' ,font=('Courier',24,'normal'))




'''Function'''
def paddle_a_up():
   y = paddle_a.ycor()
   y += 20
   paddle_a.sety(y)#paddle_a set y to a new y
    
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
     

'''keyboard connection'''
wn.listen()
wn.onkeypress(paddle_a_up,'q')
wn.onkeypress(paddle_a_down,'a')  
wn.onkeypress(paddle_b_up,'Up')
wn.onkeypress(paddle_b_down,'Down')       
         

#Main game loop:
while True:
    wn.update()  
    
    ###move the ball-based on computer speed this ball movement would be impacted.
    ball.setx(ball.xcor() + ball.dx)##current position+new added pixel to move the ball.
    ball.sety(ball.ycor() + ball.dy) 
    
    ##border setup
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 
        os.system('aplay qubodup-cfork-ccby3-jump.ogg&')##toa dd sound with added & symbol so that everything will work together.
        ####to reverse the ball from the top direction,by bouncing it back
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 
        os.system('aplay qubodup-cfork-ccby3-jump.ogg&')   
        ####to reverse the ball from the bottom direct    
    if ball.xcor() > 390:
        ball.goto(0,0)###from left  to center 
        ball.dx *= -1
        score_a += 1 ####player a will get a point if ball crosses the left screen
        pen.clear()###to clear the old and give the updated score
        pen.write('Player A: {}   Player B: {}'.format(score_a,score_b),align = 'center' ,font=('Courier',24,'normal'))
    
    if ball.xcor() < -390:
        ball.goto(0,0)###from left  to center 
        ball.dx *= -1
        score_b += 1 ###player b will get a score if ball goes to the right side of the screen.
        pen.clear()###to clear the old and give the updated score
        pen.write('Player A: {}   Player B: {}'.format(score_a,score_b),align = 'center' ,font=('Courier',24,'normal'))
        
        
    ##paddle and ball collision
    '''compare x and y cor() to bounce the ball'''
    if (ball.xcor() > 340 and ball.xcor() < 350) and  (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1  
        os.system('aplay qubodup-cfork-ccby3-jump.ogg&') 
        
    if (ball.xcor() < -340 and ball.xcor() > -350) and  (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1 
        os.system('aplay qubodup-cfork-ccby3-jump.ogg&')    