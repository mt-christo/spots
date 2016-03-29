from __future__ import print_function
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Spot(object):
    def __init__(self, x, y, r, col, figure, subplot):
        self.figure = figure
        self.subplot = subplot
        self._x = x
        self._y = y
        self._r = r
        self._color = col
        self.vx = np.random.random(1)*0.1
        self.vy = np.random.random(1)*0.1
        self.patch = patches.Circle((self._x, self._y), radius = self._r, color = self._color)
        self.subplot.add_patch(self.patch)

    def assign_patch(self):
        #self.patch = patches.Circle((self._x, self._y), radius = self._r, color = self._color)
        self.patch.center = self.x, self.y
        
    def move(self):
        self.x = self._x + self.vx
        self.y = self._y + self.vy

    #def draw(self):
        #self.subplot.add_patch(self.patch)
        #plt.axis('scaled')
        #plt.show()

    @property
    def x(self):
        return self._x
        
    @x.setter
    def x(self, value):
        self._x = value
        self.assign_patch()

    @property
    def y(self):
        return self._y
        
    @y.setter
    def y(self, value):
        self._y = value
        self.assign_patch()

    @property
    def r(self):
        return self._r
        
    @r.setter
    def r(self, value):
        self._r = value
        self.assign_patch()

    @property
    def color(self):
        return self._color
        
    @color.setter
    def color(self, value):
        self._color = value
        self.assign_patch()

         
 
class Spots(object):
    def __init__(self, xs, ys, r, color, figure, subplot, xyborder):
        self.spots = []
        for i, p in enumerate(xs):
            self.spots.append(Spot(xs[i], ys[i], r, color, figure, subplot))
        self.figure = figure
        self.subplot = subplot
        self.xyborder = xyborder
        self.subplot.set_xlim(xyborder[0], xyborder[1])
        self.subplot.set_ylim(xyborder[0], xyborder[1])

    def draw(self):
        #for p in self.spots:
            #p.draw()
        self.figure.canvas.draw()
        #plt.show()
        
    def animate(self, k):
        print(len(self.spots))
        for p1 in self.spots:
            for p2 in self.spots:
                if np.sqrt((p1.x + p1.vx - p2.x - p2.vx)**2 + (p1.y + p1.vy - p2.y - p2.vy)**2)[0] < p1.r + p2.r:
                    v1 = np.array([p1.vx, p1.vy])
                    v1tmp = np.array([p1.vx, p1.vy])
                    v2 = np.array([p2.vx, p2.vy])
                    
                    d12 = np.array([p2.x - p1.x, p2.y - p1.y])
                    d21 = -d12

                    proj12 = d12 * sum(v1*d12) / sum(d12**2)
                    proj21 = d21 * sum(v2*d21) / sum(d21**2)
                    
                    v1 = v1 - proj12 + proj21
                    v2 = v2 - proj12 + proj21
                    
                    p1.vx = v1[0]
                    p1.vy = v1[1]
                    p2.vx = v2[0]
                    p2.vy = v2[1]
            if (p1.x + p1.r + p1.vx)[0] > self.xyborder[1] or (p1.x - p1.r + p1.vx)[0] < self.xyborder[0]:
                    p1.vx = -p1.vx
            if (p1.y + p1.r + p1.vy)[0] > self.xyborder[1] or (p1.y - p1.r + p1.vy)[0] < self.xyborder[0]:
                    p1.vy = -p1.vy
            p1.move()
        self.draw()
        
        
        
    #def draw(self):
        #for s in self.spots:
    
def press(event):
    print('press', event.key)
    #sys.stdout.flush()
    #if event.key == 'x'

#fig, ax = plt.subplots()

#fig.canvas.mpl_connect('key_press_event', press)

#showKirill(myDraw)
