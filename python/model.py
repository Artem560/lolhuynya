from pydantic import BaseModel, Field, field_validator, ValidationError
from datetime import date

class Spieler(BaseModel):
    name: str = Field(..., min_length=2)
    jahrgang: int = Field(..., ge=1900, le=date.today().year)
    staerke: float = Field(..., ge=0, le=100)
    torschuss: float = Field(..., ge=0, le=100)
    motivation: float = Field(...)

    @field_validator('motivation')
    def check_motivation(cls, v):
        if v < 10:
            print("Warnung: Motivation ist sehr niedrig!")
        return v

print("Test: Spieler 1 – gültige Daten")
try:
    s1 = Spieler(
        name="Toni Kroos",
        jahrgang=1990,
        staerke=85.0,
        torschuss=90.0,
        motivation=70.0
    )
    print("Spieler erstellt:", s1.model_dump())
except ValidationError as e:
    print("Fehler bei Spieler 1:\n", e)

print("\n" + "="*60 + "\n")


print("Test: Spieler 2 – Motivation zu hoch")
try:
    s2 = Spieler(
        name="Max",
        jahrgang=1995,
        staerke=70,
        torschuss=80,
        motivation=150
    )
    print("Spieler erstellt:", s2.model_dump())
except ValidationError as e:
    print("Fehler bei Spieler 2:\n", e)

print("\n" + "="*60 + "\n")


print("Test: Spieler 3 – Jahrgang zu alt")
try:
    s3 = Spieler(
        name="Leo",
        jahrgang=1800,
        staerke=88,
        torschuss=85,
        motivation=90
    )
    print("Spieler erstellt:", s3.model_dump())
except ValidationError as e:
    print("Fehler bei Spieler 3:\n", e)

print("\n" + "="*60 + "\n")

print("Test: Spieler 4 – Name zu kurz")
try:
    s4 = Spieler(
        name="A",
        jahrgang=2000,
        staerke=60,
        torschuss=65,
        motivation=80
    )
    print("Spieler erstellt:", s4.model_dump())
except ValidationError as e:
    print("Fehler bei Spieler 4:\n", e)

print("\n" + "="*60 + "\n")
