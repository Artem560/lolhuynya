###Übung###

from datetime import date
 
class Auto:
    __anzahl_autos: int = 0
    __baujahr_max: int = 2025
 
    def __init__(self, marke: str, baujahr: int) -> None:
        if baujahr > Auto.__baujahr_max:
            raise ValueError("Baujahr zu groß!")
        self.marke: str = marke
        self.__baujahr: int = baujahr
        Auto.__anzahl_autos += 1
 
    @property
    def baujahr(self) -> int:
        return self.__baujahr
 
    @property
    def alter(self) -> int:
        return date.today().year - self.__baujahr
 
    @classmethod
    def statistik(cls) -> str:
        return f"Es gibt {cls.__anzahl_autos} Autos."
 
    @classmethod
    def get_baujahr_max(cls) -> int:
        return cls.__baujahr_max
 
    @classmethod
    def set_baujahr_max(cls, wert: int) -> None:
        cls.__baujahr_max = wert
 
    baujahr_max: property = property(get_baujahr_max, set_baujahr_max)
 