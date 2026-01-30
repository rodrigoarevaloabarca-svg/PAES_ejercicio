from Validaciones import Validaciones
class Postulante:
    def __init__(self,nombre, rut,):
        self.nombre = nombre
        self.rut = rut
        self.__matematica = 0
        self.__lenguaje = 0
        self.__ciencias = 0
        self.__historia = 0
        self.__nem = 0
        self.__ranking = 0
#Setters Puntajes
    def set_puntajes_mate(self,matematica):
        if Validaciones.validar_puntaje(matematica):
            self.__matematica = matematica
        else:
            print("El puntaje debe estar entre 100 y 1000")
    def set_puntajes_leng(self,lenguaje):
        if Validaciones.validar_puntaje(lenguaje):
            self.__lenguaje = lenguaje
        else:
            print("El puntaje debe estar entre 100 y 1000")
    def set_puntajes_cien(self,ciencias):
        if Validaciones.validar_puntaje(ciencias):
            self.__ciencias = ciencias
        else:
            print("El puntaje debe estar entre 100 y 1000")
    def set_puntajes_hist(self,historia):
        if Validaciones.validar_puntaje(historia):
            self.__historia = historia
        else:
            print("El puntaje debe estar entre 100 y 1000")
    def set_puntajes_nem(self,nem):
        if Validaciones.validar_puntaje(nem):
            self.__nem = nem
        else:
            print("El puntaje debe estar entre 100 y 1000")
    def set_ranking(self,ranking):
        if Validaciones.validar_puntaje(ranking):
            self.__ranking = ranking
        else:
            print("El puntaje debe estar entre 100 y 1000")
    #getters
    def promedio_paes(self):
        return round((self.__matematica + self.__lenguaje + self.__ciencias + self.__historia )/4)

    def promedio_nem(self):
        return self.__nem

    def promedio_ranking(self):
        return self.__ranking

    def __str__(self):
        return f"Nombre :{self.nombre} | Rut :{self.rut} | Promedio Paes : {self.promedio_paes()} | NEM: {self.promedio_nem()} | Ranking: {self.promedio_ranking()}"
