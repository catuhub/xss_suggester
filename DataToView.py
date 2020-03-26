import json
import cgi

"""Converter from data to view"""

def convertObservation(o):
    subObservations = o.getSubObservations()
    obs = []
    for k, v in subObservations:
        obs.append({
                'category' : v.getCategory(),
                'name': v.getName(),
                'description': v.getDescription()
        })

    return {o.getID() : obs}

def convertAction(action, string):
    subActions = action.getSubActions()
    print(string)
    actions = []
    for k, v in subActions:
        actions.append({
            'category' : v.getCategory(),
            'name': v.getName(),
            'description': v.getDescription()
        })
    return {action.getID() : {
        'reward' : action.getReward(),
        'subActions' : actions,
        'string' : cgi.escape(string["PreContext"] + string["Context"] + string["PreExploit"] + string["ExploitCode"] + string["PostContext"])}
        }


def response(ERR_CODE, theId = None, theObject = None):
    retObj = {}
    retObj['status'] = ERR_CODE
    if theId:
       retObj[theId] =  theObject
    return json.dumps(retObj)
