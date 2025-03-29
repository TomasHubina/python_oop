class Zlomok:

  def __init__(self, cit, men):
    self.__citatel = cit
    self.__menovatel = men

  def __str__(self):
    return self.__vypis()

  # čistá funkcia, nemení obsah
  def __vypis(self):
    return f'{self.__citatel}/{self.__menovatel}'

  def get_citatel(self):
    return self.__citatel

  def get_menovatel(self):
    return self.__menovatel

  # modifikátor, mení hodnotu atribútov

  def zmen_menovatel(self, hodnota):
    if hodnota != 0:
      self.__menovatel = hodnota
      return True
    else:
      return False
    
  def zmen_citatel(self, hod):
    self.__citatel = hod
    return True 

  # kopia .. klonovanie
  def kopia(self):
    z = Zlomok(self.__citatel, self.__menovatel)
    return z

  # sucin
  def sucin(self, iny):              # iny berie to čo je uložené v z2!!!
    c = self.__citatel * iny.get_citatel()
    m = self.__menovatel * iny.get_menovatel()
    novy = Zlomok(c, m)
    return novy
    # chýba súčet, podiel a rozdieľ

  # porovnajme dva zlomky, ==
  def __eq__(self, iny):
    if not isinstance(iny, Zlomok):
      return None

    c = self.__citatel == iny.get_citatel()
    m = self.__menovatel == iny.get_menovatel()
    return c and m

  # chýba < (__lt__), > (__gt__), <= (__le__), >= (__ge__), != (__ne__)

  # ak zavolám zlomok * zlomok
  def __mul__(self, iny):
    if isinstance(iny, Zlomok):
        newc = self.__citatel * iny.get_citatel()
        newm = self.__menovatel * iny.get_menovatel()
        novy = Zlomok(newc, newm)
        novy.zakladny_tvar()
        return novy
    elif isinstance(iny, int):
        newc = self.__citatel * iny
        return Zlomok(newc, self.__menovatel)
    else:
      return None

  def __add__(self, iny):
    if isinstance(iny, Zlomok):  # Zlomok + Zlomok
        c = self.__citatel * iny.get_menovatel() + iny.get_citatel() * self.__menovatel
        m = self.__menovatel * iny.get_menovatel()
        return Zlomok(c, m)
    elif isinstance(iny, int):  # Zlomok + celé číslo
        return Zlomok(self.__citatel + iny * self.__menovatel, self.__menovatel)
    else:
        return None
    
  def __sub__(self, iny):
    if isinstance(iny, Zlomok):
        c = self.__citatel * iny.get_menovatel() - iny.get_citatel() * self.__menovatel
        m = self.__menovatel * iny.get_menovatel()
        return Zlomok(c, m)
    elif isinstance(iny, int):
        return Zlomok(self.__citatel - iny * self.__menovatel, self.__menovatel)
    else:
        return None

  def __truediv__(self, iny):
    if isinstance(iny, Zlomok):  # Delenie zlomkom
        return Zlomok(self.__citatel * iny.get_menovatel(), self.__menovatel * iny.get_citatel())
    elif isinstance(iny, int):  # Delenie celým číslom
        return Zlomok(self.__citatel, self.__menovatel * iny)
    else:
        return None
    
  def __floordiv__(self, iny):
    return self.__float__() // float(iny)

  # chýba __add__ __sub__ __div__

  # čo keď ku zlomku +, -, *, / celé číslo?
  # napríklad 3/2 * 5

  # float
  def __float__(self):
     return(round(self.__citatel / self.__menovatel, 2))

  def __NSD(self, a, b):
    while a != b:
      if a > b:
        a -= b
      else:
        b -= a
    return a

  # uprava na zakladny
  def zakladny_tvar(self):
    nsd = self.__NSD(self.__citatel, self.__menovatel)
    self.__citatel //= nsd
    self.__menovatel //= nsd

z = Zlomok(10,13)
print(type(z))

dir(z)

z2 = Zlomok(5, 10)

#print(z.citatel)
#print(z2.menovatel)
#z.menovatel = 0
#print(z.vypis())
z.zmen_citatel(5)
z.zmen_menovatel(9) #toto tam bolo
#print(z.vypis())
#print(z.zmen_menovatel(0)) toto tam bolo
#print(z.vypis())

print("print(z): ", z)
print("print(z2): ", z2)

klon = z.kopia()
print("print(klon) #klon = z.kopia(): ", klon)

sucin = z.sucin(z2)
print("print(sucin) #sucin = z.sucin(z2): ", sucin)

podiel = z / z2
print("print(podiel) #podiel = z / z2: ", podiel)

podiel_celocis = z // z2
print("print(podiel_celocis) #podiel_celocis = z // z2: ", podiel_celocis)

sucet = z + z2
print("print(sucet) #sucet = z + z2: ", sucet)

rozdiel = z - z2
print("print(rozdiel) #rozdiel = z - z2: ", rozdiel)

# porovnanie, prekryjem __eq__
# z == z2

print("print(float(sucin)): ", float(sucin))
print("print(z == klon): ", z == klon)
print("print(z == z2): ", z == z2)

o = z * 3
print("print(o) #o = z * 3: ", o)