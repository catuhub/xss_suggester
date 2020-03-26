from BaseElement import BaseElement
from Observation import Observation
from Action import Action

def test_id():
    cat1 = "OBSERVATION_ONE"
    cat2 = "OBSERVATION_TWO"
    cat3 = "OBSERVATION_THREE"
    be2 = BaseElement("secondObservation", "The second observation", cat2)
    be3 = BaseElement("thirdObservation", "The third observation", cat3)
    be = BaseElement("firstObservation", "The first observation", cat1)
    d = {
            cat1: be,
            cat3: be3,
            cat2: be2
    }
    o = Observation(d)
    idObs = o.getID()
    assert idObs == "firstObservation|||secondObservation|||thirdObservation"


def test_idAction():
    cat1 = "ACTION1"
    cat2 = "ACTION2"
    cat3 = "ACTION3"
    be2 = BaseElement("action two", "second action", cat2)
    be3 = BaseElement("action_three", "third action", cat3)
    be = BaseElement("action_one", "first action", cat1)
    d = {
            cat1: be,
            cat3: be3,
            cat2: be2
    }
    o = Action(d, 1)
    idObs = o.getID()
    assert idObs == "action_one|||action_three|||action two"

def test_equalityAction():
    cat1 = "ACTION1"
    cat2 = "ACTION2"
    cat3 = "ACTION3"
    be2 = BaseElement("action two", "second action", cat2)
    be3 = BaseElement("action_three", "third action", cat3)
    be = BaseElement("action_one", "first action", cat1)
    d = {
            cat1: be,
            cat3: be3,
            cat2: be2
    }
    d2 = dict(d)
    d2['v'] = BaseElement.empty("v")
    o = Action(d, 1)
    o2 = Action(d, 2)
    o3 = Action(d2, 2)
    assert o == o2
    assert o != o3

def test_withEmptyElements():
    e1 = BaseElement.empty("TEST")
    cat1 = "OBSERVATION_ONE"
    cat2 = "OBSERVATION_TWO"
    cat3 = "OBSERVATION_THREE"
    be2 = BaseElement("secondObservation", "The second observation", cat2)
    be3 = BaseElement("thirdObservation", "The third observation", cat3)
    be = BaseElement("firstObservation", "The first observation", cat1)

    d = {
            cat1: be,
            cat3: be3,
            cat2: be2,
            "TEST": e1
    }
    o = Observation(d)
    idObs = o.getID()
    assert idObs == "firstObservation||||||secondObservation|||thirdObservation"

def testEqualityObs():
    e1 = BaseElement.empty("TEST")
    cat1 = "OBSERVATION_ONE"
    cat2 = "OBSERVATION_TWO"
    cat3 = "OBSERVATION_THREE"
    be2 = BaseElement("secondObservation", "The second observation", cat2)
    be3 = BaseElement("thirdObservation", "The third observation", cat3)
    be = BaseElement("firstObservation", "The first observation", cat1)

    d = {
            cat1: be,
            cat3: be3,
            cat2: be2,
            "TEST": e1
    }
    o = Observation(d)
    o2 = Observation(d)
    assert o == o2
