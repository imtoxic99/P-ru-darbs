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
