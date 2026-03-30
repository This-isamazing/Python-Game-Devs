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
penup = False
acceleration = 1.3001  # Acceleration factor for forward movement. Yes I'm very presise with this number.
fullscreen = True
if fullscreen:
    screen.setup(width=1.0, height=1.0)  # Set to fullscreen
shape = "classic"  # Default shape
t.shape(shape)
# World coordinate boundaries (initial view size, e.g., 400x400)
llx, lly = -400, -200
urx, ury = 400, 200
screen.setworldcoordinates(llx, lly, urx, ury)
t.write("Use arrow keys to move the turtle. The view will shift as you move." + "\n" + " (Fullscreen is recommended). Use p to toggle pen up/down. Use Q to clear the screen.(BE CAREFUL!)" + "\n" + 
        "Use 1-6 to change shape. Use X, Z, V, G to change color." + "\n" + "Use F, S, M, H to change speed. Use A, L, K, J for alternative speed options." + "\n" + 
        "Use C, R, B, N to change pen color. Use I, U, Y, T to change pen size. T is very thick!" + "\n" + 
        " It's better to use other shapes to see the effect.", align="center", font=("Futura", 16, "normal"))

  # Clear the instruction text when movement starts


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

#pen up/down toggle
screen.onkeypress(lambda: t.penup(), "p")  # Press 'p' to toggle pen up/down
screen.onkeypress(lambda: t.pendown(), "o")  # Press 'o' to put pen down

#Oww Shape shifting Keys. Imagine this in multiplayer! 

#color changing keys are down there too. I just wanted to group them together. You can also change the keys if you want, just make sure to change the instructions at the beginning of the code as well.
screen.onkeypress(lambda: t.shape("turtle"), "1")  # Press '1' to change shape to turtle
screen.onkeypress(lambda: t.shape("circle"), "2")  # Press '2' to change shape to circle
screen.onkeypress(lambda: t.shape("square"), "3")  # Press '3' to change shape to square
screen.onkeypress(lambda: t.shape("triangle"), "4")  # Press '4' to change shape to triangle
screen.onkeypress(lambda: t.shape("arrow"), "5")  # Press '5' to change shape to arrow
screen.onkeypress(lambda: t.shape("classic"), "6")  # Press '6' to change shape to classic

# Clear screen key
screen.onkeypress(lambda: t.clear(), "q")  # Press 'q' to clear the screen

#Color changing keys
screen.onkeypress(lambda: t.color("black"), "x")  # Press 'x' to change color to black
screen.onkeypress(lambda: t.color("red"), "z")  # Press 'z' to change color to red
screen.onkeypress(lambda: t.color("blue"), "v")  # Press 'v' to change color to blue
screen.onkeypress(lambda: t.color("green"), "g")  # Press 'g' to change color to green

#Speed changing keys
screen.onkeypress(lambda: t.speed(0), "f")  # Press 'f' to set speed to fastest
screen.onkeypress(lambda: t.speed(1), "s")  # Press 's' to set speed to slowest
screen.onkeypress(lambda: t.speed(5), "m")  # Press 'm' to set speed to medium
screen.onkeypress(lambda: t.speed(10), "h")  # Press 'h' to set speed to fast

#Alternative speed keys for more options
screen.onkeypress(lambda: t.speed(0), "a")  # Press 'a' to set speed to fastest (alternative key)
screen.onkeypress(lambda: t.speed(1), "l")  # Press 'l' to set speed to slowest (alternative key)
screen.onkeypress(lambda: t.speed(5), "k")  # Press 'k' to set speed to medium (alternative key)
screen.onkeypress(lambda: t.speed(10), "j")  # Press 'j' to set speed to fast (alternative key)

#Ok this is alot of controls, but I wanted to give you a lot of options to customize your turtle.
screen.onkeypress(lambda: t.pencolor("black"), "c")  # Press 'c' to change pen color to black
screen.onkeypress(lambda: t.pencolor("red"), "r")  # Press 'r' to change pen color to red
screen.onkeypress(lambda: t.pencolor("blue"), "b")  # Press 'b' to change pen color to blue
screen.onkeypress(lambda: t.pencolor("green"), "n")  # Press 'n' to change pen color to green

#Wow pensize keys this is great for drawing! Better start typing that letter to MS Paint, am I right?
screen.onkeypress(lambda: t.pensize(1), "i")  # Press 'i' to set pen size to thin
screen.onkeypress(lambda: t.pensize(3), "u")  # Press 'u' to set pen size to medium
screen.onkeypress(lambda: t.pensize(5), "y")  # Press 'y' to set pen size to thick
screen.onkeypress(lambda: t.pensize(10), "t")  # Press 't' to set pen size to extra thick. KSI style.

#ok that's alot of controls. You can always ask for more.
screen.listen()


if shape == "turtle":
    t.color("green")

if shape == "circle":
    t.color("purple")

if shape == "square":
    t.color("red")

if shape == "triangle":
    t.color("orange")

if shape == "arrow":
    t.color("blue")  #I picked blue because it represents speed and arrows are fast.

if shape == "classic":
    t.color("black") #It was the original color and I think it fits the classic shape the best. Ya know, classic black.

if shape == "turtle" or shape == "circle" or shape == "square" or shape == "triangle" or shape == "arrow":
    t.shapesize(0.5, 0.5, 0.5)  # This probably doesn't work. I wanted to make the shapes smaller because they look better with the movement system, but it doesn't seem to be working. You can try to fix it if you want, but it's not a big deal.

# Main movement loop
def move():
    global llx, lly, urx, ury
    if moving_forward:
        t.forward(movementspeed*acceleration)
    if moving_backward:
        t.backward(movementspeed*0.9)
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

def pen_toggle():
    if t.isdown():
        t.penup()
    else:
        t.pendown()

pen_toggle()  # Start with pen up
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
#Up top is where you can add the code for the second turtle if you want to have a second player. 
# You can also add the follow_turtle function up there if you want to have a third turtle that 
# follows the first one. You might need to tweek it a bit to make it work with the movement system, but it should be possible. 
# Just make sure to change the instructions at the beginning of the code if you add more controls.
turtle.done()