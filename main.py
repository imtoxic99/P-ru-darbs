import viz
import vizact

viz.go()
viz.mouse(viz.ON)

model = viz.add('models/tinker.obj')
model.setPosition([0, 0, 5])
model.setScale([0.1, 0.1, 0.1])

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
