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

def allow_move(allow):
    if allow:
        movex, movey = give_move(posball[0], posball[1], poscenter[0], poscenter[1], deg)
        canvas.move(ball, movex, movey)

if __name__ == "__main__":
    tk = Tk()
    canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
    tk.title("illusion")
    canvas.pack()
    center_point = canvas.create_oval(400, 400, 405, 405, fill="black")
    ball = canvas.create_oval(400, 10, 420, 30, fill="gray99")
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
        if i == 99 or i == 9:
            j = -j
        if deg == 360:
            deg = 0
        canvas.itemconfig(ball, fill="gray"+str(i))
        posball = canvas.coords(ball)
        poscenter = canvas.coords(center_point)
        allow_move(move)
        tk.update()
        degchange = outdegchange
        deg = deg + degchange
        i = i+j
    tk.mainloop()
