class OperacionesSistema():
    _contCod = 0
    def __init__(self, descrp):
          OperacionesSistema._contCod +=1
          self.CodOpercSys = OperacionesSistema._contCod
          self.DescrpOpercSys = descrp
