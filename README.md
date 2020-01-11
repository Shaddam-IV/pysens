# pysens
## Sensitivity generator for various games

Current featues:
* Generates a random sensitivity for selected game
* Accepts custom DPI and sensitivity range

Supported games:
* Overwatch
* Fortnite
* Counter-Strike
* Quake Champions

Planned features:
* Error handling, if you do something the program doesn't like, it can be hard to tell what went wrong
* Converting sensitivities between games
* Listing availabe games in-program
* Better documentation

## Dependencies
* Python (obviously)

## Usage

Should work with any OS

Simply call it from the terminal with desired game

This will generate a random sensitivity for Overwatch:
```
python3 pysens.py ow
```
Output:
```
8.06 in Overwatch settings (21.49cm/360)
setttings: 800 DPI, 15cm - 50cm
```
You can specify some options with flags

-d or --dpi : Change the DPI your mouse is configured as

-l or --lower : The lower sensitivity bound (in cm/360)

-u or --upper : The upper sensitivity bound (in cm/360)

#### Example:

Here I'm asking for a Counter-Strike sensititvity, my dpi is 400 and I want it between 30 and 70 cm/360
```
python3 pysens.py csgo --dpi 400 -l 30 -u 70
```
And it spits out:
```
2.86 in Counter-Strike settings (36.35cm/360)
setttings: 400 DPI, 30cm - 70cm
```
## Current games
```
ow - Overwatch
fn - Fortnite (In-game slider)
csgo - Counter-Strike
qc - Quake Champions
```
## Disclaimer

I'm new to coding, I know nothing. This is my attempt to learn by making projects I want. Please rip apart my code and tell me what to do better.

I don't even know how to use git from the command line yet.
