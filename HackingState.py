# -*- coding: utf-8 -*-
from Observation import Observation


class HackingState():
    class ObsState():
        def __init__(self, obs, state):
            self.obs = obs
            self.state = state


    """Hacking State class models a state"""
    # def __init__(self, name, description, isFinalState):
    def __init__(self, name, isFinalState):
        self.actions = []
        self.observationStateMap = {}
        self.__name = name
        # self.__description = description
        self.finalState =  isFinalState
    def __eq__(self, other):
        """ a state is equal
        """
        # return self.__class__ == other.__class__ and self.__name == other.__name and other.__description == self.__description
        return self.__class__ == other.__class__ and self.__name == other.__name

    def getName(self):
        """returns the state name
        :returns: name of the state
        """
        return self.__name

    def addAction(self, action):
        """Add the action for the current state
            :action: the current action to do
        """
        noContain = len([a for a in self.actions if a.getID() == action.getID()]) == 0
        # if action not in self.actions:
        if noContain:
            self.actions.append(action)
    def isFinalState(self):
        """Returns True if it is a final state
        :returns: a boolean value
        """
        return self.finalState

    def addObservationState(self, observation, state):
        self.observationStateMap[observation.getID()] = self.ObsState(observation, state)

    def setObservations(self, observations, states):
        """set the observations for this state """
        for i in len(observations):
            self.addObservationState(observations[i], states[i])

    def suggestActions(self):
        """Returns the action to do
        :returns: action
        """
        return self.actions

    def availableObservations(self):
        observations = []
        """Returns the list of available observations"
        :returns: <list> observations
        """
        for k , v in self.observationStateMap.iteritems():
            observations.append(v.obs)
        return observations

    def getObservationStateMap(self):
        return self.observationStateMap

    def acquireObservation(self, hg, obsID):
        """Acquire the observation from the state set the new state"""
        obsState = self.observationStateMap[obsID]
        print "Update state to %s" % (obsState.state.getName())
        newState = obsState.state
        hg.setState(newState)
    def __str__(self):
        """returns the string  description of state
        :returns: a string
        """
        # strRet = "Name: %s \nDescr: %s\nAction: %s\nisFinalState: %s\n" % (self.__name, self.__description, self.action, self.finalState)
        strRet = "Name: %s \nActions: %s\nisFinalState: %s\n" % (self.__name, self.actions, self.finalState)
        observations = "Observations: "
        for k,v in self.observationStateMap.iteritems():
            observations = observations + str(v.obs) + ", "
        return strRet + observations
    def __eq__(self, theState):
        """Overrides the default implementation"""
        if isinstance(theState, HackingState):
            return self.getName() == theState.getName()
        return False

    def __ne__(self, other):
        """Overrides the default implementation (unnecessary in Python 3)"""
        return not self.__eq__(other)
