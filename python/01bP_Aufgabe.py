class Auto:
    __anzahl_autos = 0        
    __baujahr_max = 2030      
 
    def __init__(self, marke, baujahr):
        if baujahr > Auto.__baujahr_max:
            raise ValueError("Baujahr zu groß!")  
        self.marke = marke
        self.baujahr = baujahr
        Auto.__anzahl_autos += 1
 
    @classmethod
    def get_anzahl(cls):
        return cls.__anzahl_autos
 
    @classmethod
    def get_baujahr_max(cls):
        return cls.__baujahr_max
 
    @classmethod
    def set_baujahr_max(cls, wert):
        cls.__baujahr_max = wert
 
    @classmethod
    def von_string(cls, text):
        teile = text.split(";")         
        marke = teile[0]
        baujahr = int(teile[1])
        return cls(marke, baujahr)  

a1 = Auto("VW", 2010)
a2 = Auto("BMW", 2015)
a3 = Auto.von_string("Tesla;2020")

print("Gesamtanzahl Autos:", Auto.get_anzahl())
print("Max Baujahr erlaubt:", Auto.get_baujahr_max())

Auto.baujahr_max = 2030
print("Neues max Baujahr:", Auto.baujahr_max)

try:
    a4 = Auto("Audi", 2050)
except ValueError as e:
    print("Fehler:", e)    