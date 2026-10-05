class Auto:
    kerekek = 4
    def __init__(self, marka, tipus = "Nincs"):
        self.marka = marka
        self.tipus = tipus

class Teglalap:
    szog = None
    def __init__(self, aoldal = 5, boldal = 10):
        self.aoldal = aoldal
        self.boldal = boldal

    def terulet(self):
        return self.aoldal * self.boldal

    def kerület(self):
        return self.aoldal * 2 + self.boldal

class Dolgozo:
    ceg = "Minta Kft."
    def __init__(self, nev, kor, email, jelszo=""):
        self.nev = nev
        self.kor = kor
        self.email = email
        self.jelszo = jelszo
        self.korkerdes()

    def korkerdes(self):
        kor = input(f"Hány éves vagy {self.nev}:")
        self.kor = kor
        hiba = True
        for i in range(len(kor)):
            if kor[i].isnumeric():
                hiba = False
                break
        if hiba:
            print("Nem számjegyeket adtál meg!")
            self.kor = 0
        else:
            self.kor = kor
        return

# -----------------------------------------------
d = Dolgozo("Józsi", 34, "jozsi@g.hu")
print(d.kor)

t = Teglalap()
print(t.aoldal, t.boldal)
print(t.terulet())
print(t.kerület())
print(t.szog)

a1 = Auto("Peugeot", "Partner")
a2 = Auto("Chery", "Tiggo")

# a1.kerekek = 3

print(a1.kerekek, a2.kerekek, Auto.kerekek)
print(a1.marka, a1.tipus)
print(a2.marka, a2.tipus)