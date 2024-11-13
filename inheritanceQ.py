# python inheritanceQ.py

# Python Program to Create a Class in which One Method Accepts a String from the 
# User and Another method Prints it. Define a class named Country which has a method 
# called print Nationality. Define subclass named state from Country which has a mehtod 
# called printState. Write a method to print state, country and nationality.
#
class Country:
    def acceptCountry(self, name):
        self.cname = name
    def displayCountry(self):
        return self.cname

class State(Country):
    def Acceptstate(self,state):
        self.sstate = state
    def displaystate(self):
        return self.sstate
    
obj1 = State()
obj1.acceptCountry("India")
obj1.Acceptstate("Maharastra")
country = obj1.displayCountry()
state = obj1.displaystate()

print(f"The country is {country} and state is {state}")