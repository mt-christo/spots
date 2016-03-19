from __future__ import print_function
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Spot(object):
    def __init__(self, patch, figure, letters, colors):
        self.patch = patch
        self.figure = figure
        self.subplot = figure.add_subplot(111)
        self.letters = letters
        self.colors = colors
        self.figure.canvas.mpl_connect('key_press_event', self.press)
        
    def press(self, event):
        for i, p in enumerate(self.letters):
            if event.key == p:
                print('press', p)
                self.patch.set_color(self.colors[i])
                self.figure.canvas.draw()
         
    def draw(self):
        self.subplot.add_patch(self.patch)
        plt.axis('scaled')
        plt.show()
 
class Spots(object):
    def __init__(self):
        self.spots = []
        
    #def draw(self):
        #for s in self.spots:
    
def press(event):
    print('press', event.key)
    #sys.stdout.flush()
    #if event.key == 'x'

#fig, ax = plt.subplots()

#fig.canvas.mpl_connect('key_press_event', press)

#showKirill(myDraw)
