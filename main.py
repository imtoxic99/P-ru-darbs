import viz
import vizact

viz.go()
viz.mouse(viz.ON)

model = viz.add('models/tinker.obj') # или 'tinker.obj'
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
rainbow_action = None

def startRainbow():
    global rainbow_action
    steps = []
    for c in RAINBOW:
        steps.append(vizact.method.color(model, c))
        steps.append(vizact.waittime(0.12))
        rainbow_action = vizact.sequence(steps)
        model.addAction(vizact.loop(rainbow_action))

def stopRainbowAndRestore():
    global rainbow_action
    model.clearActions()
    rainbow_action = None
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
