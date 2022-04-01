# our own error creation

class InvalidAgeError(Exception):
    def __init__(self,age=0):
        self.age = age

    def __str__(self):
        return str(self.age)+ " is an invalid age"