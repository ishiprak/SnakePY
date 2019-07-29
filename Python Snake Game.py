# -*- coding: utf-8 -*-
"""

@author: Shivam Prakash (https://github.com/ishiprak)

"""
#**************************************** --Developed and created by SHIVAM PRAKASH-- **********************************************# 

# All module imports--
import turtle
import random
import time

# Making the canvas--
delay=0.35
i=1
j=0
score=high_score=prev_score=0
x=y=1
scr=turtle.Screen()
scr.bgcolor("green")
scr.setup(width=750, height=700)
#scr.tracer(0)

# Making the head (alex)--
alex=turtle.Turtle()
alex.color("white")
alex.shape("triangle")
alex.up()
alex.speed(0)
alex.goto(0,0)
#alex.shapesize(2)
#alex.write("Pervious Score: 0 Score: 0  High Score: 0", align="center", font=("Courier", 10, "normal"))
snake=list()
snake.append(alex)
#key = cv2.waitKey(1) & 0xFF
#print(key)

# Pening the score panel--
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(145, 317)
pen.write("Previous Score: 0 Score: 0  High Score: 0", align="center", font=("Courier", 11, "normal"))


# Pening the credit panel and name bar--
sp = turtle.Turtle()
sp.speed(0)
sp.shape("square")
sp.color("white")
sp.penup()
sp.hideturtle()
sp.goto(0,-310)
sp.write("Made with 'Love' By Shivam Prakash.", align="center", font=("Courier", 11, "normal"))

# Bordering the play area--
border=turtle.Turtle()
border.shape(None)
border.hideturtle()
border.up()
border.goto(-345,300)
border.pensize(2)
border.color("black")
border.speed(0)
border.down()
border.forward(685)
border.right(90)
border.forward(625)
border.right(90)
border.forward(685)
border.right(90)
border.forward(625)

# Making the food (turtle)--
food=turtle.Turtle()
food.color("black")
food.shape("circle")
food.up()
food.speed(0)
seed_x=random.randint(-280,300)
seed_y=random.randint(-280,275)
food.goto(seed_x,seed_y)
"""while True:
    alex.forward(10)
while(True):
    seed=random.randint(0,100)
    dir=random.randint(1,5)
    if dir==1:
        alex.forward(seed)
    elif dir==2:
        alex.backward(seed)
    elif dir==3:
        alex.right(seed)
    elif dir==4:
        alex.left(seed)"""
        
# Main Play Loop--
while True:
    
    # Defining user input functions--
    def move_up():
        if alex.heading()!=270:
            alex.setheading(90)
            """for seg in snake[1:]:
                seg.setheading(90)"""
    def move_down():
        if alex.heading()!=90:
            alex.setheading(270)
            """for seg in snake[1:]:
                seg.setheading(270)"""
        #alex.forward(50)
    def move_left():
        if alex.heading()!=0:
            alex.setheading(180)
            """for seg in snake[1:]:
                seg.setheading(180)"""
        #alex.forward(50)
    def move_right():
        if alex.heading()!=180:
            alex.setheading(0)
            """for seg in snake[1:]:
                seg.setheading(0)"""
                
    # Making the snake segments--         
    def make_snake(seg):
        seg.speed(0)
        seg.up()
        seg.shape("circle")
        """x=snake[i-1].xcor()
        y=snake[i-1].ycor()
        snake[i].goto(x,y) """                              
        #i=random.randint(10,50)
        #seg.forward(i)
        """if(alex.heading()==0):
            seg.goto(alex.xcor()-x,alex.ycor())
            seg.setheading(0)
            x+=1
            return x,y
        elif(alex.heading()==90):
            seg.goto(alex.xcor(),alex.ycor()-y)
            seg.setheading(90)
            y+=1
            return x,y
        elif(alex.heading()==180):
            seg.goto(alex.xcor()+x,alex.ycor())
            seg.setheading(180)
            x+=1
            return x,y
        elif(alex.heading()==270):
            seg.goto(alex.xcor(),alex.ycor()+y) 
            seg.setheading(270)
            y+=1
            return x,y"""
   
    # Taking user_inputs--
    scr.listen()
    scr.onkeypress(move_up, "8")
    scr.onkeypress(move_down, "2")
    scr.onkeypress(move_left, "4")
    scr.onkeypress(move_right, "6")
    
    #print("***************************************"+alex.position+"******************************************")
    colors=["red","yellow","orange","black","white","blue"]
    if food.color()==("red","red"):
            if j==0:
                start_time=time.time()
            elapsed_time=time.time()-start_time
            if (int(elapsed_time)<11):
                if(j%2==0):
                    food.shapesize(2)
                else:
                    food.shapesize(1)
            else:
                food.shapesize(1)
                index=random.randint(0,5)
                food.color(colors[index])
                seed_x=random.randint(-280,300)
                seed_y=random.randint(-280,275)
                food.goto(seed_x,seed_y)
            j+=1
    else:
        j=0
    
    # Defining collision with food--
    if(alex.distance(food)<20):
        snake.append(turtle.Turtle())
        make_snake(snake[i])
        seed_x=random.randint(-280,300)
        seed_y=random.randint(-280,275)
        if food.color()==("orange","orange"):
            score+=2
        elif food.color()==("yellow","yellow"):
            score+=5
        elif (food.color()==("white","white") or food.color()==("black","black")):
            score+=10
        elif food.color()==("blue","blue"):
            score+=15
        elif food.color()==("red","red"):
            food.shapesize(1)
            score+=20
        index=random.randint(0,5)
        food.color(colors[index])
        food.goto(seed_x,seed_y)
        delay-=0.05
        #score+=10
        pen.clear()
        pen.write("Previous Score: {} Score: {}  High Score: {}".format(prev_score,score,high_score), align="center", font=("Courier", 11, "normal"))
        i+=1
        #$alex.home()
        
    # Defining collision of head (alex) with body--    
    for seg in snake[2:]:
        if seg.distance(alex)<10:
            time.sleep(1)
            alex.goto(0,0)
            food.clear()
            for seg in snake[1:]:
                seg.goto(1000,1000)
            snake.clear()
            snake.append(alex)
            seed_x=random.randint(-280,300)
            seed_y=random.randint(-280,275)
            food.goto(seed_x,seed_y)
            i=1
            prev_score=score
            delay=0.35
            score=0
            food.shapesize(1)
            pen.clear()
            pen.write("Previous Score: {} Score: {}  High Score: {}".format(prev_score,score,high_score), align="center", font=("Courier", 11, "normal"))
     
    # Updating high score--    
    if score>high_score:
        high_score=score
        pen.clear()
        pen.write("Previous Score: {} Score: {}  High Score: {}".format(prev_score,score,high_score), align="center", font=("Courier", 11, "normal"))
    
    # Defining collision with play area boundary--            
    if(alex.xcor()<-315 or alex.xcor()>318 or alex.ycor()<-298 or alex.ycor()>275):
        time.sleep(1)
        alex.goto(0,0)
        food.clear()
        for seg in snake[1:]:
            seg.goto(1000,1000)
        snake.clear()
        snake.append(alex)
        seed_x=random.randint(-280,300)
        seed_y=random.randint(-280,275)
        food.goto(seed_x,seed_y)
        i=1
        prev_score=score
        score=0
        delay=0.35
        food.shapesize(1)
        pen.clear()
        pen.write("Previous Score: {} Score: {}  High Score: {}".format(prev_score,score,high_score), align="center", font=("Courier", 11, "normal"))
        #alex.home()
        
    # Moving the body--
    if len(snake)>1:   
        for m in range(len(snake)-1,0,-1):
            x=snake[m-1].xcor()
            y=snake[m-1].ycor()
            if m%2==0:
                snake[m].color("white")
            else:
                snake[m].color("black")
            snake[m].speed(0)
            snake[m].up()
            snake[m].shape("circle")
            snake[m].goto(x,y)    
    
    # Moving the snake--
    alex.fd(20)
   
    # Defining the delay for consecutive pace speeding--
    if(delay>=0.00):
        time.sleep(delay)
        
scr.exitonclick()

#**************************************************END OF PROGRAM****************************************************#

#**************************************** --Developed and created by SHIVAM PRAKASH-- **********************************************#











