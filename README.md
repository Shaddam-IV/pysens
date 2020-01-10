# pysens
Sensitivity tool for various games
> Currently only generates in-game setting for Overwatch

> You can still use the generated cm/360 in other games, but you will have to convert it yourself until I implemet other games

Current featues:
* Generates a random sensitivity between 20 cm/360 and 50 cm/360 for when you want to try out a new sensitivity
* Outputs the sensitivity as cm/360 or in-game setting
  * Overwatch only for now
* Takes into account user DPI

Planned features:
* Change prompts to command line flags
* Generate random sensitivity for other popular games
* Convert sensitivity between games
  * Support different conversion methods, cm/360, FOV scaling, etc
* Whatever else I think of

## Dependencies
* Python (obviously)

## Usage

Should work with any OS

Simply call it from the command line:
```
python3 pysens.py
```

Then answer the prompts (or leave them blank for default values)

Look up how to run python files on your specific platform if it doesn't work for you

## Disclaimer

I'm new to coding, I know nothing. This is my attempt to learn by making projects I want. Please rip apart my code and tell me what to do better.

I don't even know how to use git from the command line yet.
