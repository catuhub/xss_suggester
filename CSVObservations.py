import CSVUtil
import os
from BaseElement import ComposedElement
from BaseElement import BaseElement
from Observation import Observation

class CSVObservations(object):
    DELIMITER_OBSERVATION = "observation_"
    def _readObservationFile(self):
        """Docstring for readActionFile """
        csvObj = CSVUtil.readCSV(self.observationFile, self.delimiter)
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
        self.observationFile = os.path.join(basedata, "observations.csv")
        self._readObservationFile()

    def getCategories(self):
        """Returns the  list of categories"""
        return self.actionElements.getCategories()

    def createObservation(self, header, row):
        """Create an action from a row
        :row: the row
        :returns: the parsed action
        """
        idRow = row[0]
        observationElements = {}
        for i in range(len(header)):
            if CSVObservations.DELIMITER_OBSERVATION in header[i]:
                # Take all the actions of the category
                category = header[i]
                idObservation = row[i]
                # Get all elements of the category
                categoryElements = self.actionElements.getElementsByCategory(category)
                # Get the currect value for that action
                if idObservation != "":
                    obsInstance  = categoryElements.getElement(idObservation)
                    if obsInstance is None:
                        print "WARN: no %s idObservation" % (idObservation)
                    observationElements[category] = obsInstance
                else:
                    obsInstance  = categoryElements.getElement(idObservation)
                    obsInstance = BaseElement.empty(category)
                    observationElements[category] = obsInstance
        return Observation(observationElements,idRow)
