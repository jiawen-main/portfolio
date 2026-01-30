from assets import ArrayBoolean

class Metric:
    """This is an abstract class"""
    def getType(self):
        raise NotImplementedError()
    def distance(self, p1, p2):
        raise NotImplementedError()
    
class FloatMetric(Metric):
    def __init__(self, function):
        self.function = function
    def getType(self):
        return float
    def distance(self, float1, float2):
        # Assumes that self.function is a metric
        # with 2 parameters, each with type float
        if (isinstance(float1, float) 
        and isinstance(float2, float)):
            return self.function(float1, float2)
        
class BooleanArrayMetric(Metric):
    def __init__(self, function):
        self.function = function
    def getType(self):
        return ArrayBoolean
    def distance(self, arrayBoolean1, arrayBoolean2):
        # Assumes that self.function is a metric
        # with 2 parameters, each with type ArrayBoolean
        if (isinstance(arrayBoolean1, ArrayBoolean)
        and isinstance(arrayBoolean2, ArrayBoolean)):
            return self.function(arrayBoolean1, arrayBoolean2)
        
class StringMetric(Metric):
    def __init__(self, function):
        self.function = function
    def getType(self):
        return str
    def distance(self, string1, string2):
        # Assumes that self.function is a metric
        # with 2 parameters, each with type string
        if (isinstance(string1, str)
        and isinstance(string2, str)):
            return self.function(string1, string2)