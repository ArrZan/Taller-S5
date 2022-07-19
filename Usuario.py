class Usuario():
                
    def __init__(self, ced, nom, clav, correo, telf):
          self.CeduUser = ced
          self.NomUser = nom
          self.ClaveUser = clav
          self.CorreoUser = correo
          self.TelfUser = telf

    def mostrarNomUser(self):
        print("Usuario: {}      ID: {}".format(self.NomUser, self.CeduUser))
