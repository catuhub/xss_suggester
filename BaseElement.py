# -*- coding: utf-8 -*-
from cgi import escape

class ComposedElement(object):
    def __init__(self):
        self.baseElements = []

    """Composition of more Base Elements"""
    def addElement(self, baseElement):
        """Add new Elements
        :baseElement:
        """
        self.baseElements.append(baseElement)

    def removeElement(self, name):
        """Remove the element from the array
        :name: the name inside
        """
        theElement = self.getElement(name)
        if theElement in self.baseElements:
            self.baseElements.remove(theElement)
        # name =

    def getElement(self, name):
        """ returns the element by name
        :name: the name of base element
        :returns: the elements
        """
        el = next((x for x in self.baseElements if x.getName() == name), None)
        return el
    def getElements(self):
        """Returns all the elements
        :returns:  elements
        """
        return self.baseElements
    def getElementsByCategory(self, cat):
        """Returns the list of elements taken by category
        :cat: the category
        :returns: the list of elements
        """
        newCE = ComposedElement()
        for x in self.baseElements:
            if x.getCategory() == cat:
                newCE.addElement(x)
        return newCE

    def getCategories(self):
        allCats = [c.getCategory() for c in self.baseElements]
        return list(set(allCats))
    def getLength(self):
        """Returns the length of composed element
        :returns: the length of base elements
        """
        return len(self.baseElements)

class BaseElement():
    @staticmethod
    def empty(category):
        """ Returns an empty element
        :returns: an empty baseElement
        """
        return BaseElement("", "", category)

    """Action to do"""

    def __init__(self, name, description, category):
        self.__name = escape(name)
        self.__description = escape(description)
        self.__category = escape(category)

    def getName(self):
        """returns the name of the action
        :returns: the name of the action

        """
        return self.__name

    def getDescription(self):
        """return the action description
        :returns: description
        """
        return self.__description

    def getCategory(self):
        """
        :returns: category of base element
        """
        return self.__category

    def __str__(self):
        """Get Action string
        :returns: action string
        """
        theName = self.__name if self.__name else ""
        theCategory = self.__category if self.__category else ""
        theDescr = self.__description if self.__description else ""
        return "Name: "+ self.__name + "; Descr: "+ self.__description + "; Cat: " + self.__category
