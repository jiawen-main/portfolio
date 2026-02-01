# Standard data structures

class ArrayBoolean:
    """An array of boolean"""
    def length(self):
        pass
    def __getitem__(self, index):
        # Get value at position index using operator []
        pass

class ListFloat:
    """A homogeneous list of real numbers"""
    pass

class ListArrayBoolean:
    """A homogeneous list of boolean arrays"""
    pass

class ListString:
    """A homogeneous list of strings"""
    pass

# Particular data structures

class Point:
    """A 2D point"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

class AnswerSurvey:
    """An answer of a survey"""
    def getAnswerQuestions():
        pass
    def getIdAnswerSurvey():
        pass

class AnswerNumericalQuestion:
    """An answer of a numerical question (in a survey)"""
    def getAnswerNumber():
        pass

class AnswerMultipleOptionsQuestion:
    """An answer of a numerical question (in a survey)"""
    def getAnswerMultipleOptions():
        pass

class AnswerTextQuestion:
    """An answer of a numerical question (in a survey)"""
    def getAnswerText():
        pass