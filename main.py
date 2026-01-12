import viz
import vizact

viz.go()
viz.mouse(viz.ON)

model = viz.add('models/tinker.obj')
model.setPosition([0, 0, 6])
model.setScale([0.2, 0.2, 0.2])

RAINBOW = [
viz.RED,
viz.ORANGE,
viz.YELLOW,
viz.GREEN,
viz.CYAN,
viz.BLUE,
viz.PURPLE
]

is_rainbow = False
color_index = 0
rainbow_timer = None

def rainbowStep():
    global color_index
    model.color(RAINBOW[color_index])
    color_index = (color_index + 1) % len(RAINBOW)

def startRainbow():
    global rainbow_timer
    rainbow_timer = vizact.ontimer(0.12, rainbowStep)

def stopRainbowAndRestore():
    global rainbow_timer, color_index
    if rainbow_timer:
        rainbow_timer.remove()
        rainbow_timer = None
    color_index = 0
    try:
        model.apply()
    except:
        model.color(viz.WHITE)

def onPick():
    global is_rainbow
    if not is_rainbow:
        is_rainbow = True
        startRainbow()
    else:
        is_rainbow = False
        stopRainbowAndRestore()

vizact.onpick(model, onPick)


import viz
import vizact
import vizcam
import vizconnect
import colorsys

viz.go()


VR_ACTIVE = True

try:
    vizconnect.go('my_vr_config.py')
except:
    VR_ACTIVE = False

viz.MainView.setPosition([0, 5, -20])


if not VR_ACTIVE:
    vizcam.WalkNavigate()

    viz.mouse(viz.ON)

    def look_on():
        viz.mouse(viz.OFF)

    def look_off():
        viz.mouse(viz.ON)

    vizact.onmousedown(viz.MOUSEBUTTON_RIGHT, look_on)
    vizact.onmouseup(viz.MOUSEBUTTON_RIGHT, look_off)


else:
    viz.mouse(viz.OFF)


model = viz.add('models/tinker.obj')
model.setPosition([0, 0, 5])
model.setScale([0.2, 0.2, 0.2])
model.setEuler([0, 90, 0])


def moveForward():
    viz.MainView.move([0, 0, 0.3])

vizact.onkeydown('w', moveForward)


is_rainbow = False
hue = 0.0
rainbow_timer = None
HUE_STEP = 0.006

def rainbowStep():
    global hue
    r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    model.color([r, g, b])
    hue = (hue + HUE_STEP) % 1.0

def startRainbow():
    global rainbow_timer
    rainbow_timer = vizact.ontimer(0.02, rainbowStep)

def stopRainbow():
    global rainbow_timer, hue
    if rainbow_timer:
        rainbow_timer.remove()
        rainbow_timer = None
    hue = 0.0
    try:
        model.apply()
    except:
        model.color(viz.WHITE)

def onPick():
    global is_rainbow
    if not is_rainbow:
        is_rainbow = True
        startRainbow()
    else:
        is_rainbow = False
        stopRainbow()

vizact.onpick(model, onPick)
