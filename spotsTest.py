from spotsLib import *

s = Spot(5,5,2,'red',circa)

s.behave('k', lambda self: s.recolor('blue') if true else false)

showKirill(s.draw)
