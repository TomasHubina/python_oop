class Auto:
    def __init__(self, objem_nadrze, miest_na_sedenie, stav_tachometra, spotreba, pocet_cestujucich, SPZ):
        if objem_nadrze <= 0:
            raise ValueError("Nesprávne zadaný objem nádrže")
        if not (1 <= miest_na_sedenie <= 8):
            raise ValueError("Nesprávne zadaný počet miest na sedenie")
        if stav_tachometra < 0:
            raise ValueError("Nesprávny stav tachometra")
        if spotreba <= 0:
            raise ValueError("Nesprávne zadaná spotreba")
        if not (0 <= pocet_cestujucich < miest_na_sedenie):
            raise ValueError("Nesprávne zadaný počet cestujúcich")
        if not (len(SPZ) == 7 and SPZ.isalnum() and SPZ.isupper()):
            raise ValueError("Nesprávne zadaná SPZ")
        
        self.objem_nadrze = objem_nadrze
        self.miest_na_sedenie = miest_na_sedenie
        self.stav_tachometra = stav_tachometra
        self.spotreba = spotreba
        self.pocet_cestujucich = pocet_cestujucich
        self.SPZ = SPZ
        self.nadrz = self.objem_nadrze
    
    def getCapacity(self):
        return round(self.nadrz, 2)
    
    def getPassanger(self):
        return self.pocet_cestujucich
    
    def getKm(self):
        return self.stav_tachometra
    
    def Travel(self, km):
        potrebne_palivo = (km / 100) * self.spotreba
        if potrebne_palivo > self.nadrz:
            print("Insufficient amount of fuel !")
        else:
            self.nadrz -= potrebne_palivo
            self.stav_tachometra += km
            print(f"Spotrebované palivo: {potrebne_palivo:.2f} L, stav tachometra: {self.stav_tachometra:.1f} km")
    
    def Board(self, pocet):
        if self.pocet_cestujucich + pocet <= self.miest_na_sedenie:
            self.pocet_cestujucich += pocet
        else:
            print("Nie je miesto")
    
    def GetOff(self, pocet):
        if self.pocet_cestujucich - pocet >= 0:
            self.pocet_cestujucich -= pocet
        else:
            print("V aute už nikto nie je")
a1 = Auto(40, 7, 5001, 7, 1, "NR123BB")

print(a1.getKm())  # output 5001
a1.Board(3)
print(a1.getPassanger())  # output 4
a1.Travel(450)  # output "Spotrebované palivo: 31.5 L, stav tachometra: 5451.0 km"
print("-------------------------")

class NakladneAuto(Auto):
    def __init__(self, objem_nadrze, miest_na_sedenie, stav_tachometra, spotreba, pocet_cestujucich, SPZ, max_cargo):
        super().__init__(objem_nadrze, miest_na_sedenie, stav_tachometra, spotreba, pocet_cestujucich, SPZ)
        if not (0 < miest_na_sedenie <= 2):
            raise ValueError("Nesprávny počet miest na sedenie pre nákladné auto")
        self.miest_na_sedenie = miest_na_sedenie
        if max_cargo <= 0:
            raise ValueError("Nesprávne zadaný maximálny náklad")
        self.max_cargo = max_cargo
        self.cargo = 0
    
    def Board(self, naklad):
        if self.cargo + naklad <= self.max_cargo:
            self.cargo += naklad
        else:
            print("Nedostatok miesta pre náklad")
    
    def Unload(self, naklad):
        if self.cargo - naklad >= 0:
            self.cargo -= naklad
        else:
            print("Nie je už žiadny náklad na vyloženie")
    
    def getCargo(self):
        return self.cargo
    
na1 = NakladneAuto(400, 2, 35221, 25, 1, "NR321YY", 15)
  # objem nadrze = 400, miest na sedenie = 2, stav tachometra = 35221, spotreba = 25, pocet cestujucich = 1, SPZ = NR-321-YY, cargo = 15 <-- je to maximum, ktore dokaze NakladneAuto odniest. 
print(na1.getCapacity())  # output 400
na1.Board(10)
na1.Unload(7.5)
print(na1.getCargo()) # output 2.5
na1.Travel(1250)  # output "Spotrebované palivo: 312.5 L, stav tachometra: 36471.0 km"

na2 = NakladneAuto(450, 2, 24555, 31, 1, "TO478AQ", 50)
print(na2.getKm(), "km") # output 24555.0 km  
na2.Board(50)
na2.Travel(358) # output "Spotrebované palivo: 110.98 L, stav tachometra: 24913.0 km"
na2.Unload(35.5)  
na2.Travel(1000) # output "Spotrebované palivo: 310 L, stav tachometra: 25913.0 km"
print(na2.getCapacity()) # output 29.02 
print("------------------")

class Parkovisko:
    def __init__(self):
        self.auta = []
    
    def addObject(self, auto):
        self.auta.append(auto)
    
    def getMax(self, typ):
        max_auto = None
        max_km = -1
        for auto in self.auta:
            if isinstance(auto, Auto) and typ == "Auto" and not isinstance(auto, NakladneAuto):
                if auto.getKm() > max_km:
                    max_km = auto.getKm()
                    max_auto = auto
            elif isinstance(auto, NakladneAuto) and typ == "NakladneAuto":
                if auto.getKm() > max_km:
                    max_km = auto.getKm()
                    max_auto = auto
        
        if max_auto:
            print(f"{max_auto.SPZ}, {max_auto.getKm():.1f} km")
        else:
            print("Žiadne auto daného typu.")
p = Parkovisko()
p.addObject(a1)
p.addObject(a1)
p.addObject(na1)
p.addObject(na2)
p.getMax("Auto") # output NR123BB, 5451.0 km
p.getMax("NakladneAuto") # output NR321YY, 36471.0 km