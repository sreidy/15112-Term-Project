# information of Vjoystics 
# sourece : http://code.google.com/p/fscode/wiki/SimScript

# code used with mission planning sowtware to test what each 
#V joystick motion does. 

import joysticks,math,state

vjoy = joysticks.get("vJoy Device")

loop = state.inc("loop")

# rotate all axis
for a in range(0,vjoy.numAxis()): 
    vjoy.setAxis(a,math.sin(loop/10.0 + a * math.pi/8.0))

# go through buttons
for b in range(0,vjoy.numButtons()):
    vjoy.setButton(b, False)
vjoy.setButton(int(loop/10.0 % vjoy.numButtons()), True)    

