class Rol():
    contCod = 0
    
    def __init__(self, nombre):
          Rol.contCod += 1
          self.CodRol = Rol.contCod
          self.TipoRol = nombre

    def mostrarNomRol(self):
        print("{}".format(self.NomRol))