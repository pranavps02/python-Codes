class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def explain(self):
        return f"Employee name : {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname == None or self.lname == None :
            return "Email is Not Set. Pleae set using setter"
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self,string):
        print("Setting Now.....")
        names = string.split("@")[0]
        self.fname=names.split(".")[0]
        self.lname=names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname =None
        self.lname=None

pranav = Employee("Pranavs","Supsandes)")

print(pranav.email)

pranav.email = "Pranav.Supsande@gmail.com"
print(pranav.fname)


del pranav.email
print(pranav.fname)
print(pranav.lname)
print(pranav.email)
