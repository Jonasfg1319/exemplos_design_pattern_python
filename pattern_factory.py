import sys


class Programador(object):
  def __init__(self):
    print("programador")

class Empresario(object):
  def __init__(self):
    print("empresario")


class Factory(object):
  def __init__(self):
    pass

  def criar(self, classe):
   try:
     return getattr(sys.modules[__name__], classe)()
   except:
     print("Essa classe não existe, verifique se digitou corretamente")



cargo = input("Digite o cargo: ")

factory = Factory()

factory.criar(cargo)



