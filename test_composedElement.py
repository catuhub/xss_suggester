# -*- coding: utf-8 -*-
import pytest

from BaseElement import ComposedElement
from BaseElement import BaseElement


def test_addElement():
    ce = ComposedElement()
    be = BaseElement("Test", "TestDesc", "category")
    ce.addElement(be)
    assert be == ce.getElement("Test")
    # gs.addObservationState(observation2, failState)
    # avObs = gs.availableObservations()
    # assert len(avObs) == 2
    # assert avObs[0] == observation1
    # assert avObs[1] == observation2
# def test_noDuplicate():
#     ce = ComposedElement()
#     be = BaseElement("Test", "TestDesc")
#     be2 = BaseElement("Test", "TestDesc")
#     ce.addElement(be)

def test_remove():
    ce = ComposedElement()
    be = BaseElement("Test", "TestDesc", "category")
    ce.addElement(be)

    assert be == ce.getElement("Test")
    ce.removeElement("Test")
    assert (ce.getElement("Test") is None)
def test_category():
    ce = ComposedElement()
    be = BaseElement("Test", "TestDesc", "category")
    be2 = BaseElement("Test2 ", "TestDesc2", "category")
    be3 = BaseElement("Test3", "TestDesc3", "category2")

    ce.addElement(be)
    ce.addElement(be2)
    ce.addElement(be3)

    eg = ce.getElementsByCategory("category")
    assert([be,be2] == eg or [be2, be] == eg)

