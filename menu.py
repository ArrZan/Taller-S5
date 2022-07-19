import os
from Usuario import Usuario
from Rol import Rol
from OpcionesSys import OpcionesSistema
from OperacionesSys import OperacionesSistema


class Menu:

    def menu(self, Usuario, Rol, Opciones):
        print("-"*43)
        Usuario.mostrarNomUser()
        print("Rol : {}".format(Rol.TipoRol))
        print("Opción: {}".format(Opciones.NomOpcSys))
        print("")
        for i in Opciones.ListOpercSys:
            print("{}.   {}".format(i.CodOpercSys, i.DescrpOpercSys))
        print("-"*43)
    
    def cls(self):
        os.system("cls")


if __name__ == "__main__":
    Rol1 = Rol("Estudiante")
    opc1 = OpcionesSistema(1, "Mis Materias")
    oper1_1 = OperacionesSistema("Ver materias")
    oper1_2 = OperacionesSistema("Ver profesores")
    oper1_3 = OperacionesSistema("Ver Compañeros")
    opc1.GuadarOpercSys(oper1_1)
    opc1.GuadarOpercSys(oper1_2)
    opc1.GuadarOpercSys(oper1_3)

    user1 = Usuario('0941213548','Josué Zambrano','vinilo','jzambranoc9@unemi.edu.ec','0963999834')

    menupr = Menu()
    menupr.cls()
    menupr.menu(user1,Rol1,opc1)
