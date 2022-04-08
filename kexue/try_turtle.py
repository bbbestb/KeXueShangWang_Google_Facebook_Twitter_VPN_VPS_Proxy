# *-* coding=utf-8 *-*
import turtle
import time
#定义绘制时画笔的颜色
turtle.color("purple")
#定义绘制时画笔的线条的宽度
turtle.pensize(5)
#定义绘图的速度
turtle.speed(10)
#以0,0为起点进行绘制
turtle.goto(0,0)
#绘出正方形的四条边
for i in range(4):
    turtle.forward(100)
    turtle.right(90)
#画笔移动到点(-150,-120)时不绘图
turtle.up()
turtle.goto(-150,-120)
#再次定义画笔颜色
turtle.color("red")
#在(-150,-120)点上打印"Done"
turtle.write("Done")
turtle.done()
#time.sleep(10)
