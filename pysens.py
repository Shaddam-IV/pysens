# pysens.py

import random
import argparse
import os
import sys
import math

# Creating the parser
my_parser = argparse.ArgumentParser(description='Generated random sensitivity')

# Add the arguments
my_parser.add_argument('game',
						metavar='game',
						type=str,
						help='Game to generate sensitivity for')
my_parser.add_argument('-d',
						'--dpi',
						action='store',
						help='custom dpi, defaults to 800')
my_parser.add_argument('-l',
						'--lower',
						action='store',
						help='lower sensitivity bound, in cm')
my_parser.add_argument('-u',
						'--upper',
						action='store',
						help='upper sensitivity bound, in cm')

# Execute the parse_args() method
args = my_parser.parse_args()

input_game = args.game

# Game Dictionary

games = {
	#input: [Title, yaw, game sensitivity precision]
	'ow': ['Overwatch', 0.0066, 2],
	'fn': ['Fortnite', 0.005555, 3],
	'csgo': ['Counter-Strike', 0.022, 2],
	'qc': ['Quake Champions', 0.022, 6]
}

# Variables
dpi = 800
minsens = 15
maxsens = 50

# If flag wasn't entered, set default values
if type(args.dpi) == str:
	dpi = int(args.dpi)
else:
	dpi = 800

if type(args.lower) == str:
	minsens = int(args.lower)
else:
	minsens = 15

if type(args.upper) == str:
	maxsens = int(args.upper)
else:
	maxsens = 50

# Generating the random sensitivity
randomfloat = (random.uniform(minsens,maxsens))

# Calculation to convert randomfloat to game sensitivity
# Pulls game yaw and input precision from dictionary
def gensens():
	return round((4572 / (5 * randomfloat * dpi * games.get(input_game)[1])), games.get(input_game)[2])

# Printing output
if input_game in games:
	print(str(gensens()) + ' in ' + games.get(input_game)[0] + ' settings (' + str(round(randomfloat, 2)) + 'cm/360)')
	print('setttings: ' + str(dpi) + ' DPI, ' + str(minsens) + 'cm - ' + str(maxsens) + 'cm')
else:
	print('This game is not supported currently')