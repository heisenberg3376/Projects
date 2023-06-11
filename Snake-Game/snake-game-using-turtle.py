import turtle
import time
import random

delay = 0.1

score = 0
high_score = 0

window = turtle.Screen()
window.title('Simple Snake Game')
window.bgcolor('green')
window.setup(width=600, height=600)
window.tracer(0)

# creating the snake head
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('blue')
head.penup()
head.goto(0,0)
head.direction = 'stop'

# food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(0,150)

# scoreboard
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.shape("square")
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 260)
scoreboard.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))


# functions to move the snakes direction
def move_up():
    if head.direction != 'down':
        head.direction = 'up'
def move_down():
    if head.direction != 'up':
        head.direction = 'down'
def move_right():
    if head.direction != 'left':
        head.direction = 'right'
def move_left():
    if head.direction != 'right':
        head.direction = 'left'

def move():
    if head.direction=='up':
        y = head.ycor()
        head.sety(y + 20)
        
    if head.direction=='down':
        y = head.ycor()
        head.sety(y - 20)
        
    if head.direction=='left':
        x = head.xcor()
        head.setx(x - 20)
        
    if head.direction=='right':
        x = head.xcor()
        head.setx(x + 20)

# key binding
window.listen()
window.onkeypress(move_up,'w')
window.onkeypress(move_down,'s')
window.onkeypress(move_right,'d')
window.onkeypress(move_left,'a')

# if the snake touches the food, its body must grow

body_segments = []

while True:
    window.update()

    # cheking for a collision with a boundary
    if head.xcor()<-290 or head.xcor()>290 or head.ycor()<-290 or head.ycor()>290:
        time.sleep(2)
        head.goto(0,0)
        head.direction = 'stop'

        for segment in body_segments:
            segment.goto(1000,1000)
            
        body_segments.clear()

        # reset delay
        score = 0
        # reset delay
        delay = 0.1

        scoreboard.clear()
        scoreboard.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
    
    
    if head.distance(food) < 20:
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.color('light blue')
        new_segment.shape('square')
        new_segment.penup()
        body_segments.append(new_segment)
        # add score
        score += 10
        # shorten delay
        delay -= 0.001
        if score > high_score:
            high_score = score
            
        scoreboard.clear()
        scoreboard.write('Score: {}  High-Score: {}'.format(score,high_score),align="center", font=('Courier', 24, 'normal'))
        

    for i in range(len(body_segments)-1,0,-1):
        x = body_segments[i-1].xcor()
        y = body_segments[i-1].ycor()
        body_segments[i].goto(x, y)

    if len(body_segments) > 0:
        x = head.xcor()
        y = head.ycor()
        body_segments[0].goto(x,y)

    
        
    move()

    # check for head colliding with body
    for segment in body_segments:
        if segment.distance(head) < 20:
            time.sleep(2)
            head.goto(0,0)
            head.direction='stop'
            
            for segment in body_segments:
                segment.goto(1000,1000)
            
            body_segments.clear()

            score = 0
            dealy = 0.1

            scoreboard.clear()
            scoreboard.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
            
    
    
    time.sleep(delay)

window.mainloop()

