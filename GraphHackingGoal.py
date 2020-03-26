import pydot

class GraphHackingGoal():
    stateDraw = {}

    """Docstring for GraphHackingGoal. """
    def __init__(self, hg, filename):
        self.hg = hg
        self.filename = filename
        self.graph = pydot.Dot(graph_type='digraph')
        pass


    def _draw(self, s):
        print "Current state %s " % s.getName()
        if s.getName() not in GraphHackingGoal.stateDraw.keys():
            originNode = self.nodeState(s)
        else:
            originNode  = GraphHackingGoal.stateDraw[s.getName()]
        self.graph.add_node(originNode)
        observations = s.availableObservations()
        for o in observations:
            idObservation = o.getID()
            obsStateMap = s.getObservationStateMap()
            obsState = obsStateMap[idObservation]
            newState = obsState.state
            if newState.getName() == s.getName():
                print "WARN: %s in loop" % (newState.getName())
                return
            elif not newState.isFinalState():
                 self._draw(newState)
            newObs = obsState.obs
            # Draw the state if does not exists
            if newState.getName() not in GraphHackingGoal.stateDraw.keys():
                print "Print %s" % newState.getName()
                ns = self.nodeState(newState)
                currentNode = ns
                self.graph.add_node(ns)
            else:
                # The node was previously created
                currentNode = GraphHackingGoal.stateDraw[newState.getName()]
            # Add the edge between nodes
            self.graph.add_edge(pydot.Edge(originNode, currentNode, label=self.stringObservation(o)))
        self.graph.write_png(self.filename)

    def draw(self):
        """Draw  hacking goal """
        # Initial State
        s = self.hg.getState()
        self._draw(s)

    def getStates(obsStateMap):
        return [s.state.getName() for s in obsStateMap.iteritems()]


    def stringObservation(self, o):
        strInNode =  "Observation:"
        strInNode += "\n"+"-"* 50 + "\n"
        so = o.getSubObservations()
        for k, v in so:
            if v.getName() != "":
                strInNode +=  k + " - " + v.getDescription() + "\n"
        strInNode += "\n"+"-"* 50 + "\n"
        return strInNode

    def stringAction(self, a):
        strInNode = "\n"+"-"* 50 + "\n"
        subActions = a.getSubActions()
        for k, v in subActions:
            if v.getName() != "":
                strInNode +=  k + " - " + v.getDescription() + "\n"
        strInNode +="-"*50  + "\n"
        return strInNode
    # node_a = pydot.Node(stateName, style="filled", fillcolor="red")

    def nodeState(self, state):
        """ generate the node state """
        strInNode = ""
        stateName = state.getName()
        strInNode = stateName + "\n----------------------\n"
        actions = state.suggestActions()
        idAction = 1
        for i in actions:
            strInNode +=  "Action n. %s %s" % (str(idAction), self.stringAction(i))
            idAction += 1
        # node_a = pydot.Node(stateName, style="filled", fillcolor="red")
        node_a = pydot.Node(strInNode)
        GraphHackingGoal.stateDraw[stateName] = node_a
        return node_a
