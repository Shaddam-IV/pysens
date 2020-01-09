# My very first python program ever, don't crucify me

import random

# declaring variables

system = 'metric' # metric or imperial
dpi = 800 # mouse DPI
game = 'ow' # the game to generate sensitvity for
minsens = 20 # minimum sensitivity
maxsens = 50 # maximum sensitivity
printform = 'cm360' # the way the sens is printed

# cm/360 generation

gen360 = (round(random.uniform(minsens,maxsens), 2))
sgen360 = str(gen360)

# ow sens generation

genow = (gen360)

# 

print (sgen360 + ' cm/360')
