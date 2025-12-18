import viz
import vizact
import vizcam

viz.go()
viz.mouse(viz.ON)

vizcam.WalkNavigate()
viz.MainView.setPosition([0, 1.6, 0])

model = viz.add('tinker.obj')
model.setPosition([0, 0, 5])
model.setScale([0.1, 0.1, 0.1])

def onPick():
    model.color(viz.RED)
    model.addAction(vizact.moveTo([0, 1.5, 5], time=1))

vizact.onpick(model, onPick)

RAINBOW = [viz.RED, viz.ORANGE, viz.YELLOW, viz.GREEN, viz.CYAN, viz.BLUE, viz.PURPLE]


is_rainbow = False
rainbow_action = None

def startRainbow():
    global rainbow_action
    seq = vizact.sequence([
        vizact.method.color(model, c),
        vizact.waittime(0.12)
        ] for c in RAINBOW)

    steps = []
        for chunk in seq:
            steps.extend(chunk)

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
