# My very first python program ever, I expect to be crucified
# I will be commenting exhaustively becuase I know I'll look at this in the future and have no idea what is happening
# sens means sensitivity

import random

# declaring variables
system = 'metric' # metric or imperial
dpi = 800 # mouse DPI
game = 'ow' # the game to generate sensitvity for
minsens = 20 # minimum sensitivity (in cm/360)
maxsens = 50 # maximum sensitivity (in cm/360)

# cm/360 sens generation
# getting a random float between min and max variables, then rounding it to 2 decimal places
gen360 = (round(random.uniform(minsens,maxsens), 2))
# converting to string to print
sgen360 = str(gen360)


# ow sens generation
# getting the random float from cm/360 generation, will be converted into ow sensitivity using player's DPI
genow = (gen360)

# printing cm/360 generated sens
# gonna replace this with an if to choose ow or cm/360 for the next version
print (sgen360 + ' cm/360')
