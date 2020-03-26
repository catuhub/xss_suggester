# -*- coding: utf-8 -*-
from Action import Action
from Observation import Observation
from HackingState import HackingState
from HackingGoal import HackingGoal
from BaseElement import BaseElement
from BaseElement import ComposedElement
import CSVUtil
from CSVHackingState import CSVHackingState
import os
import sys


class CSVModelManager():
    def getCategories(self):
        """Returns all getCategories
        :returns: categories
        """
        return CSVUtil.getOnlyDirs(self.categoryDir)

    def __init__(self, baseDir = "data", delimiter=","):
        """Manage all csv in directories"""
        self.hg = None
        self.baseDir = baseDir
        self.delimiter = delimiter
        self.categoryDir = os.path.join(self.baseDir, "categories")
        pass


    def generateHackingGoal(self, category, goal):
        """Returns an hacking goal from a csvfile
        :returns the hacking goal
        """
        self.stateParser = CSVHackingState(self.baseDir, category, goal)
        self.stateParser.generateEmptyStates()
        self.stateParser.fillEmptyStates()
        initialState = self.stateParser.getInitialState()
        print("The initial state is: ", initialState)
        initialString = {'PreContext': '', 'Context': '', 'PreExploit': '', 'ExploitCode': '', 'PostContext': ''}
        self.hg = HackingGoal(goal="", category=category, initialState=initialState, initialString = initialString)
        return self.hg

    def getHackingGoal(self):
        """Returns the hacking ogal
        :returns: hg
        """
        return self.hg

    def getGoalsByCategory(self, category):
        """returns the list of goals by category
        :category: the category
        :returns: the list of csv
        """
        csvFiles =  CSVUtil.getOnlyCSV(os.path.join(self.categoryDir, category))
        return [os.path.splitext(o)[0] for o in csvFiles]

    # def setCurrentHackingGoal(self, category, nameHackingGoal):
    #     """ set the current hacking goal
    #     :nameHackingGoal: the name of hacking goal
    #     """
    #     self.hackingGoal = self.getHackingGoal(category, nameHackingGoal+".csv")
