from __future__ import division
from tkinter import *
import time
import math
import balls
import random

WIDTH = 800
HEIGHT = 800
colorRange = (30,60)
colorSpeed = 1
MoveSpeed = 2.5

def give_move(xball, yball, xcenter, ycenter, deg):
    rad = math.sqrt((xcenter-xball)**2 + (ycenter-yball)**2)
    return (math.cos(math.radians(deg))*rad - xball) + xcenter, (math.sin(math.radians(deg))*rad - yball) + ycenter

def allow_move(allow, ball, deg):
    if allow:
        posball = canvas.coords(ball)
        poscenter = canvas.coords(center_point)
        movex, movey = give_move(posball[0], posball[1], poscenter[0], poscenter[1], deg)
        canvas.move(ball, movex, movey)

if __name__ == "__main__":
    tk = Tk()
    canvas = Canvas(tk, bg="gray50", width=WIDTH, height=HEIGHT)
    tk.title("illusion")
    canvas.pack()
    ballarray = []
    ballinfoarray = []
    for x in balls.info:
        balldegree = math.degrees(math.atan(abs(400 - x[0])/abs(400 - x[1])))
        if x[0] < 400 and x[1] < 400:
            balldegree = balldegree + 270
        if x[0] > 400 and x[1] > 400:
            balldegree = balldegree + 90
        if x[0] < 400 and x[1] > 400:
            balldegree = balldegree + 180
        ballcolor = random.randint(colorRange[0],colorRange[1])
        ballarray.append(canvas.create_oval(x[0],x[1],x[0]+20,x[1]+20,fill="gray"+str(ballcolor)))
        ballinfoarray.append([ballcolor,colorSpeed,balldegree])
    center_point = canvas.create_oval(400, 400, 405, 405, fill="black")
    deg = 0
    outdegchange = MoveSpeed
    start_time = time.time()
    outmove = True
    i = 0
    while True:
        i = i + 1
        elapsed_time = time.time() - start_time
        if (int(round(elapsed_time)) - (int(round(elapsed_time)) % 5)) % 2 == 0:
            outmove = True
            outdegchange = MoveSpeed
        else:
            outmove = False
            outdegchange = 0
        move = outmove
        degchange = outdegchange
        if deg == 360:
            deg = 0
        
        for index in range(0, len(ballarray)):
            
            if ballinfoarray[index][0] >= colorRange[1] or ballinfoarray[index][0] <= colorRange[0]:
                ballinfoarray[index][1] = -ballinfoarray[index][1]
            canvas.itemconfig(ballarray[index], fill="gray"+str(ballinfoarray[index][0]))
            ballinfoarray[index][0] = ballinfoarray[index][0] + ballinfoarray[index][1]

            if ballinfoarray[index][2] == 360:
                ballinfoarray[index][2] = 0
            allow_move(move, ballarray[index], ballinfoarray[index][2])
            ballinfoarray[index][2] = ballinfoarray[index][2] + degchange
        
        tk.update()
        deg = deg + degchange
    tk.mainloop()
