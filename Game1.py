import turtle

screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)  # Fastest drawing speed for fluidity
movementspeed = 5  # Speed of movement in pixels per update

# Movement flags
moving_forward = False
moving_backward = False
turning_left = False
turning_right = False

acceleration = 1.3

# World coordinate boundaries (initial view size, e.g., 400x400)
llx, lly = -400, -200
urx, ury = 400, 200
screen.setworldcoordinates(llx, lly, urx, ury)
t.write("Use arrow keys to move the turtle. The view will shift as you move.(Fullscreen is recommended)", align="center", font=("Futura", 16, "normal"))

if moving_forward == True or moving_backward == True or turning_left == True or turning_right == True:
    t.clear()


def start_forward():
    global moving_forward
    moving_forward = True

def stop_forward():
    global moving_forward
    moving_forward = False

def start_backward():
    global moving_backward
    moving_backward = True

def stop_backward():
    global moving_backward
    moving_backward = False

def start_left():
    global turning_left
    turning_left = True

def stop_left():
    global turning_left
    turning_left = False

def start_right():
    global turning_right
    turning_right = True

def stop_right():
    global turning_right
    turning_right = False

# Bind keys to start/stop functions
screen.onkeypress(start_forward, "Up")
screen.onkeyrelease(stop_forward, "Up")
screen.onkeypress(start_backward, "Down")
screen.onkeyrelease(stop_backward, "Down")
screen.onkeypress(start_left, "Left")
screen.onkeyrelease(stop_left, "Left")
screen.onkeypress(start_right, "Right")
screen.onkeyrelease(stop_right, "Right")

screen.listen()

# Main movement loop
def move():
    global llx, lly, urx, ury
    if moving_forward:
        t.forward(movementspeed*acceleration)
    if moving_backward:
        t.backward(movementspeed)
    if turning_left:
        t.left(movementspeed)
    if turning_right:
        t.right(movementspeed)
    
    # Check and shift view in Y direction
    height = ury - lly
    if t.ycor() > ury:
        lly += height
        ury += height
        screen.setworldcoordinates(llx, lly, urx, ury)
    elif t.ycor() < lly:
        lly -= height
        ury -= height
        screen.setworldcoordinates(llx, lly, urx, ury)
    
    # Check and shift view in X direction
    width = urx - llx
    if t.xcor() > urx:
        llx += width
        urx += width
        screen.setworldcoordinates(llx, lly, urx, ury)
    elif t.xcor() < llx:
        llx -= width
        urx -= width
        screen.setworldcoordinates(llx, lly, urx, ury)
    
    screen.ontimer(move, 10)  # Call every 10ms for smooth updates

# Start the loop
move()
'''
turtle.clone()  # Clone the turtle to allow for multiple turtles if needed
movement2 = turtle.Turtle()  # Create a second turtle for the second player
def turtle2_control():
    if moving_forward:
        movement2.forward(movementspeed*acceleration)
    if moving_backward:
        movement2.backward(movementspeed)
    if turning_left:
        movement2.left(movementspeed)
    if turning_right:
        movement2.right(movementspeed)
    
    screen.ontimer(turtle2_control, 10)  # Call every 10ms for smooth updates

def turtle2_start_forward():
    global moving_forward
    moving_forward = True

def turtle2_stop_forward():
    global moving_forward
    moving_forward = False

def turtle2_start_backward():
    global moving_backward
    moving_backward = True
def turtle2_stop_backward():
    global moving_backward
    moving_backward = False
def turtle2_start_left():
    global turning_left
    turning_left = True
def turtle2_stop_left():
    global turning_left
    turning_left = False
def turtle2_start_right():
    global turning_right
    turning_right = True
def turtle2_stop_right():
    global turning_right
    turning_right = False
# Bind keys for the second turtle
screen.onkeypress(turtle2_start_forward, "w")
screen.onkeyrelease(turtle2_stop_forward, "w")
screen.onkeypress(turtle2_start_backward, "s")
screen.onkeyrelease(turtle2_stop_backward, "s")
screen.onkeypress(turtle2_start_left, "a")
screen.onkeyrelease(turtle2_stop_left, "a")
screen.onkeypress(turtle2_start_right, "d")
screen.onkeyrelease(turtle2_stop_right, "d")
turtle2_control()  # Start the second turtle's control loop
'''
#Up top is where you can add the code for the second turtle if you want to have a second player. You can also add the follow_turtle function up there if you want to have a third turtle that follows the first one.
# Include your follow_turtle function here if needed
turtle.done()