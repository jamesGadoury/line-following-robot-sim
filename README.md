# line-following-robot

## Dependencies
- pygame : `pip3 install pygame`

## How to run
- `python3 main.py --manual` : run the simulator using a manual controller, which responds to arrow key presses to move robot
- `python3 main.py`: without the manual flag, the simulator will use a custom controller, which must be implemented in controllers.py

## How to add custom_controller
- Just implement `custom_controller` in controllers.py and run the `main.py` script w/o args. 

## Todos
1. Right now the Robot class relies on lambda functions as controllers, which must be implemented in py scripts. Specifically, the `custom_controller` needs to be implemented in controllers.py. This is very limited. Look into allowing more robust deployment of custom controller code, potentially using json inputs.
2. Inconsistent style, fix at some point.
3. Some places I'm using class constants (sorta kinda not really since this is py) as colors and sizes. Might be better to change these all to default options as class constructor args, so that code is more extensible. 
4. `manual_controller` is relying on events, but `custom_controller` will only care about sensor readings, since they are on a common interface; this is confusing, and likely bad design