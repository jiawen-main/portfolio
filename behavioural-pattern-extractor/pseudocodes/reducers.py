from assets import ArrayBoolean, ListFloat, ListArrayBoolean, ListString

class Reducer:
    """This is an abstract class"""
    def getType(self):
        raise NotImplementedError()
    def reduce(self, list):
        raise NotImplementedError()
    
class FloatReducer(Reducer):
    def __init__(self, function):
        self.function = function
    def getType(self):
        return float
    def reduce(self, listFloat):
        # Assumes that self.function is a reducer 
        # with parameter type ListFloat
        if isinstance(listFloat, ListFloat):
            return self.function(listFloat)

class BooleanArrayReducer(Reducer):
    def __init__(self, function):
        self.function = function
    def getType(self):
        return ArrayBoolean
    def reduce(self, listBooleanArray):
        # Assumes that self.function is a reducer 
        # with parameter type ListArrayBoolean
        if isinstance(listBooleanArray, ListArrayBoolean):
            return self.function(listBooleanArray)
    
class StringReducer(Reducer):
    def __init__(self, function):
        self.function = function
    def getType(self):
        return str
    def reduce(self, listString):
        # Assumes that self.function is a reducer 
        # with parameter type ListString
        if isinstance(listString, ListString):
            return self.function(listString)