# import the Flask class from the flask module
from flask import Flask, render_template
from CSVModelManager import CSVModelManager
import DataToView

import json

# create the application object
app = Flask(__name__)
manager = CSVModelManager("data")
hg = None


CODE_SUCCESS = 0
CODE_SET_HACKING_GOAL = 1

# use decorators to link the function to a url
@app.route('/')
def home():
    hg = None
    return render_template('index.html')  # render a template

@app.route("/wapt")
def categories():
    categories = manager.getCategories()
    return DataToView.response(CODE_SUCCESS, "categories", categories)

@app.route("/wapt/<string:category>")
def goalsfromcategory(category):
    goals = manager.getGoalsByCategory(category)
    return DataToView.response(CODE_SUCCESS, "goals", goals)

@app.route("/wapt/<string:category>/<string:goal>")
def hackingGoal(category, goal):
    print "Generate hacking goal"
    hg = manager.generateHackingGoal(category, goal)
    return DataToView.response(CODE_SUCCESS)

@app.route("/wapt/ask/finalstate")
def finalState():
    hg = manager.getHackingGoal()
    actionsToRet = []
    if hg is None:
        return DataToView.response(CODE_SET_HACKING_GOAL)
    currentState = hg.getState()
    isFinalState = currentState.isFinalState()
    return DataToView.response(CODE_SUCCESS, "isFinalState", isFinalState)

@app.route("/wapt/ask/actions")
def askActions():
    hg = manager.getHackingGoal()
    actionsToRet = []
    if hg is None:
        return DataToView.response(CODE_SET_HACKING_GOAL)
    actions = hg.suggestActions()
    for o in actions:
        hg.setCurrentString(o)
        a = DataToView.convertAction(o,hg.getCurrentString())
        actionsToRet.append(a)
    return DataToView.response(CODE_SUCCESS, 'actions', actionsToRet)

@app.route("/wapt/tell/observation/<string:idObservation>",  methods=['PUT'])
def tellObservation(idObservation):
    hg = manager.getHackingGoal()
    if hg is None:
        return DataToView.response(CODE_SET_HACKING_GOAL)
    hg.acquireObservation(idObservation)
    return DataToView.response(CODE_SUCCESS)



@app.route("/wapt/ask/observations")
def askObservations():
    hg = manager.getHackingGoal()
    observations = []
    if hg is None:
        return DataToView.response(CODE_SET_HACKING_GOAL)
    availableObservations = hg.displayCurrentObservations()
    for v in availableObservations:
        obs = DataToView.convertObservation(v)
        observations.append(obs)
    return DataToView.response(CODE_SUCCESS, 'observations', observations)


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
