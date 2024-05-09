from turtle import *

# -----------------------------------------------------------------
# Draw a hollow hexagon, each side a different color
# -----------------------------------------------------------------
# pencil = Turtle()

# colors = ["red", "purple", "orange", "lime green", "light blue", "yellow"]

# for i in range(6):
#     pencil.color(colors[i])
#     pencil.width(5)
#     pencil.fd(100)
#     pencil.rt(60)

# done()

# -----------------------------------------------------------------
# Draw 4 solid aquares all different colors in different locations
# -----------------------------------------------------------------
# from random import randint

# pencil = Turtle()

# # number of shapes
# for _ in range(4):
#     r = randint(0, 255)
#     g = randint(0, 255)
#     b = randint(0, 255)

#     color = (r / 255, g / 255, b / 255)

#     x = randint(-200, 200)
#     y = randint(-200, 200)

#     pencil.up()
#     pencil.goto(x, y)
#     pencil.down()

#     pencil.color(color)
#     pencil.begin_fill()

#     # draw squares
#     for i in range(4):
#         pencil.fd(100)
#         pencil.rt(90)

#     pencil.end_fill()

# done()

# -----------------------------------------------------------------
# Create 3 functions that'll draw something different when called
# -----------------------------------------------------------------
# pencil = Turtle()


# def square(p, size, color):
#     p.color(color)
#     p.begin_fill()
#     for _ in range(4):
#         p.fd(size)
#         p.rt(90)
#     p.end_fill()


# def circle(p, radius, color):
#     p.color(color)
#     p.begin_fill()
#     p.circle(radius)
#     p.end_fill()


# def pentagon(p, size, color):
#     p.color(color)
#     p.begin_fill()
#     for _ in range(5):
#         p.fd(size)
#         p.lt(72)
#     p.end_fill()


# start = input("square/circle/pentagon (stop to end): ").lower()

# while start != "stop":
#     if start == "square":
#         size = int(input("Enter a size: "))
#         color = input("Enter a color: ")
#         square(pencil, size, color)

#     elif start == "circle":
#         radius = int(input("Enter radius: "))
#         color = input("Enter a color: ")
#         circle(pencil, radius, color)

#     elif start == "pentagon":
#         size = int(input("Enter a size"))
#         color = input("Enter a color: ")
#         pentagon(pencil, size, color)

#     else:
#         print("Error: Shape not found!")

#     start = input("square/circle/pentagon (stop to end): ").lower()

# done()

# -----------------------------------------------------------------
# Draw 10 circles, each at a random location with a random radius
# -----------------------------------------------------------------
# from random import *

# pencil = Turtle()

# count = int(input("How many circles do you want to draw?: "))

# while count:
#     for _ in range(count):
#         radius = randint(5, 100)
#         x = randint(-200, 200)
#         y = randint(-200, 200)

#         r = randint(0, 255)
#         g = randint(0, 255)
#         b = randint(0, 255)

#         color = (r / 255, g / 255, b / 255)

#         pencil.up()
#         pencil.goto(x, y)
#         pencil.down()

#         pencil.color(color)
#         pencil.begin_fill()
#         pencil.circle(radius)
#         pencil.end_fill()

#     count = int(input("How many circles do you want to draw?: "))

# done()

# -----------------------------------------------------------------
# Create 3 objects, that'll draw 3 triangles in a column, all a different color
# -----------------------------------------------------------------
t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t4 = Turtle()


def triangle(t, color):
    t.color(color)
    t.begin_fill()
    for _ in range(3):
        t.fd(100)
        t.lt(120)
    t.end_fill()


turtles = [t1, t2, t3, t4]

y = 100
for t in turtles:
    t.up()
    t.goto(0, y)
    t.down()
    y -= 100

triangle(t1, "blue")
triangle(t2, "red")
triangle(t3, "green")
triangle(t4, "yellow")

done()
