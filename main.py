import viz

viz.go()

model = viz.add('models/tinker.obj')
model.setPosition([0, 0, 5])
model.setScale([0.1, 0.1, 0.1])

def onPick(e):
    if e.object == model:
        model.color(viz.RED)
        model.addAction(vizact.moveTo([0, 1.5, 5], time=1))

viz.callback(viz.PICK_EVENT, onPick)
