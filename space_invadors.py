import turtle
import math
import random
import sys
import time


class Enemy( turtle.Turtle ):
    enemy_speed = 1


e = [ ]


def draw_frame():
    for i in range( 2 ):
        frame_pen.forward( 1200 )
        frame_pen.left( 90 )
        frame_pen.forward( 800 )
        frame_pen.left( 90 )


def make_enemies():
    enemy = Enemy()
    e.append( enemy )
    enemy.color( "red" )
    enemy.shape( "arrow" )
    enemy.degrees(90)
    enemy.penup()
    enemy.speed( 0 )
    x = random.randint( -570 , 570 )
    y = random.randint( 190 , 350 )
    enemy.setposition( x , y )
    enemy.setheading( 0 )


def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -570:
        x = -570
    player.setx( x )


def move_right():
    x = player.xcor()
    x += player_speed
    if x > 570:
        x = 570
    player.setx( x )


def fire_bullet():
    global bullet_state
    if bullet_state == "ready":
        bullet_state = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition( x , y )
        bullet.showturtle()


def is_collision( t1 , t2 ):
    distance = math.sqrt( math.pow( t1.xcor() - t2.xcor() , 2 ) + math.pow( t1.ycor() - t2.ycor() , 2 ) )
    if distance < 15:
        return True
    else:
        return False


wn = turtle.Screen()
wn.setup( width=.75 , height=.90 , startx=0 , starty=0 )
wn.title( "Space Invaders" )
wn.bgcolor( "black" )
wn.tracer( 30 )

frame_pen = turtle.Turtle()
frame_pen.pen( fillcolor="white" , pencolor="purple" , pensize=6 )
frame_pen.speed( 0 )
frame_pen.penup()
frame_pen.setposition( -600 , -400 )
frame_pen.pendown()
draw_frame()

player_speed = 15
bullet_speed = 20

player = turtle.Turtle()
bullet = turtle.Turtle()

for enemy in range( 5 ):
    make_enemies()

player.color( "yellow" )
player.shape( "triangle" )
player.speed( 0 )
player.penup()
player.goto( 0 , -375 )
player.setheading( 90 )

bullet.color( "yellow" )
bullet.shape( "triangle" )
bullet.speed( 0 )
bullet.penup()
bullet.setheading( 90 )
bullet.shapesize( 0.5 , 0.5 )
bullet.hideturtle()

bullet_state = "ready"

wn.listen()
wn.onkey( move_left , 'Left' )
wn.onkey( move_right , 'Right' )
wn.onkey( fire_bullet , "space" )

while True:
    wn.update()

    for enemy in e:
        x = enemy.xcor()
        x += enemy.enemy_speed
        enemy.setx( x )

        if enemy.xcor() > 570:
            y = enemy.ycor()
            y -= 40
            enemy.enemy_speed *= -1
            enemy.sety( y )

        if enemy.xcor() < -570:
            y = enemy.ycor()
            y -= 40
            enemy.enemy_speed *= -1
            enemy.sety( y )

    for enemy in e:
        if enemy.ycor() < -400:
            x = random.randint( -570 , 570 )
            y = random.randint( 190 , 350 )
            enemy.setposition( x , y )
            enemy.setheading( 0 )

    for enemy in e:
        if is_collision( player , enemy ):
            end = turtle.Turtle()
            end.penup()
            end.pen( fillcolor="black" , pencolor="red" , pensize=30 )
            end.setposition( -40 , -50 )
            end.hideturtle()
            end.write( "GAME OVER" , 'center' , font=30 )
            time.sleep( 2 )
            sys.exit()

        if is_collision( bullet , enemy ):
            bullet.hideturtle()
            bullet_state = "ready"
            bullet.setposition( 0 , -350 )
            x = random.randint( -570 , 570 )
            y = random.randint( 100 , 250 )
            enemy.setposition( x , y )

    if bullet_state == "fire":
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety( y )

    if bullet.ycor() > 370:
        bullet.hideturtle()
        bullet_state = "ready"