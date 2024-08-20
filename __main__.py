import turtle
import time

one=turtle.Turtle()
screen=turtle.Screen()
screen.title("Catch the Dolphin")
screen.bgcolor("lightblue")
screen.addshape("dolphin.gif")
one.shape("dolphin.gif")
import random
one.penup()

def move_randomly():
    x = random.randint(-screen.window_width()//2, screen.window_width()//2)
    y = random.randint(-screen.window_height()//2, screen.window_height()//2)
    one.goto(x, y)
    screen.ontimer(move_randomly, 1000)
move_randomly()
import time
dolphin=turtle.Turtle()
dolphin.hideturtle()
dolphin.penup()
dolphin.goto(0,260)
dolphin.color("white")
score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.penup()
score_turtle.goto(0, screen.window_height()//2 - 40)
score_turtle.write("Clicks: 0", align="center", font=("Arial", 16, "normal"))
click_count = 0

# Function to update the click counter
def update_click_count(x, y):
    global click_count
    click_count += 1
    score_turtle.clear()
    score_turtle.write(f"Clicks: {click_count}", align="center", font=("Arial", 16, "normal"))

# Bind the click event to the image turtle
one.onclick(update_click_count)

def countdown(seconds):
    while seconds>0:
        dolphin.clear()
        dolphin.write(str(seconds), align="center", font=("Arial", 24, "normal"))
        time.sleep(1)
        seconds -= 1
    dolphin.clear()
    dolphin.write("It is over", align="center", font=("Arial", 24, "normal"))


countdown(10)

turtle.mainloop()