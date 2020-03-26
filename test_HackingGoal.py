# -*- coding: utf-8 -*-
import pytest

from HackingState import HackingState
from HackingGoal import HackingGoal
from Observation import Observation
from Action import Action


#def HackingGoal_testSuggestAction:
#    Observation = new Observation("osservazioneX")
#    gs = HackingGoal()

def test_displayobservation():
    gs = HackingState("TestReflectionString", "Il Pentest sta verificando se la stringa è riflessa", False)
    gs.setAction("Invia la richiesta con una testNTT, controlla tutte le pagine per verificare se la stringa è riflessa")
    observation1 = Observation("La stringa e' riflessa")
    observation2 = Observation("La stringa non e' riflessa")
    newHS = HackingState("TestReflectionType", "Il Pentest sta verificando il tipo di riflessione", False)
    failState = HackingState("NoXSS", "No xss found", False)
    gs.addObservationState(observation1, newHS)
    gs.addObservationState(observation2, failState)
    hg = HackingGoal("xss", "goal", gs)
    avObs = hg.displayCurrentObservations()
    assert len(avObs) == 2
    assert avObs[0] == observation1
    assert avObs[1] == observation2

def test_updatestate():
    gs = HackingState("TestReflectionString", "Il Pentest sta verificando se la stringa è riflessa", False)
    gs.setAction(Action("NameRequest", "Invia la richiesta con una testNTT, controlla tutte le pagine per verificare se la stringa è riflessa"))
    observation1 = Observation("ReflectionString", "La stringa e' riflessa")
    observation2 = Observation("NotReflectionString" ,"La stringa non e' riflessa")
    newHS = HackingState("TestReflectionType", "Il Pentest sta verificando il tipo di riflessione", False)
    actionToAnalyze = Action("CheckReflectionType", "Analizza la riflessione dove è avvenuta")
    newHS.setAction(actionToAnalyze)
    failState = HackingState("NoXSS", "No xss found", False)
    gs.addObservationState(observation1, newHS)
    gs.addObservationState(observation2, failState)
    hg = HackingGoal("xss", "goal", gs)
    currentObservation = Observation("ReflectionString", "La stringa e' riflessa")
    hg.acquireObservation(currentObservation)
    theActionToDo = hg.suggestAction()
    assert theActionToDo == actionToAnalyze
