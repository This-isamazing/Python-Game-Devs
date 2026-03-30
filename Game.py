import turtle
import random
import time

screen = turtle.Screen()
screen.title("Follow Turtle + Obstacle + UI")
screen.tracer(0)

# world boundaries (screen block size)
llx, lly = -400, -200
urx, ury = 400, 200
screen.setworldcoordinates(llx, lly, urx, ury)

t = turtle.Turtle()
t.shape("triangle")
t.color("black")
t.penup()
t.speed(0)

movementspeed = 5
moving_forward = moving_backward = turning_left = turning_right = False
show_coords = False

player_speed = 2.0
min_speed = 2.0
max_speed = 10.0
acceleration = 1.3

ghost_mode = False
ghost_end_time = 0.0

level = 1
score = 0
obstacles = []

def create_obstacles(num):
    for _ in range(num):
        obs = turtle.Turtle()
        obs.shape("square")
        obs.color("red")
        obs.penup()
        x = random.randint(int(llx) - 800, int(urx) + 800)
        y = random.randint(int(lly) - 600, int(ury) + 600)
        obs.goto(x, y)
        obstacles.append(obs)

create_obstacles(6)

ui_turtle = turtle.Turtle()
ui_turtle.hideturtle()
ui_turtle.penup()
ui_turtle.speed(0)

speed_gauge = turtle.Turtle()
speed_gauge.hideturtle()
speed_gauge.penup()
speed_gauge.speed(0)

heading_gauge = turtle.Turtle()
heading_gauge.hideturtle()
heading_gauge.penup()
heading_gauge.speed(0)

coord_turtle = turtle.Turtle()
coord_turtle.hideturtle()
coord_turtle.penup()
coord_turtle.speed(0)

def draw_level_ui():
    ui_turtle.clear()
    ui_turtle.goto(-screen.window_width()//2 + 10, screen.window_height()//2 - 20)
    ui_turtle.write(f"Level: {level}  Score: {int(score)}", font=("Arial", 14, "normal"))

def draw_speed_gauge():
    gauge_width = 200
    gauge_height = 14
    x0 = -screen.window_width()//2 + 10
    y0 = screen.window_height()//2 - 50
    pct = (player_speed - min_speed) / (max_speed - min_speed)
    pct = max(0.0, min(1.0, pct))

    speed_gauge.clear()
    speed_gauge.goto(x0, y0)
    speed_gauge.color("black")
    speed_gauge.pendown()
    for _ in range(2):
        speed_gauge.forward(gauge_width)
        speed_gauge.right(90)
        speed_gauge.forward(gauge_height)
        speed_gauge.right(90)
    speed_gauge.penup()

    speed_gauge.goto(x0, y0)
    speed_gauge.color("green")
    speed_gauge.pendown()
    speed_gauge.begin_fill()
    for _ in range(2):
        speed_gauge.forward(gauge_width * pct)
        speed_gauge.right(90)
        speed_gauge.forward(gauge_height)
        speed_gauge.right(90)
    speed_gauge.end_fill()
    speed_gauge.penup()

    speed_gauge.goto(x0, y0 - 18)
    speed_gauge.color("black")
    speed_gauge.write(f"Speed: {player_speed:.1f}", font=("Arial", 10, "normal"))

def draw_heading_gauge():
    bar_width = 200
    bar_height = 14
    x0 = -screen.window_width()//2 + 10
    y0 = screen.window_height()//2 - 90
    heading = t.heading() % 360
    pct = heading / 360.0

    heading_gauge.clear()
    heading_gauge.goto(x0, y0)
    heading_gauge.color("black")
    heading_gauge.pendown()
    for _ in range(2):
        heading_gauge.forward(bar_width)
        heading_gauge.right(90)
        heading_gauge.forward(bar_height)
        heading_gauge.right(90)
    heading_gauge.penup()

    heading_gauge.goto(x0, y0)
    heading_gauge.color("blue")
    heading_gauge.pendown()
    heading_gauge.begin_fill()
    for _ in range(2):
        heading_gauge.forward(bar_width * pct)
        heading_gauge.right(90)
        heading_gauge.forward(bar_height)
        heading_gauge.right(90)
    heading_gauge.end_fill()
    heading_gauge.penup()

    heading_gauge.goto(x0, y0 - 18)
    heading_gauge.color("black")
    heading_gauge.write(f"Heading: {heading:.0f}°", font=("Arial", 10, "normal"))

def draw_coords():
    coord_turtle.clear()
    if show_coords:
        x, y = t.position()
        coord_turtle.goto(-screen.window_width()//2 + 10, screen.window_height()//2 - 120)
        coord_turtle.write(f"X: {x:.1f} Y: {y:.1f}", font=("Arial", 10, "normal"))

def enter_ghost_mode():
    global ghost_mode, ghost_end_time
    ghost_mode = True
    ghost_end_time = time.time() + 5.0
    t.color("gray")

def exit_ghost_mode():
    global ghost_mode
    ghost_mode = False
    t.color("black")

def check_collision():
    if ghost_mode:
        return False
    for obs in obstacles:
        if t.distance(obs) < 20:
            enter_ghost_mode()
            return True
    return False

def update_view():
    global llx, lly, urx, ury
    width = urx - llx
    height = ury - lly
    moved = False

    if t.xcor() > urx:
        llx += width; urx += width; moved = True
    elif t.xcor() < llx:
        llx -= width; urx -= width; moved = True

    if t.ycor() > ury:
        lly += height; ury += height; moved = True
    elif t.ycor() < lly:
        lly -= height; ury -= height; moved = True

    if moved:
        screen.setworldcoordinates(llx, lly, urx, ury)

def move():
    global player_speed, score, level

    if moving_forward:
        player_speed = min(max_speed, player_speed * acceleration)
        t.forward(player_speed)
    else:
        player_speed = min_speed

    if moving_backward:
        t.backward(2)
    if turning_left:
        t.left(movementspeed)
    if turning_right:
        t.right(movementspeed)

    update_view()

    if check_collision():
        score = max(0, score - 30)

    if ghost_mode and time.time() >= ghost_end_time:
        exit_ghost_mode()

    score += 0.2
    if score >= level * 150:
        level += 1
        create_obstacles(2)

    draw_level_ui()
    draw_speed_gauge()
    draw_heading_gauge()
    draw_coords()

    screen.update()
    screen.ontimer(move, 20)

def start_forward(): global moving_forward; moving_forward = True
def stop_forward(): global moving_forward; moving_forward = False
def start_backward(): global moving_backward; moving_backward = True
def stop_backward(): global moving_backward; moving_backward = False
def start_left(): global turning_left; turning_left = True
def stop_left(): global turning_left; turning_left = False
def start_right(): global turning_right; turning_right = True
def stop_right(): global turning_right; turning_right = False
def show_coords_on(): global show_coords; show_coords = True
def show_coords_off(): global show_coords; show_coords = False

screen.onkeypress(start_forward, "Up")
screen.onkeyrelease(stop_forward, "Up")
screen.onkeypress(start_backward, "Down")
screen.onkeyrelease(stop_backward, "Down")
screen.onkeypress(start_left, "Left")
screen.onkeyrelease(stop_left, "Left")
screen.onkeypress(start_right, "Right")
screen.onkeyrelease(stop_right, "Right")
screen.onkeypress(show_coords_on, "space")
screen.onkeyrelease(show_coords_off, "space")

screen.listen()
move()
screen.mainloop()