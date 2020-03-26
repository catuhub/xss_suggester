# -*- coding: utf-8 -*-
import base64
import csv
import ast
import numpy as np
class Action():

    ID_DELIM = "|||"

    def __dictReorder(self, item):
        return {k: sort_dict(v) if isinstance(v, dict) else v for k, v in sorted(item.items())}

    def __init__(self, actionElements, rank, idRow):
        # An action elements is a dict containing all BaseElements with the category
        self.__actionElements = self.__dictReorder(actionElements)
        self.__idRow = idRow
        self.string = {'PreContext': '', 'Context': '', 'PreExploit': '', 'ExploitCode': '', 'PostContext': ''}
        self.id = base64.b64encode(Action.ID_DELIM.join(str(x.getName().strip()) for x in self.__actionElements.values()))
        self.rank = rank

    def getActionElements(self):
        return self.__actionElements
        
    def getSubActions(self):
        return self.__actionElements.iteritems()

    def getReward(self):
        return self.rank

    def __str__(self):
        retStr = ""
        subActions = self.getSubActions()
        for k, v in subActions:
            retStr = retStr + k + ":" + str(v) + "\n"
        return retStr

    def getID(self):
        """
        :returns: id
        """
        return self.id
    
    def getString(self):
        return self.string

    def setString(self):
        name = self.__actionElements["action_agent"].getName()
        if(name != "bootstrap"):
            print(str(self.__dictReorder(self.string)))
            with open("./q_tables/q_table_simple_html.csv", "r") as csv_file:
                reader = csv.reader(csv_file)
                i = 0
                for row in reader:
                    if(i!= 0):
                        res = ast.literal_eval(row[0])
                        if (cmp(res,self.string) == 0):
                            if(self.__actionElements["action_place"].getName() == "ExploitCode"):
                                q_values = np.asarray(row[15:17],dtype=np.float64)
                                actionString = header_ExploitCode[np.argmax(q_values)]
                                actionDict = ast.literal_eval(actionString)
                            elif(self.__actionElements["action_place"].getName() == "PreContext"):
                                q_values = np.asarray(row[1:11],dtype=np.float64)
                                print(q_values)
                                actionString = header_PreContext[np.argmax(q_values)]
                                actionDict = ast.literal_eval(actionString)
                            elif(self.__actionElements["action_place"].getName() == "Context"):
                                q_values = np.asarray(row[11:15],dtype=np.float64)
                                print(q_values)
                                actionString = header_Context[np.argmax(q_values)]
                                actionDict = ast.literal_eval(actionString)
                                print(actionDict)
                            elif(self.__actionElements["action_place"].getName() == "PostContext"):
                                q_values = np.asarray(row[20:23],dtype=np.float64)
                                actionString = header_PostContext[np.argmax(q_values)]
                                actionDict = ast.literal_eval(actionString)
                            elif(self.__actionElements["action_place"].getName() == "PreExploit"):
                                q_values = np.asarray(row[17:20],dtype=np.float64)
                                actionString = header_PreExploit[np.argmax(q_values)]
                                actionDict = ast.literal_eval(actionString)    
                            self.string[actionDict["place"]] = actionDict["substring"]
                    else:
                        header_PreContext = row[1:11]
                        header_Context = row[11:15]
                        header_ExploitCode = row[15:17]
                        header_PreExploit = row[17:20]
                        header_PostContext = row[20:23]
                    i += 1

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Action):
            return self.getID() == other.getID()
        return False

    def __ne__(self, other):
        """Overrides the default implementation (unnecessary in Python 3)"""
        return not self.__eq__(other)

