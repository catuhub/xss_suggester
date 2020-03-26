import CSVUtil
import os
from BaseElement import ComposedElement
from BaseElement import BaseElement
from Action import Action
import sys

class CSVActions(object):
    DELIMITER_ACTION = "action_"
    ACTION_ID = "reward"
    def _readActionFile(self):
        """Docstring for readActionFile """
        csvObj = CSVUtil.readCSV(self.actionfile, self.delimiter)
        rows = csvObj['listRows']
        self.actionElements = ComposedElement()
        # Use for loop to print csv row by row
        for row in rows:
            be = BaseElement(row[0], row[1], row[2].lower())
            self.actionElements.addElement(be)

    def __init__(self, basedata):
        """Docstring for CSVActions. """
        self.basedata = basedata
        self.delimiter = ","
        self.actionfile = os.path.join(basedata, "actions.csv")
        self._readActionFile()

    def getCategories(self):
        """Returns the  list of categories"""
        return self.actionElements.getCategories()

    def createAction(self, header, row):
        """Create an action from a row
        :row: the row
        :returns: the parsed action
        """
        rank = 1
        idRow = row[0]
        actionElements = {}
        for i in range(len(header)):
            if CSVActions.ACTION_ID == header[i]:
                rank = row[i]
            elif CSVActions.DELIMITER_ACTION in header[i]:
                # Take all the actions of the category
                category = header[i]
                idAction = row[i]
                # Get all elements of the category

                categoryElements = self.actionElements.getElementsByCategory(category)
                if idAction != "":
                    # Get the currect value for that action
                    actionInstance = categoryElements.getElement(idAction)
                    if actionInstance is None:
                        print "WARN: no %s idAction" % (idAction)
                    actionElements[category] = actionInstance
                else:
                    actionInstance = BaseElement.empty(category)
                    actionElements[category] = actionInstance

        return Action(actionElements, rank, idRow)
        pass
