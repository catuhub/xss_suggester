from cmd import Cmd
from CSVModel import CSVModelInput
from CSVModel import CSVModelManager

manager = CSVModelManager("testdata")
noRelevantObservation = "NotRelevant"

def getBanner():
    banner = """
     \ \        / /        | |  / ____|                           | |
      \ \  /\  / /_ _ _ __ | |_| (___  _   _  __ _  __ _  ___  ___| |_ ___ _ __
       \ \/  \/ / _` | '_ \| __|\___ \| | | |/ _` |/ _` |/ _ \/ __| __/ _ \ '__|
        \  /\  / (_| | |_) | |_ ____) | |_| | (_| | (_| |  __/\__ \ ||  __/ |
         \/  \/ \__,_| .__/ \__|_____/ \__,_|\__, |\__, |\___||___/\__\___|_|
                     | |                      __/ | __/ |
                     |_|                     |___/ |___/
    """
    return banner


def printSuggestion(action):
    print "Suggestion:"
    print action.getDescription()

def printObservations(observations):
    toPrint =  "What have you observed?\n"
    toPrint = toPrint + getList([o.getDescription() for o in observations])
    observationNumber = input(toPrint)
    return observationNumber

def printList(theList):
    values = 1
    for c in theList:
        print "%s) %s" % (str(values), c)
        values = values + 1

def getList(theList):
    values = 1
    strRet = ""
    for c in theList:
        strRet = strRet + "%s) %s\n" % (str(values), c)
        values = values + 1
    return strRet

def noRelevant(observations):
    print len(observations)
    return len(observations) == 1 and observations[0].getName() == noRelevantObservation


class MyPrompt(Cmd):
    selectedCategory = ""
    selectedGoal = ""
    currentHackingGoal = None
    prompt = 'wapt> '
    intro =  getBanner()
    def do_categories(self, inp):
        categories = manager.getCategories()
        '''List all the categories '''
        print "Here categories:"
        values = 1
        printList(categories)
    def help_categories(self):
        print "See all categories"

    def do_cat(self, inp):
        if inp == "":
            print "Pls select a category"
            return
        cName = inp
        if cName not in manager.getCategories():
            print "%s not present in categories" % cName
            return
        MyPrompt.selectedCategory = cName
        print "Category Set!"
    def do_goals(self, inp):
        if MyPrompt.selectedCategory == "":
            print "Pls select a category first!"
            return
        goals = manager.getGoalsByCategory(MyPrompt.selectedCategory)
        printList(goals)
    def do_goal(self, inp):
        # Cannot select a goal if you have not selected a category
        if inp == "":
            print "Pls select a hacking goal!"
            return
        if MyPrompt.selectedCategory == "":
            print "Pls select a category first!"
            return
        MyPrompt.selectedGoal = inp
        print "Goal Set!"
        print "Hacking Goal loaded"
        MyPrompt.currentHackingGoal = manager.getHackingGoal(MyPrompt.selectedCategory, MyPrompt.selectedGoal)
    def do_run(self, inp):
        continueVar = True
        if MyPrompt.selectedCategory == "":
            print "Pls select a category first!"
            return
        if MyPrompt.selectedGoal  == "":
            print "Pls select a hacking goal!"
            return

        while continueVar:
            sugg = MyPrompt.currentHackingGoal.suggestAction()
            # Get the current state
            currentState = MyPrompt.currentHackingGoal.getState()
            if currentState.isFinalState() :
                print "END:\n"
                print currentState.getName()
                continueVar = False
                MyPrompt.selectedCategory = ""
                MyPrompt.selectedGoal  = ""
                return
            printSuggestion(sugg)
            observations = MyPrompt.currentHackingGoal.displayCurrentObservations()
            # If no relevant skip the current state and go to next state
            if noRelevant(observations):
                MyPrompt.currentHackingGoal.acquireObservation(observations[0])
            else:
                observationNumber = printObservations(observations)
                obs = observations[observationNumber-1]
                MyPrompt.currentHackingGoal.acquireObservation(obs)


    def do_exit(self, inp):
        '''exit the application.'''
        print("Bye")
        return True
MyPrompt().cmdloop()
