from spotsLib import *

s = Spot(patches.Circle((5,5), radius=1, color='red'), plt.figure())
s.add_color('w','red')
s.add_color('q','blue')

s.draw()
