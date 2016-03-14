from __future__ import print_function
import sys
import numpy as np
import matplotlib.pyplot as plt

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
