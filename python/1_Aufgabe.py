class Auto:
    def __init__(self, marke="Unbekannt", modell="Unbekannt", baujahr=2000, kilometerstand=0):
        self._marke = marke
        self._modell = modell
        self.set_baujahr(baujahr)
        self.set_kilometerstand(kilometerstand)

    def set_baujahr(self, baujahr):
        if isinstance(baujahr, int) and 1886 <= baujahr <= 2025:
            self._baujahr = baujahr
        else:
            raise ValueError("Baujahr muss zwischen 1886 und 2025 liegen.")

    def set_kilometerstand(self, kilometerstand):
        if isinstance(kilometerstand, (int, float)) and kilometerstand >= 0:
            self._kilometerstand = kilometerstand
        else:
            raise ValueError("Kilometerstand muss eine nicht-negative Zahl sein.")

    def __str__(self):
        return f"{self._marke} {self._modell} ({self._baujahr}) - {self._kilometerstand} km"
    


auto1 = Auto()
print(auto1)

auto2 = Auto("Tesla", "Model 3", 2022, 15000)
print(auto2)

auto2.set_kilometerstand(20000)
print(auto2)

try:
    auto2.set_kilometerstand(-100)
except ValueError as e:
    print("Fehler:", e)

try:
    auto2.set_baujahr(1700)
except ValueError as e:
    print("Fehler:", e)