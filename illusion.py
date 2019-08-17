from tkinter import *
import random
import time
import math
import sys

RAD = 350
WIDTH = 800
HEIGHT = 800

def give_move(xball, yball, xcenter, ycenter, deg):
    return (math.cos(math.radians(deg))*RAD - xball) + xcenter, (math.sin(math.radians(deg))*RAD - yball) + ycenter

def allow_move(allow, ball):
    if allow:
        posball = canvas.coords(ball)
        poscenter = canvas.coords(center_point)
        movex, movey = give_move(posball[0], posball[1], poscenter[0], poscenter[1], deg)
        canvas.move(ball, movex, movey)

if __name__ == "__main__":
    tk = Tk()
    canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
    tk.title("illusion")
    canvas.pack()
    center_point = canvas.create_oval(400, 400, 405, 405, fill="black")
    ballarray = [canvas.create_oval(400, 10, 420, 30, fill="gray30"), canvas.create_oval(10, 400, 30, 420, fill="gray70")]
    ballinfoarray = [[30, 1], [70,1]]
    deg = 0
    outdegchange = 0.5
    i = 11
    j = 2
    start_time = time.time()
    outmove = True
    while True:
        elapsed_time = time.time() - start_time
        if (int(round(elapsed_time)) - (int(round(elapsed_time)) % 5)) % 2 == 0:
            outmove = True
            outdegchange = 0.5
        else:
            outmove = False
            outdegchange = 0
        move = outmove
        if deg == 360:
            deg = 0
        for index in range(0, len(ballarray)):
            
            if ballinfoarray[index][0] == 99 or ballinfoarray[index][0] == 9:
                ballinfoarray[index][1] = -ballinfoarray[index][1]
            canvas.itemconfig(ballarray[index], fill="gray"+str(ballinfoarray[index][0]))
            ballinfoarray[index][0] = ballinfoarray[index][0] + ballinfoarray[index][1]
            
        allow_move(move, ballarray[0])
        tk.update()
        degchange = outdegchange
        deg = deg + degchange
    tk.mainloop()
