class Employee:
    no_of_leaves =8

    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    def printDetails(self):
        return f"The Name is {self.name}. Salary is  {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls,newLeaves):
        cls.no_of_leaves = newLeaves

    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("-"))

    @staticmethod
    def printGood(string):
        print("This is good "+ string)

class Player:
    var =9
    no_of_game = 4
    def __init__(self,name,game):
        self.name= name
        self.game=game

    def printDetails(self):
        return f"The name is {self.name},and he plays {self.game}"

class Programmer(Player,Employee):
   language = "C++"
   def printLanguage(self):
       print(self.language)


pranav4 = Programmer("Pranav",["Cricket","Football"])

print(pranav4.printDetails())