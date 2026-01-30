class Carrera:
    def __init__(self, nombre_carrera,codigo,puntaje_minimo,vacantes):
        self.nombre_carrera = nombre_carrera
        self.codigo = codigo
        self.puntaje_minimo = puntaje_minimo
        self.vacantes = vacantes
        self.postulantes_aceptados = []
    @staticmethod
    def calcular_ponderacion(postulante):
        ponderacion = (postulante.promedio_paes() * 0.4) + \
                      (postulante.promedio_nem() * 0.3) + \
                      (postulante.promedio_ranking() * 0.3)
        return int(ponderacion)
    def aceptar_postulante(self,postulante):
        if len(self.postulantes_aceptados) < self.vacantes and self.calcular_ponderacion(postulante) >= self.puntaje_minimo:
            self.postulantes_aceptados.append(postulante)
            return True
        return False
    def __str__(self):
        cupos_libres = self.vacantes - len(self.postulantes_aceptados)
        return f"{self.nombre_carrera} | Codigo :{self.codigo} | Puntaje Minimo {self.puntaje_minimo} | Cupos Libres : {cupos_libres}"