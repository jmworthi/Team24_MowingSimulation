# import required modules
import turtle
import time
import random

delay = 0.1
fill = False
# Creating a window screen
wn = turtle.Screen()
wn.bgcolor("blue")
# the width and height can be put as user's choice
wn.setup(width=600, height=600)
wn.tracer(0)

# head of the snake
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(-280, -280)
head.direction = "Stop"

x_length = 0
y_length = 0
grid = []

# assigning key directions
def group():
    if head.direction != "down":
        head.direction = "up"
        #
        # Adding segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        if fill == True:
            new_segment.color("red")
        else:
            new_segment.color("orange")  # tail colour
        new_segment.penup()
        y = head.ycor()
        x = head.xcor()
        segments.append(new_segment)
        new_segment.setx(x)
        new_segment.sety(y)
        move()



def godown():
    if head.direction != "up":
        head.direction = "down"


        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")  # tail colour
        new_segment.penup()
        y = head.ycor()
        x = head.xcor()
        segments.append(new_segment)
        new_segment.setx(x)
        new_segment.sety(y)
        move()

def goleft():
    if head.direction != "right":
        head.direction = "left"


        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")  # tail colour
        new_segment.penup()
        y = head.ycor()
        x = head.xcor()
        segments.append(new_segment)
        new_segment.setx(x)
        new_segment.sety(y)
        move()

def goright():
    if head.direction != "left":
        head.direction = "right"

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")  # tail colour
        new_segment.penup()
        y = head.ycor()
        x = head.xcor()
        segments.append(new_segment)
        new_segment.setx(x)
        new_segment.sety(y)
        move()

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    wn.update()



def print_grid():
    for x in grid:
        print("\n", end="")
        for y in x:
            print(y, end="")
    print("\n")

def fill():

    # find dimensions
    x_coordinates = []
    y_coordinates = []
    for segment in segments:
        x_coordinates.append(segment.xcor())
        y_coordinates.append(segment.ycor())
    x_length = max(x_coordinates) - min(x_coordinates)
    y_length = max(y_coordinates) - min(y_coordinates)

    #create grid with dimensions
    print(x_length/20 + 1)
    print(y_length/20 + 1)
    L1 = []
    for x in range(int(x_length/20 + 1)):
        L1.append('O')
    for y in range(int(y_length/20 + 1)):
        L2 = L1.copy()
        grid.append(L2)

    # "x" out the perimeter
    for segment in segments:
        grid[(int(segment.ycor()/20) - int(min(y_coordinates)/20))][(int(segment.xcor()/20) - int(min(x_coordinates)/20))] = "X"
    grid.reverse()

    # Remove everything outside of grid at the perimeter
    for x in range(int(x_length/20 + 1)):
        if grid[0][x] == "O":
            grid[0][x] = "-"
        if grid[int(y_length/20)][x] == "O":
            grid[int(y_length/20)][x] = "-"
    for y in range(int(y_length/20 + 1)):
        if grid[y][0] == "O":
            grid[y][0] = "-"
        if grid[y][int(x_length/20)] == "O":
            grid[y][int(x_length / 20)] = "-"

    # remove other things outside of perimeter
    done = False
    while done == False:
        done = True
        for x in range(int(x_length/20 + 1)): # below
            for y in range(int(y_length/20)):
                if (grid[y][x] == "-") & (grid[y+1][x] == "O"):
                    grid[y + 1][x] = "-"
                    done = False
        for x in range(int(x_length/20 + 1)): # above
            for y in range(int(y_length/20)):
                if (grid[y + 1][x] == "-") & (grid[y][x] == "O"):
                    grid[y][x] = "-"
                    done = False
        for x in range(int(x_length/20)): # right
            for y in range(int(y_length/20 + 1)):
                if (grid[y][x] == "-") & (grid[y][x+1] == "O"):
                    grid[y][x+1] = "-"
                    done = False
        for x in range(int(x_length/20)): # left
            for y in range(int(y_length/20 + 1)):
                if (grid[y][x+1] == "-") & (grid[y][x] == "O"):
                    grid[y][x] = "-"
                    done = False

    #filling
    head.color("red")
    stop = False
    d = "up" #direction
    print_grid()
    while stop == False:
        print(head.xcor(), head.ycor())
        y_sq = -int((head.ycor()-min(y_coordinates))/20-y_length/20) #y grid coordinate
        x_sq = int((head.xcor()-min(x_coordinates))/20) #x grid coordinate
        w = [grid[y_sq-1][x_sq-1], grid[y_sq-1][x_sq], grid[y_sq-1][x_sq+1],
             grid[y_sq][x_sq-1], grid[y_sq][x_sq], grid[y_sq][x_sq+1],
             grid[y_sq+1][x_sq-1], grid[y_sq+1][x_sq], grid[y_sq+1][x_sq+1]] #window
        '''
        w = [0h,1a,2b,3g,4x,5c,6f,7e,8d]
        a'*c'*e'*g'*(f*h+b'*d*f+b'*d*h+b*d+b*d'*f+b*d'*h)
        + a'*c'*e'*g*(b+d)
        + a'*c'*e*g*b
        + a'*c'*e*g'*(h+b)
        + a'*c*e*g'*h
        + a'*c*e'*g
        + a'*c*e'*g'*(f+h)
        + a*c*e'*g'*f
        + a*c'*e*g'
        + a*c'*e'*g*d
        + a*c'*e'*g'*(d+f)
        '''
        critical = (w[1] == "O" and w[5] == "O" and w[7] == "O" and w[3] == "O" and (w[6] != "O" and
            w[0] != "O" or w[2] == "O" and w[8] != "O" and w[6] != "O" or w[2] == "O" and w[8] != "O" and
            w[0] != "O" or w[2] != "O" and w[8] != "O" or w[2] != "O" and w[8] == "O" and w[6] != "O" or w[2] != "O" and
            w[8] == "O" and w[0] != "O") or
            w[1] == "O" and w[5] == "O" and w[7] == "O" and w[3] != "O" and (w[2] != "O" or w[8] != "O") or
            w[1] == "O" and w[5] == "O" and w[7] != "O" and w[3] != "O" and w[2] != "O" or
            w[1] == "O" and w[5] == "O" and w[7] != "O" and w[3] == "O" and (w[0] != "O" or w[2] != "O") or
            w[1] == "O" and w[5] != "O" and w[7] != "O" and w[3] == "O" and w[0] != "O" or
            w[1] == "O" and w[5] != "O" and w[7] == "O" and w[3] != "O" or
            w[1] == "O" and w[5] != "O" and w[7] == "O" and w[3] == "O" and (w[6] != "O" or w[0] != "O") or
            w[1] != "O" and w[5] != "O" and w[7] == "O" and w[3] == "O" and w[6] != "O" or
            w[1] != "O" and w[5] == "O" and w[7] != "O" and w[3] == "O" or
            w[1] != "O" and w[5] == "O" and w[7] == "O" and w[3] != "O" and w[8] != "O" or
            w[1] != "O" and w[5] == "O" and w[7] == "O" and w[3] == "O" and (w[8] != "O" or w[6] != "O"))

        if d == "up":
            if w[5] == "O":  # square to right
                d = "right"
                goright_fill(x_coordinates, y_coordinates, critical)
            elif w[1] == "O": #square above
                d = "up"
                goup_fill(x_coordinates, y_coordinates, critical)
            elif w[3] == "O": #square to left
                d = "left"
                goleft_fill(x_coordinates, y_coordinates, critical)
            elif w[7] == "O": #square below
                d = "down"
                godown_fill(x_coordinates, y_coordinates, critical)
            else:
                stop = True
        elif d == "right":
            if w[7] == "O": #square below
                d = "down"
                godown_fill(x_coordinates, y_coordinates, critical)
            elif w[5] == "O":  # square to right
                d = "right"
                goright_fill(x_coordinates, y_coordinates, critical)
            elif w[1] == "O": #square above
                d = "up"
                goup_fill(x_coordinates, y_coordinates, critical)
            elif w[3] == "O": #square to left
                d = "left"
                goleft_fill(x_coordinates, y_coordinates, critical)
            else:
                stop = True
        elif d == "down":
            if w[3] == "O": #square to left
                d = "left"
                goleft_fill(x_coordinates, y_coordinates, critical)
            elif w[7] == "O": #square below
                d = "down"
                godown_fill(x_coordinates, y_coordinates, critical)
            elif w[5] == "O":  # square to right
                d = "right"
                goright_fill(x_coordinates, y_coordinates, critical)
            elif w[1] == "O": #square above
                d = "up"
                goup_fill(x_coordinates, y_coordinates, critical)
            else:
                stop = True
        elif d == "left":
            if w[1] == "O": #square above
                d = "up"
                goup_fill(x_coordinates, y_coordinates, critical)
            elif w[3] == "O": #square to left
                d = "left"
                goleft_fill(x_coordinates, y_coordinates, critical)
            elif w[7] == "O": #square below
                d = "down"
                godown_fill(x_coordinates, y_coordinates, critical)
            elif w[5] == "O":  # square to right
                d = "right"
                goright_fill(x_coordinates, y_coordinates, critical)
            else:
                stop = True

    print_grid()


def goup_fill(x_coordinates, y_coordinates, critical):
    if head.direction != "down":
        head.direction = "up"

        # Adding segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")  # tail colour
        new_segment.penup()
        if grid[-1*(int((head.ycor()-min(y_coordinates))/20) + 1)][int((head.xcor()-min(x_coordinates))/20)] == "O":
            if critical:
                grid[-1 * (int((head.ycor() - min(y_coordinates)) / 20) + 1)][int((head.xcor() - min(x_coordinates)) / 20)] = "2"
            else:
                grid[-1*(int((head.ycor()-min(y_coordinates))/20) + 1)][int((head.xcor()-min(x_coordinates))/20)] = "1"
        y = head.ycor()
        x = head.xcor()
        segments.append(new_segment)
        new_segment.setx(x)
        new_segment.sety(y)
        move()



def godown_fill(x_coordinates, y_coordinates, critical):
    if head.direction != "up":
        head.direction = "down"


        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")  # tail colour
        new_segment.penup()
        if grid[-1*(int((head.ycor()-min(y_coordinates))/20) + 1)][int((head.xcor()-min(x_coordinates))/20)] == "O":
            if critical:
                grid[-1 * (int((head.ycor() - min(y_coordinates)) / 20) + 1)][int((head.xcor() - min(x_coordinates)) / 20)] = "2"
            else:
                grid[-1*(int((head.ycor()-min(y_coordinates))/20) + 1)][int((head.xcor()-min(x_coordinates))/20)] = "1"
        y = head.ycor()
        x = head.xcor()
        segments.append(new_segment)
        new_segment.setx(x)
        new_segment.sety(y)
        move()

def goleft_fill(x_coordinates, y_coordinates, critical):
    if head.direction != "right":
        head.direction = "left"


        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")  # tail colour
        new_segment.penup()
        if grid[-1*(int((head.ycor()-min(y_coordinates))/20) + 1)][int((head.xcor()-min(x_coordinates))/20)] == "O":
            if critical:
                grid[-1*(int((head.ycor()-min(y_coordinates))/20) + 1)][int((head.xcor()-min(x_coordinates))/20)] = "2"
            else:
                grid[-1*(int((head.ycor()-min(y_coordinates))/20) + 1)][int((head.xcor()-min(x_coordinates))/20)] = "1"
        y = head.ycor()
        x = head.xcor()
        segments.append(new_segment)
        new_segment.setx(x)
        new_segment.sety(y)
        move()

def goright_fill(x_coordinates, y_coordinates, critical):
    if head.direction != "left":
        head.direction = "right"
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")  # tail colour
        new_segment.penup()
        if grid[-1*(int((head.ycor()-min(y_coordinates))/20) + 1)][int((head.xcor()-min(x_coordinates))/20)] == "O":
            if critical:
                grid[-1*(int((head.ycor()-min(y_coordinates))/20) + 1)][int((head.xcor()-min(x_coordinates))/20)] = "2"
            else:
                grid[-1*(int((head.ycor()-min(y_coordinates))/20) + 1)][int((head.xcor()-min(x_coordinates))/20)] = "1"
        y = head.ycor()
        x = head.xcor()
        segments.append(new_segment)
        new_segment.setx(x)
        new_segment.sety(y)

        move()

wn.listen()
wn.onkeypress(group, "w")
wn.onkeypress(godown, "s")
wn.onkeypress(goleft, "a")
wn.onkeypress(goright, "d")
wn.onkeypress(fill, "m")

segments = []

# Main Gameplay
# while True:
#     wn.update()
#     if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
#         time.sleep(1)
#         head.goto(0, 0)
#         head.direction = "Stop"
#         colors = random.choice(['red', 'blue', 'green'])
#         shapes = random.choice(['square', 'circle'])
#         for segment in segments:
#             segment.goto(1000, 1000)
#         segments.clear()
#         score = 0
#         delay = 0.1
#
#
#     # Checking for head collisions with body segments
#     for index in range(len(segments) - 1, 0, -1):
#         x = segments[index - 1].xcor()
#         y = segments[index - 1].ycor()
#         segments[index].goto(x, y)
#     if len(segments) > 0:
#         x = head.xcor()
#         y = head.ycor()
#         segments[0].goto(x, y)
#     move()
#     for segment in segments:
#         if segment.distance(head) < 20:
#             time.sleep(1)
#             head.goto(0, 0)
#             head.direction = "stop"
#             colors = random.choice(['red', 'blue', 'green'])
#             shapes = random.choice(['square', 'circle'])
#             for segment in segments:
#                 segment.goto(1000, 1000)
#             segment.clear()
#
#             score = 0
#             delay = 0.1
#     time.sleep(delay)

wn.mainloop()