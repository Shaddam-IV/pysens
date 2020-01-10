# My very first python program ever, I expect to be crucified
# I will be commenting exhaustively becuase I know I'll look at this in the future and have no idea what is happening
# sens means sensitivity

import random

# variables
system = 'metric' # metric or imperial
DPI = 800 # mouse DPI
game = 'Overwatch' # the game to generate sensitvity for
OverwatchYaw = 0.0066
MinSens = 20 # minimum sensitivity (in cm/360)
MaxSens = 50 # maximum sensitivity (in cm/360)
SelectedYaw = 0
output = 'game' # output in either physical (cm/360) or game setting

if game == 'Overwatch':

	SelectedYaw = OverwatchYaw

# cm/360 sens generation
# getting a random float between min and max variables, then rounding it to 2 decimal places
RandomFloat = (random.uniform(MinSens,MaxSens))
RandomFloatRounded = (round(RandomFloat, 2))

# converting rounded float to string in order to print
RandomFloatRoundedString = str(RandomFloatRounded)

# getting DPI before calculations
DPI = input('DPI? Defaults to 800\n')

# testing if DPI is integer or not. I know this is probaly extremely sloppy
if DPI == '':
	DPI = 800
else:
	try:
		DPI = int(DPI)
	except ValueError:
		print ('Please use intergers only')
	finally:
		DPI = int(DPI)

# converting float to ow sensitivity
OverwatchRandomFloat = (4572 / (5 * RandomFloat * DPI * SelectedYaw))
OverwatchRandomFloatRounded = (round(OverwatchRandomFloat, 2))

# converting rounded float to string in order to print
OverwatchRandomFloatRoundedString = str(OverwatchRandomFloatRounded)

# asking user for desired output

output = input("cm/360 or Overwatch output? (enter 'cm' or 'ow') Defaults to game\n")

# printing generated sens

if output == 'cm':
	print (RandomFloatRoundedString + ' cm/360')
elif output == 'ow' or output == '':
	print (OverwatchRandomFloatRoundedString + ' In Overwatch settings')
else:
	print ('you done fucked up')