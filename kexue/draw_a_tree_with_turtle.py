from turtle import Turtle
import time


def tree(tlist, l, a, f):
    if l > 5:
        lst = []
        for t in tlist:
            t.forward(l)
            p = t.clone()
            t.left(a)
            p.right(a)
            lst.append(t)
            lst.append(p)
            time.sleep(1)
        tree(lst, l*f, a, f)


def main():
    t = Turtle()
    t.color('green')
    t.pensize(5)
    #t.hideturtle()
    #t.speed(1)
    t.getscreen().tracer(30, 0)
    t.left(90)
    t.penup()
    t.goto(0, -200)
    t.pendown()
    tree([t], 150, 60, 0.6)


if __name__ == '__main__':
    main()
