from __future__ import print_function
import sys
import numpy as np
import matplotlib.pyplot as plt

class Spot(object):
    def __init__(self, x1, y1, r, col, draw_f):
        self.x = x1
        self.y = y1
        self.size = r
        self.color = col
        self.draw_f = draw_f
        
    def recolor(self, new_col):
            self.color = new_col                
        
    def draw(self):
        self.draw_f(self.x,self.y,self.size,self.color)
        
    def behave(self, letter, action):
        fig, ax = plt.subplots()
        fig.canvas.mpl_connect('key_press_event', 
                               lambda event, self: action() if event.key == letter else false)

class Spots(object):
    def __init__(self):
        self.spots = []
        
    def draw(self):
        for s in self.spots:
            s.draw()
            

def circa(x, y, r, col):
    circle = plt.Circle((x, y), radius=r, fc=col)
    plt.gca().add_patch(circle)

def showKirill(drawFunc):
    plt.axes()
    drawFunc()
    plt.axis('scaled')
    plt.show()
    
def myDraw():
    circa(0,0,10,'red')    

def press(event):
    print('press', event.key)
    sys.stdout.flush()
    #if event.key == 'x'

#fig, ax = plt.subplots()

#fig.canvas.mpl_connect('key_press_event', press)

#showKirill(myDraw)
