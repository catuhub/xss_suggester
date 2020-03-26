# -*- coding: utf-8 -*-
import base64

class Observation:
    ID_DELIM = "|||"
    """An observation from environment"""
    def __dictReorder(self, item):
        return {k: sort_dict(v) if isinstance(v, dict) else v for k, v in sorted(item.items())}

    def __init__(self, obsElements, idRow):
        self.__obsElements = self.__dictReorder(obsElements)
        self.__idRow = idRow
        self.id = base64.b64encode(Observation.ID_DELIM.join(str(x.getName().strip()) for x in self.__obsElements.values()))

    def getSubObservations(self):
        """Returns the observations grouped by category and ordered
        :returns: the list of sub observations
        """
        return self.__obsElements.iteritems()

    def __str__(self):
        """return string rapresentation"""
        retStr = ""
        for i in self.getSubObservations():
            retStr = retStr +  str(i) + "\n"
        return retStr

    def getID(self):
        """
        :returns: an id composed by the combination of all the categories
        """
        # Get ordered keys
        return self.id

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Observation):
            return self.getID() == other.getID()
        return False

    def __ne__(self, other):
        """Overrides the default implementation (unnecessary in Python 3)"""
        return not self.__eq__(other)
