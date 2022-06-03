class ElectronicDevices:
    def isElectronicDevice(self):
       return print(f"It is an Electronic Device")


class PocketGadgets(ElectronicDevices):
    def isPocketGadget(self):

       return print(f"It is a Pocket Gadget")


class Phone(PocketGadgets):
    def isPhone(self):
        return print(f"We can call it as Phone")

realme = Phone()

realme.isElectronicDevice()
realme.isElectronicDevice()
realme.isPhone()
