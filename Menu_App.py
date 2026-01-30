from Carrera import *
from Postulante import *
from Validaciones import *
lista_postulantes = []
lista_carreras = []

def menu():
    print("*" * 80)
    print("   🎓 --- SIMULADOR PAES 2026 --- 🎓   ")
    print("*" * 80)
    print("  [1] 👤 Crear Postulante")
    print("  [2] 🏛️  Crear Carrera")
    print("  [3] 📝 Simular Postulación")
    print("  [4] 📊 Mostrar Listas")
    print("  [5] 🚪 Salir")
    print("*" * 80)
    return input("👉 Ingrese una opción (1-5): ")

def principal():
    while True:
        opcion = menu()

        match opcion:
            case "1" :
                nombre = input("👉Ingrese nombre del postulante: ")
                while True:
                    rut = input("👉Ingrese rut del postulante (Ejemplo: 12345678-9): ")
                    if Validaciones.validar_rut(rut):
                        break
                    else:
                        print("❌ El rut ingresado no es valido (Ejemplo: 12345678-9)")
                mat = int(input("👉Ingrese puntaje de matematicas: "))
                lenguaje = int(input("👉Ingrese puntaje de lenguaje: "))
                ci = int(input("👉Ingrese puntaje de ciencias: "))
                his = int(input("👉Ingrese puntaje de historia: "))
                nem = int(input("👉Ingrese puntaje de nem: "))
                rank = int(input("👉Ingrese puntaje de ranking: "))
                if (Validaciones.validar_puntaje(mat) and Validaciones.validar_puntaje(lenguaje)
                        and Validaciones.validar_puntaje(ci) and Validaciones.validar_puntaje(his)
                        and Validaciones.validar_puntaje(nem) and Validaciones.validar_puntaje(rank)):
                    nuevo_postulante = Postulante(nombre,rut)
                    nuevo_postulante.set_puntajes_mate(mat)
                    nuevo_postulante.set_puntajes_leng(lenguaje)
                    nuevo_postulante.set_puntajes_cien(ci)
                    nuevo_postulante.set_puntajes_hist(his)
                    nuevo_postulante.set_puntajes_nem(nem)
                    nuevo_postulante.set_ranking(rank)
                    lista_postulantes.append(nuevo_postulante)
                    print(f"👤 Postulante Creado con exito")
                    print(f"{nuevo_postulante}")

                else:
                    print("❌Uno o mas puntajes ingresados no son validos (deben estar entre 100 y 1000)")
                    print(f"Puntajes ingresados: {mat}, {lenguaje}, {ci}, {his}, {nem}, {rank}")
            case "2" :
                nombre_carrera = input("👉Ingrese nombre de la carrera: ")
                codigo = input("👉Ingrese codigo de la carrera : ")
                vacantes = int(input("👉Ingrese cantidad de vacantes: "))
                puntaje_minimo = int(input("👉Ingrese puntaje minimo para aceptar postulante: "))
                carrera = Carrera(nombre_carrera,codigo,puntaje_minimo,vacantes)
                lista_carreras.append(carrera)
                print(f"🏛️Carrera Creada con exito")
                print(f"{carrera}")

            case "3" :
                if not lista_postulantes or not lista_carreras:
                    print("⚠️ Se requiere al menos un postulante y una carrera.")
                else:
                    # 1. Seleccionar Carrera
                    print("\n--- Seleccione Carrera ---")
                    for i, c in enumerate(lista_carreras):
                        print(f"🏛️[{i}] Nombre :{c.nombre_carrera} - Codigo: {c.codigo} - Puntaje Minimo: {c.puntaje_minimo} (Cupos: {c.vacantes - len(c.postulantes_aceptados)})")

                    idx_c = int(input("👉 Seleccione el índice de la carrera: "))
                    carrera_sel = lista_carreras[idx_c]

                    # 2. Seleccionar Postulante
                    print("\n--- Seleccione Postulante ---")
                    for i, p in enumerate(lista_postulantes):
                        print(f"👤[{i}]Nombre: {p.nombre} - RUT: {p.rut} - Promedio: {p.promedio_paes()} - Puntaje NEM: {p.promedio_nem()} - Ranking: {p.promedio_ranking()}")

                    idx_p = int(input("👉 Seleccione el índice del postulante: "))
                    postulante_sel = lista_postulantes[idx_p]

                    # 3. Lógica de postulación
                    puntaje_obtenido = Carrera.calcular_ponderacion(postulante_sel)
                    print(f"\n📊 Puntaje Ponderado: {puntaje_obtenido}")

                    if carrera_sel.aceptar_postulante(postulante_sel):
                        print(
                            f"✅ ¡Felicidades! {postulante_sel.nombre} ha sido aceptado en {carrera_sel.nombre_carrera}.")
                    else:
                        if len(carrera_sel.postulantes_aceptados) >= carrera_sel.vacantes:
                            print("❌ Lo sentimos, no quedan vacantes disponibles.")
                        else:
                            print(f"❌ No alcanza el puntaje mínimo requerido ({carrera_sel.puntaje_minimo}).")
            case "4" :
                if not lista_carreras:
                    print("⚠️ No hay carreras registradas.")
                else:
                    print("\n" + "*" * 50)
                    print("📋 LISTADO DE CARRERAS Y MATRICULADOS")
                    print("*" * 50)

                    for carrera in lista_carreras:
                        print(f"\n🏛️ Carrera: {carrera}")
                        print("*" * 30)
                        if not carrera.postulantes_aceptados:
                            print("   (No hay alumnos matriculados aún)")
                        else:
                            for i, alumno in enumerate(carrera.postulantes_aceptados, 1):
                                print(f"👤   {i}. {alumno}")
                    print("\n" + "=" * 50)
            case "5" :
                break
            case _:
                print("❌opcion no valida")

if __name__ == "__main__":
    principal()