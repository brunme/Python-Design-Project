from MedinaFunctions import*
turtle.colormode(255)
turtle.bgcolor(0,0,0)
bob.speed(0)

jump(-660,335)

for times in range(27):
    mstar(75,(50+times*4,0,0))
    bob.speed(0)
    jump(-660+times*50,335)

bob.speed(0)
jump(660,260)
bob.right(180)

for times in range(27):
    mstar(75,(0,50+times*4,0))
    bob.speed(0)
    jump(660-times*50,260)

bob.speed(0)
jump(-660,185)
bob.right(180)

for times in range(27):
    mstar(75,(0,0,50+times*4))
    bob.speed(0)
    jump(-660+times*50,185)

bob.speed(0)
jump(660,110)
bob.right(180)

for times in range(27):
    mstar(75,(50+times*4,0,50+times*4))
    bob.speed(0)
    jump(660-times*50,110) 

bob.speed(0)
jump(-660,35)
bob.right(180)

for times in range(27):
    mstar(75, (0,50+times,50+times))
    bob.speed(0)
    jump(-660+times*50,35)

bob.speed(0)
jump(660,-40)
bob.right(180)

for times in range(27):
    mstar(75,(50+times,50+times,0))
    bob.speed(0)
    jump(660-times*50,-40)

bob.speed(0)
jump(-660,-115)
bob.right(180)

for times in range(27):
    mstar(75,(147+times*4,75+times*4,0))
    bob.speed(0)
    jump(-660+times*50,-115)

bob.speed(0)
jump(660,-190)
bob.right(180)

for times in range(27):
    mstar(75,(100+times*4,75+times*4,50+times*4))
    bob.speed(0)
    jump(660-times*50,-190)

bob.speed(0)
jump(-660,-265)
bob.right(180)

for times in range(27):
    mstar(75,(50+times*4,75+times*4,100+times*4))
    bob.speed(0)
    jump(-660+times*50,-265)

bob.speed(0)
jump(660,-340)
bob.right(180)

for times in range(27):
    mstar(75,(147+times*4,147+times*4,147+times*4))
    bob.speed(0)
    jump(660-times*50,-340)
