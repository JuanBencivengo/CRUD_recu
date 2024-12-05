from os import system
from funciones import *

system("cls")

def main():
    flag_ingreso = False
       
    while True:
        opcion = menu_principal()
        matriz = inicializar_matriz(5, 5, 0)
        
        match opcion:
            case "1":
                flag_ingreso = True
                matriz_cargada = cargar_notas(matriz)
            case "9":
                print("Saliendo...")
                break
            case "2" | "3" | "4" | "5" | "6" | "7" | "8":
                if flag_ingreso:
                    match opcion:
                        case "2":
                            mostrar_matriz(matriz_cargada)
                        case "3":
                            ordenar_por_promedio(matriz_cargada)
                        case "4":
                            ordenar_por_promedio(matriz_cargada)
                            mostrar_peores_3(matriz_cargada)
                        case "5":
                            promedio_total = calcular_promedio_total(matriz_cargada)
                            mostrar_mayores_promedios(matriz_cargada, promedio_total)
                        case "6":
                            promedios_jurados = calcular_promedio_por_jurado(matriz)
                            jurado_malo(matriz_cargada)
                        case "7":
                            mostrar_participantes_sumatoria(matriz_cargada)
                        case "8":
                            ordenar_por_promedio(matriz_cargada)
                            definir_ganador(matriz_cargada)
                else:
                    print("Debe ingresar participantes al sistema antes de acceder a esta opción.")
            case _:
                print("Opción no válida. Por favor, elija una opción entre 1 y 9.")
        
        system("pause")
        system("cls")

if __name__ == "__main__":
    main()