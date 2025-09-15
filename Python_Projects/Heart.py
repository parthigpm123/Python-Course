import turtle

# Setup
t = turtle.Turtle()
s = turtle.Screen()
s.setup(width=1000, height=800)   # Larger window size
s.bgcolor('black')
t.hideturtle()
t.speed(3)

# Draw extra big heart shape
t.penup()
t.goto(0, -200)   # Start lower for bigger heart
t.pendown()
t.pensize(6)      # Even thicker outline
t.color('red')
t.begin_fill()
t.left(140)
t.forward(300)
t.circle(-150, 200)
t.setheading(60)
t.circle(-150, 200)
t.forward(298)
t.end_fill()

# Write text inside the heart
t.penup()
t.goto(-80, 80)
t.pendown()
t.color('white')
t.write("❤️", font=("verdana", 50, "bold"))

# Write text below the heart
t.penup()
t.goto(-250, -250)
t.pendown()
t.write("I Love Programming", font=("verdana", 32, "bold"))

# Finish
t.hideturtle()
turtle.done()
