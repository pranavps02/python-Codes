class Dad:
    basketball = 5

class Son(Dad):
    dance=1
    def isDance(self):
        return f"Yes I dance {self.dance} no of times"
class Grandson(Son):
   dance = 6

   # def isDance(self):
   #     return f"Jackson Yeah!!!"


pranav1 = Dad()
pranav2 = Son()
pranav3 = Grandson()

print(pranav3.basketball)