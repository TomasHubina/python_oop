class Zviera:

  def __init__(self, m, v):
    # self.__meno = None
    # self.__vek = None
    self.set_meno(m)
    self.set_vek(v)

  def get_meno(self):
    return self.__meno

  def get_vek(self):
    return self.__vek

  def set_meno(self, m):
    if m == '':
      raise ValueError('Meno nesmie byť prázdne')

    self.__meno = m[0].upper() + m[1:].lower()

  def set_vek(self, v):
    #if not isinstance(v, float)

    if type(v) not in [float, int]:
      raise ValueError('Zadaj číslo!')
    elif v <= 0:
        raise ValueError('Vek musí byť väčší ako nula!')
    self.__vek = v

  def info(self):
    return f"{self.__class__.__name__}: meno='{self.__meno}', vek='{self.__vek}', "

  def __str__(self):
    return self.info()

  def urob_zvuk(self):
        raise NotImplementedError("Tato metoda nie je na tejto urovni implementovana")

z = Zviera('cicamica', 5)
print(z.get_meno(), z.get_vek())
z.set_meno('PARADNICA')
print(z.get_meno(), z.get_vek())
z.set_vek(5.5)
print(z.get_meno(), z.get_vek())
print(z.info())
print(z)
# print(z.urob_zvuk())
print("-----------------------------------")
import random

class Pes(Zviera):
  # neexistuje tu tzv. overloading, nie je možné vytvoriť viac ako jeden konštruktor __init__
  def __init__(self, m, v, p=None):
    # zavolám konšturktor predka
    super().__init__(m, v)
    self.__zvuk = 'Hav hav'
    self.__poslusnot = p if p is not None else random.randrange(10)

  def aport(self):
    h = random.randint(1, 10)
    if self.__poslusnot > h:
      return 'Aportujem.'
    else:
      return 'Nechce sami aportovat.'

  # polymofizmus = prekrývam metódu predka
  def info(self):
    return super().info() + f" poslusnost='{self.__poslusnot}' zvuk='{self.__zvuk}',"

  def urob_zvuk(self):
    return self.__zvuk

  def stekaj(self):
    return self.urob_zvuk()
  
class Macka(Zviera):
  # neexistuje tu tzv. overloading, nie je možné vytvoriť viac ako jeden konštruktor __init__
  def __init__(self, m, v):
    # zavolám konšturktor predka
    super().__init__(m, v)
    self.__zvuk = 'Mnau mnau'
    self.__nezavislost = random.uniform(0.5, 1.0)

  def lov(self):
    h = random.randrange(100)
    sanca = random.random() *  self.__nezavislost
    return 'Lovim.' if sanca > 0.5 else 'Nelovim'

  # polymofizmus = prekrývam metódu predka
  def info(self):
    return super().info() + f"nezavislost='{round(self.__nezavislost, 4)}' zvuk='{self.__zvuk}'"

  def urob_zvuk(self):
    return self.__zvuk

  def mnaukaj(self):
    return self.urob_zvuk()

p = Pes('Punto', 10, 4)
pp = Pes('Orech', 5)
m = Macka('cicamica', 3)
print(p.aport())
print(p.aport())
print(p.aport())
print(m.lov())
print(m.lov())
print(m.lov())
print(p.info())
print(pp)
print(m)
print(p.urob_zvuk())

