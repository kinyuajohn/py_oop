from turtle import *

# # create 2 objects
# t1 = Turtle()
# t2 = Turtle()

# t1.color("orange")
# t2.color("purple")

# t1.forward(50)
# t1.left(90)

# t2.left(90)
# t2.forward(50)

# done()

# ----------------------------------------------------------------
# t1 = Turtle()
# t1.color("orange")
# t1.width(5)

# t1.begin_fill()
# for _ in range(5):
#     t1.forward(150)
#     t1.left(144)
# t1.end_fill()

# done()


# ----------------------------------------------------------------
def star(t, width, size, color):
    t.color(color)
    t.width(width)

    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.left(144)
    t.end_fill()


def circle(t, radius, color):
    t.color(color)

    t.begin_fill()
    t.circle(radius)
    t.end_fill()


t = Turtle()

ask = input("Enter shape: ")

while ask != "done":
    if ask == "star":
        width = int(input("Enter width: "))
        colr = input("Enter a color: ")
        size = int(input("Enter a lenght: "))
        star(t, width, size, colr)
    elif ask == "circle":
        radius = int(input("Enter a radius: "))
        colr = input("Enter a color: ")
        circle(t, radius, colr)
    else:
        print("No shape entered")
    ask = input("Enter shape: ")

done()
