class OpcionesSistema():
    ListaOpciones = []
    def __init__(self, codigo, nombre):
          self.CodOpcSys = codigo
          self.NomOpcSys = nombre
          self.ListOpercSys = []

    def GuadarOpercSys(self, dato):
        self.ListOpercSys.append(dato)