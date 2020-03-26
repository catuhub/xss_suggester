# -*- coding: utf-8 -*-
import pytest
from Action import Action
from CSVActions import CSVActions
from CSVObservations import CSVObservations
import CSVUtil
import os
from os import path


def test_actions():
    csvModel = CSVActions("testdata")
    obj = CSVUtil.readCSV("test.csv")
    a = csvModel.createAction(obj['header'], obj['listRows'][0])
    for k, v in a.getSubActions():
         print k
         print v
def test_observations():
    csvModel = CSVObservations("testdata")
    obj = CSVUtil.readCSV("test.csv")
    a = csvModel.createObservation(obj['header'], obj['listRows'][0])
    for k, v in a.getSubObservations():
        print k
        print v
