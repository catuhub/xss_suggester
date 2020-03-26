import CSVUtil
from HackingState import HackingState
from CSVActions import CSVActions
from CSVObservations import CSVObservations
import os

class CSVHackingState:
    CURRENTSTATE = "CURRENTSTATE"
    NEXTSTATE = "NEXT_STATE"
    REWARD_ACTION = "REWARD"
    ISENDSTATE = "IS_END_STATE"

    def __init__(self, baseDir, category, goal):
        self.categoryDir = os.path.join(baseDir, "categories")
        csvName = os.path.join(self.categoryDir, category, goal + ".csv")
        self.csvObj = CSVUtil.readCSV(csvName)
        self.observationParser = CSVObservations(baseDir)
        self.actionParser = CSVActions(baseDir)

    def getRewardRow(self, row):
        """ Returns the reward of the word
        :row: the row
        :returns: the reward number
        """
        return float(CSVUtil.getColumnInRow(self.csvObj, row, CSVHackingState.REWARD_ACTION))

    def generateEmptyStates(self):
        """Generate states without actions and observations
        """
        self.states = []
        allRows = self.csvObj['listRows']
        columnsCurrentState = CSVUtil.getColumns(self.csvObj, CSVHackingState.CURRENTSTATE)
        for currentState in columnsCurrentState:           
            testState = HackingState(currentState, False)
            if testState not in self.states:
                self.states.append(HackingState(currentState, False))
        finalStates = self.getFinalStates()
        self.states = self.states + finalStates
    def getStates(self):
        """Returns the states
        :returns: states
        """
        return self.states


    def getNoFinalStates(self):
        """ Returns non final states
        """
        return [s for s in self.states if not s.isFinalState()]

    def fillEmptyStates(self):
        for s in self.getNoFinalStates():
            # Take the first state
            rowsOfState = CSVUtil.getRowsByColumn(self.csvObj, CSVHackingState.CURRENTSTATE, s.getName())
            for r in rowsOfState:
                #currentReward = self.getRewardRow(r)
                nextState = CSVUtil.getColumnInRow(self.csvObj, r, CSVHackingState.NEXTSTATE)
                if nextState != s.getName():
                    # Get next state
                    # Get observation and action in row
                    actionInRow = self.actionParser.createAction(self.csvObj['header'], r)
                    # Add an action to the state
                    s.addAction(actionInRow)
                    sn =  self.getStateByName(nextState)
                    # Add the observation information with the next state
                    observationInRow = self.observationParser.createObservation(self.csvObj['header'], r)
                    s.addObservationState(observationInRow, sn)
                else:
                    print "Row %s has reward 0, skipped" % (r[0])

    def getFinalStates(self):
        finalStates = []
        rowsUnique = []
        rows = CSVUtil.getRowsByColumn(self.csvObj,CSVHackingState.ISENDSTATE, "1")
        endStateIndex = CSVUtil.getIndexColumn(self.csvObj, CSVHackingState.NEXTSTATE)
        cols = list(set([r[endStateIndex] for r in rows]))
        for c in cols:
            finalStates.append(HackingState(c, True))
        return finalStates

    def getStateByName(self, theName):
        """Returns a state by name
        :returns: the state with the name
        """
        # for i in self.states:
        #     print i.getName()
        return next((x for x in self.states if x.getName() == theName), None)

    def getInitialState(self):
        """ Returns the initial state
        :returns: a state that is not present in next state
        """
        nextStateNames = CSVUtil.getColumns(self.csvObj, CSVHackingState.NEXTSTATE)
        print("next state names",nextStateNames)
        stateNames = CSVUtil.getColumns(self.csvObj, CSVHackingState.CURRENTSTATE)
        print("state names", stateNames)
        initialStates = [s for s in stateNames if s not in nextStateNames]
        theInitialState = initialStates[0]
        initialState = self.getStateByName(theInitialState)
        return initialState
