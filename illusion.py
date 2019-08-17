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

if __name__ == "__main__":
    tk = Tk()
    canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
    tk.title("illusion")
    canvas.pack()
    center_point = canvas.create_oval(400, 400, 405, 405, fill="black")
    ball = canvas.create_oval(400, 10, 420, 30, fill="gray99")
    deg = 0
    i = 11
    j = 1
    while True:
        if i == 99 or i == 10:
            j = -j
        if deg == 360:
            deg = 0
        canvas.itemconfig(ball, fill="gray"+str(i))
        posball = canvas.coords(ball)
        poscenter = canvas.coords(center_point)
        movex, movey = give_move(posball[0], posball[1], poscenter[0], poscenter[1], deg)
        canvas.move(ball, movex, movey)
        tk.update()
        deg = deg + 0.5
        i = i+j
    tk.mainloop()
