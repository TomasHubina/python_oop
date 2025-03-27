from os import sep
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

  # chýba <, >, <=, >=, !=

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

sucin = z * z2

print("print(sucin) #sucin = z * z2: ", sucin)

# porovnanie, prekryjem __eq__
# z == z2

print("print(float(sucin)): ", float(sucin))
print("print(z == klon): ", z == klon)
print("print(z == z2): ", z == z2)

o = z * 3
print("print(o) #o = z * 3: ", o)