class Validaciones:
    @staticmethod
    def validar_rut(rut):
        return "-" in rut and 8 <= len(rut) <= 10
    @staticmethod
    def validar_puntaje(puntaje):
        return 100 <= puntaje <= 1000