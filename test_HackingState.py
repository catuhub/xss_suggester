# -*- coding: utf-8 -*-
import pytest

from HackingState import HackingState
from Observation import Observation
from Action import Action


#def HackingGoal_testSuggestAction:
#    Observation = new Observation("osservazioneX")
#    gs = HackingGoal()

def test_addobservation():
    gs = HackingState("TestReflectionString", "Il Pentest sta verificando se la stringa è riflessa", False)
    gs.setAction(Action("Invia la richiesta con una testNTT, controlla tutte le pagine per verificare se la stringa è riflessa"))
    observation1 = Observation("La stringa e' riflessa")
    observation2 = Observation("La stringa non e' riflessa")
    newHS = HackingState("TestReflectionType", "Il Pentest sta verificando il tipo di riflessione", False)
    failState = HackingState("NoXSS", "No xss found", False)
    gs.addObservationState(observation1, newHS)
    gs.addObservationState(observation2, failState)
    avObs = gs.availableObservations()
    assert len(avObs) == 2
    assert avObs[0] == observation1
    assert avObs[1] == observation2
