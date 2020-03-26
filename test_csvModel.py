# -*- coding: utf-8 -*-
import pytest
from Action import Action
from HackingState import HackingState

from CSVHackingState import CSVHackingState
from os import path

def test_generateEmptyStates():
    hs = CSVHackingState("testdata", "detection", "xss")
    stateNames = ["CheckReflectionString","XSSVulnerable", "CheckUrlString","TestHrefXSS","TestImgInHTML","TestImgSrcXSS","TestXSSCode","TestXSSInAttributeHTML","TestXSSInFunctionBetweenQuotes","TestXSSInHTML","TestXSSInInputValue"]
    hs.generateEmptyStates();
    emptyStates = hs.getStates()
    names = [s.getName() for s in emptyStates]
    assert list(set(stateNames)) == list(set(names))
    s = next((x for x in emptyStates if x.getName() == "XSSVulnerable"), None)
    assert s.isFinalState() == True

def test_fillStates():
    hs = CSVHackingState("testdata", "detection", "xss")
    hs.generateEmptyStates()
    hs.fillEmptyStates()

def test_hackingGoal():
    pass
    # testModelManager = CSVModelManager("testdata")
    # hg = testModelManager.generateHackingGoal("detection", "xss")
    # print hg

# def test_observations():
#     observations = ["IsStringReflected", "IsStringReflectedButEncoded", "IsStringNotReflected", "IsStringReflectedInHTML", "IsStringReflectedInHREF", "IsStringReflectedInCode", "IsTagBracketNotEncoded", "IsTagBracketAlwaysBracket",  "NoErrorsInJS", "ErrorsInJS", "NotRelevant"]

#     csvModel = CSVModelInput("test.csv", ",", observationFile="test_observations.csv")
#     retObs =  csvModel.getObservations()
#     retObservations = []
#     for i in retObs:
#         retObservations.append(i.getName())
#     assert sorted(retObservations) == sorted(list(set(observations)))

# def test_rowsByCol():
#     csvModel = CSVModelInput("test.csv", observationFile="test_observations.csv")
#     rows = csvModel.getRowsByColumn("action", "DetectReflectionType")
#     r1 = ["TestReflectionType", "Pentest is checking the type of reflection", "DetectReflectionType", "IsStringReflectedInHTML", "TestXSSInHTML", "NO"]
#     r2 = ["TestReflectionType", "Pentest is checking the type of reflection", "DetectReflectionType", "IsStringReflectedInHREF", "TestHrefXSS", "NO"]
#     r3 = ["TestReflectionType", "Pentest is checking the type of reflection", "DetectReflectionType", "IsStringReflectedInCode", "TestXSSInCode", "NO"]
#     theRows = [",".join(r1), ",".join(r2), ",".join(r3)]
#     strRows = [str(i) for i in rows]
#     assert strRows == theRows

# def test_columns():
#     actionTest = ["SendGenericTestString", "CheckAllPagesForGenericString", "CheckAllPagesForGenericString", "DetectReflectionType", "DetectReflectionType", "DetectReflectionType", "EncodingTagBracketTest", "EncodingTagBracketTest", "SendDetectionStringHTML", "SendDetectionStringHTML", "SendDetectionStringHref", "SendDetectionStringHref", "SendDetectionStringCodeInJSwithNoErrors", "SendDetectionStringCodeInJSwithNoErrors"]
#     csvModel = CSVModelInput("test.csv", observationFile="test_observations.csv", actionFile="test_actions.csv")
#     actions = csvModel.getColumns("action")
#     assert sorted(list(set(actions))) == sorted(list(set(actionTest)))

# def test_actions():
#     csvModel = CSVModelInput("test.csv", observationFile="test_observations.csv", actionFile="test_actions.csv")
#     actionTest = ["SendGenericTestString", "CheckAllPagesForGenericString", "CheckAllPagesForGenericString", "DetectReflectionType", "DetectReflectionType", "DetectReflectionType", "EncodingTagBracketTest", "EncodingTagBracketTest", "SendDetectionStringHTML", "SendDetectionStringHTML", "SendDetectionStringHref", "SendDetectionStringHref", "SendDetectionStringCodeInJSwithNoErrors", "SendDetectionStringCodeInJSwithNoErrors"]
#     actionObjects = csvModel.generateActions()
#     actionNames = []
#     for o in actionObjects:
#         actionNames.append(o.getName())
#     assert sorted(list(set(actionTest))) == sorted(list(set(actionNames)))

# def test_observations():
#     csvModel = CSVModelInput("test.csv", observationFile="test_observations.csv", actionFile="test_actions.csv")
#     observationTest = ["NotRelevant", "IsStringReflected", "IsStringNotReflected", "IsStringReflectedInHTML", "IsStringReflectedInHREF", "IsStringReflectedInCode", "IsTagBracketNotEncoded", "IsTagBracketAlwaysBracket", "IsStringReflected", "IsStringNotReflected", "IsStringReflected", "IsStringNotReflected", "NoErrorsInJS", "ErrorsInJS"]
#     obs = csvModel.generateObservations()
#     observationNames = []
#     for o in obs:
#         observationNames.append(o.getName())
#     assert sorted(list(set(observationTest))) == sorted(list(set(observationNames)))
# def test_finalstates():
#     csvModel = CSVModelInput("test.csv", observationFile="test_observations.csv", actionFile="test_actions.csv")
#     testFinalStates = [HackingState("XSSVulnerable","",True), HackingState("NoXSS","",True)]
#     finalStates = csvModel.getFinalStates()
#     assert len(testFinalStates) == len(finalStates)
#     for i in testFinalStates:
#         assert i in finalStates
# def test_emptystates():
#     csvModel = CSVModelInput("test.csv", observationFile="test_observations.csv", actionFile="test_actions.csv")
#     csvModel.generateEmptyStates()
#     emptyStates = csvModel.getStateObjects()
#     testStates = ["SendReflectionString", "CheckReflectionString", "TestReflectionType", "TestXSSInHTML", "TestXSSAttackNoTag", "TestHrefXSS", "TestXSSInCode", "XSSVulnerable", "NoXSS"]
#     nameStates = [e.getName() for e in emptyStates]
#     assert sorted(nameStates) == sorted(testStates)

# def test_fillstates():
#     csvModel = CSVModelInput("test.csv", observationFile="test_observations.csv", actionFile="test_actions.csv")
#     csvModel.generateEmptyStates();
#     csvModel.fillEmptyStates();
#     # for s in csvModel.states:
#     #     print s
#     #     print "\n\n====\n\n"

def test__getcategories():
    testModelManager = CSVModelManager("testdata")
    cats = testModelManager.getCategories()
    assert cats == ["detection", "enumeration"]

