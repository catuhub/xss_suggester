# -*- coding: utf-8 -*-
import ast
import csv
import numpy as np
class HackingGoal():
    """An hacking goal"""

    def __init__(self, goal, category, initialState, initialString):
        """ initialize the hacking goal
        a goal
        a category
        the initial state
        """
        self.__goal = goal
        self.__category = category
        self.__currentState= initialState
        self.__currentString = initialString

    def acquireObservation(self, observationID):
        """
            Acquire the observation from the environment
            Update the current state
            :observation: the observation
        """
        self.__currentState.acquireObservation(self, observationID)

    def setState(self, state):
        self.__currentState = state

    def getState(self):
        """Get the current state
        :returns: the current state
        """
        return self.__currentState


    def suggestActions(self):
        """suggest the action for the pentester
            :returns: the action for the pentester
        """
        return self.__currentState.suggestActions()

    def displayCurrentObservations(self):
        """Display the current observations for the user
            :returns: TODO
        """
        return self.__currentState.availableObservations()

    def setCurrentString(self, action):
        currentString = self.__currentString
        subActions = action.getActionElements()
        name = subActions["action_agent"].getName()
        
        if(name != "no_agent"):
            with open("./q_free_tables/q_table_" + name + ".csv", "r") as csv_file:
                print("in set current string", name)
                reader = csv.reader(csv_file)
                i = 0
                for row in reader:
                    if(i!= 0):
                        res = ast.literal_eval(row[0])                        
                        if (cmp(res,currentString) == 0):
                            print("Current string", currentString)
                            print("RES", res)
                            if(subActions["action_place"].getName() == "ExploitCode"):
                                q_values = np.asarray(row[15:17],dtype=np.float64)
                                actionString = header_ExploitCode[np.argmax(q_values)]
                                actionDict = ast.literal_eval(actionString)
                                self.__currentString[actionDict["place"]] = actionDict["substring"]
                                break
                            elif(subActions["action_place"].getName() == "PreContext"):
                                q_values = np.asarray(row[1:11],dtype=np.float64)
                                print(q_values)
                                actionString = header_PreContext[np.argmax(q_values)]
                                actionDict = ast.literal_eval(actionString)
                                self.__currentString[actionDict["place"]] = actionDict["substring"]
                                break
                            elif(subActions["action_place"].getName() == "Context"):
                                q_values = np.asarray(row[11:15],dtype=np.float64)
                                actionString = header_Context[np.argmax(q_values)]
                                actionDict = ast.literal_eval(actionString)
                                print(actionDict)
                                self.__currentString[actionDict["place"]] = actionDict["substring"]
                                break
                            elif(subActions["action_place"].getName() == "PostContext"):
                                q_values = np.asarray(row[21:25],dtype=np.float64)
                                actionString = header_PostContext[np.argmax(q_values)]                               
                                actionDict = ast.literal_eval(actionString)
                                print("Action Dict PostContext", actionDict)
                                self.__currentString[actionDict["place"]] = actionDict["substring"]
                                break
                            elif(subActions["action_place"].getName() == "PreExploit"):
                                q_values = np.asarray(row[17:21],dtype=np.float64)
                                actionString = header_PreExploit[np.argmax(q_values)]
                                actionDict = ast.literal_eval(actionString)
                                self.__currentString[actionDict["place"]] = actionDict["substring"]
                                break
                    else:
                        header_PreContext = row[1:11]
                        header_Context = row[11:15]
                        header_ExploitCode = row[15:17]
                        header_PreExploit = row[17:21]
                        header_PostContext = row[21:25]
                    i += 1
    def getCurrentString(self):
        return self.__currentString