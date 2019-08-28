from __future__ import division
from tkinter import *
import time
import math
import squarearrangement
import random

WIDTH = 800
HEIGHT = 800
colorRange = (10,40)
colorSpeed = 1
MoveSpeed = 5

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
    for x in squarearrangement.info:
        movementState = 0
        if x[1] < 100:
            movementState = 0
        if x[0] > 700:
            movementState = 1
        if x[1] > 700:
            movementState = 2
        if x[0] < 100:
            movementState = 3
        ballcolor = random.randint(colorRange[0],colorRange[1])
        ballarray.append(canvas.create_oval(x[0],x[1],x[0]+20,x[1]+20,fill="gray"+str(ballcolor),width=0))
        offset = 0
        if movementState == 0:
            offset = 100 - x[1]
        elif movementState == 1:
            offset = x[0] - 700
        elif movementState == 2:
            offset = x[1] - 700
        elif movementState == 3:
            offset = 100 - x[0]
        ballinfoarray.append([ballcolor,colorSpeed,movementState, offset])
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
            if elapsed_time - int(round(elapsed_time)) > 0:
                outdegchange = -MoveSpeed
            else:
                outdegchange = MoveSpeed
        else:
            outmove = False
            outdegchange = 0
        move = outmove
        degchange = outdegchange
        
        for index in range(0, len(ballarray)):
            
            if i % 2 == 0:
                
                if ballinfoarray[index][0] >= colorRange[1] or ballinfoarray[index][0] <= colorRange[0]:
                    ballinfoarray[index][1] = -ballinfoarray[index][1]
                canvas.itemconfig(ballarray[index], fill="gray"+str(ballinfoarray[index][0]))
                ballinfoarray[index][0] = ballinfoarray[index][0] + ballinfoarray[index][1]

                if ballinfoarray[index][2] == 0:
                    if canvas.coords(ballarray[index])[0] > 700 + ballinfoarray[index][3]:
                        ballinfoarray[index][2] = 1
                elif ballinfoarray[index][2] == 1:
                    if canvas.coords(ballarray[index])[1] > 700 + ballinfoarray[index][3]:
                        ballinfoarray[index][2] = 2
                elif ballinfoarray[index][2] == 2:
                    if canvas.coords(ballarray[index])[0] < 100 - ballinfoarray[index][3]:
                        ballinfoarray[index][2] = 3
                elif ballinfoarray[index][2] == 3:
                    if canvas.coords(ballarray[index])[1] < 100 - ballinfoarray[index][3]:
                        ballinfoarray[index][2] = 0

                if move:
                    if ballinfoarray[index][2] == 0:
                        canvas.move(ballarray[index],MoveSpeed,0)
                    elif ballinfoarray[index][2] == 1:
                        canvas.move(ballarray[index],0,MoveSpeed)
                    elif ballinfoarray[index][2] == 2:
                        canvas.move(ballarray[index],-MoveSpeed,0)
                    elif ballinfoarray[index][2] == 3:
                        canvas.move(ballarray[index],0,-MoveSpeed)
     
        tk.update()
    tk.mainloop()
