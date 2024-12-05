def menu_principal() -> str:
    """Muestra el menú principal en un print. Cada número indica una opción.
    
    Argumentos:

    Devuelve:
        opcion (str): la opción / acción que el usuario quiere realizar.
    
    """
    
    opcion = input("\nMenú\n1. Cargar notas\n2. Mostrar votos\n3. Ordenar votos por promedio\n4. Peores 3\n5. Mayores promedio\n6. Jurado malo\n7. Sumatoria\n8. Definir ganador\n9. Salir\nElija una opción: ")

    return opcion

def validar_votos(mensaje, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int:
    """Valida que el dato ingresado sea un entero (int).
    
    Argumentos:
        mensaje (any): mensaje que se le muestra al usuario mediante input.
        mensaaje_error (str): mensaje que se le muestra al usuario al ingresar un dato incorrecto.
        minimo (int): minimo valor posible a ingresar.
        maximo (int): maximo valor posible a ingresar.
        reintentos (int): cantidad maxima de intentos que tiene el usuario tras equivocarse.
    
    Devuelve:
        numero (int): el dato de tipo entero que fue validado correctamente.
    """    
    
    intentos = 0

    while True:
        dato = input(mensaje)

        if not dato.isdigit():
            print(mensaje_error)
        else:
            numero = int(dato)
            if minimo <= numero <= maximo:
                return numero
            else:
                print(mensaje_error)
        
        intentos += 1
        if intentos == reintentos:
            break
    
    print("Se superaron los intentos permitidos.")

def inicializar_matriz(cantidad_filas: int, cantidad_columnas: int, valor_inicial: any) -> list[int]:
    """Función para el usuario, crea e inicializa una matriz con un valor inicial.
    
    Argumentos:
        cantidad_filas (int): cantidad de filas de la matriz.
        cantidad_columnas (int): cantidad de columnas de la matriz.
        valor_inicial (any): preferiblemente 0, es el valor inicial que se le da a cada celda de la matriz.

    Devuelve:
        matriz (list): la matriz creada.
    """   
    
    matriz = []
    
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        fila[0] = i + 1
        matriz += [fila]
    return matriz

def mostrar_matriz(matriz: list[int]) -> None:
    """Muestra por consola la matriz con formato.

    Argumentos:
        matriz (list): recibe la matriz ya creada.
    
    Devuelve:
        no devuelve nada, pero muestra la matriz.
    
    """
    
    print("Participante | Votos J1 | Votos J2 | Votos J3 | Promedio")
    print("-" * 57)
    
    for fila in matriz:
        print(f"{fila[0]:<12} | {fila[1]:<8} | {fila[2]:<8} | {fila[3]:<8} | {fila[4]:<8}")

def cargar_notas(matriz: list[int]) -> list[int]:
    """Función para que el usuario cargue notas a la matriz.

    Argumentos:
        matriz (list): recibe la matriz creada con sus valores iniciales.
    
    Devuelve:
        matriz (list): devuelve la matriz con los valores ya cargados.
    
    """
    
    for i in range(len(matriz)):
        print(f"\nParticipante {matriz[i][0]:}")
        
        for j in range(1, len(matriz)-1):
            nota = validar_votos(
                mensaje = f"Ingrese la nota del jurado {j} (entre 1 y 100): ",
                mensaje_error = "Nota inválida. Debe ser un número entre 1 y 100.",
                minimo = 1,
                maximo = 100,
                reintentos = 3
            )
            matriz[i][j] = nota
    
    calcular_promedio_por_participante(matriz)

    return matriz

def ordenar_por_promedio(matriz: list[int]) -> list[int]:
    """Ordena la matriz según el promedio de los participantes y el orden asignado.

    Argumentos:
        matriz (list): recibe la matriz sin ordenar.
    
    Devuelve:
        matriz (list): devuelve la matriz ordenada.
    """

    criterio = input("¿Desea ordenar de manera ascendente o descendente? (A / D): ").strip().lower()

    while criterio not in ["a", "d"]:
        criterio = input("Error. Vuelva a intentar.")

    if criterio == "a":
        ascendente = True
    else:
        ascendente = False

    n = len(matriz)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if ascendente:
                if matriz[j][-1] > matriz[j+1][-1]:
                    aux = matriz[j]
                    matriz[j] = matriz[j+1]
                    matriz[j+1] = aux
            else:
                if matriz[j][-1] < matriz[j+1][-1]:
                    aux = matriz[j]
                    matriz[j] = matriz[j+1]
                    matriz[j+1] = aux
    
    return matriz

def calcular_promedio_por_participante(matriz: list[int]) -> None:
    """Función para calcular el promedio por participante.
    
    Argumentos:
        matriz (list): recibe la matriz con los datos cargados.

    Devuelve:
        No devuelve nada pero actualiza la matriz con los promedios. 
    """
    for i in range(len(matriz)):
        suma_notas = 0
        for j in range(1, len(matriz) - 1):
            suma_notas += matriz[i][j]
        promedio = suma_notas // 3
        matriz[i][-1] = promedio

def mostrar_peores_3(matriz: list[int]) -> None:
    """Encuentra los peores 3 promedios y los muestra.

    Argumentos:
        matriz (list): recibe la matriz con las notas y promedios.

    Devuelve:
        No devuelve nada, pero muestra los 3 participantes con los promedios más bajos. 
    """
    matriz_ordenada = ordenar_por_promedio(matriz)

    print("Los 3 participantes con los promedios más bajos son:")

    for i in range(3):
        participante = matriz_ordenada[i]
        print(f"Participante {participante[0]}: Promedio {participante[-1]}")

def calcular_promedio_total(matriz: list[int]) -> float:
    """Calcula la nota promedio total.

    Argumentos:
        matriz (list): la matriz con los datos de los participantes.

    Devuelve:
        promedio_total (float): el promedio total final.
    """

    suma_total = 0
    for fila in matriz:
        for nota in fila[1:-1]:
            suma_total += nota
    
    promedio_total = suma_total // (len(matriz) * 3)

    return promedio_total

def mostrar_mayores_promedios(matriz: list[int], promedio_total: float) -> None:
    """Muestra los participantes cuyo promedio esta por encima del promedio total.

    Argumentos:
        matriz (list): la matriz con las notas de los participantes.
        promedio_total (float): el promedio total de notas.
    
    Devuelve:
        No devuelve nada, pero muestra los participantes con promedio superior al total.
    """
    
    print(f"El promedio total de notas es: {promedio_total}")
    print("Los participantes con promedios superiores al total son:")

    for fila in matriz:
        if fila[-1] > promedio_total:
            print(f"Participante {fila[0]}: Promedio {fila[-1]}")

def calcular_promedio_por_jurado(matriz: list[int]) -> list[float]:
    """Calcula el promedio de notas por jurado.

    Argumentos:
        matriz (list): la matriz con los datos de los participantes.
    
    Devuelve:
        promedios_jurados (list): una lista con los promedios de cada jurado.
    """

    suma_j1 = 0
    suma_j2 = 0
    suma_j3 = 0

    for fila in matriz:
        suma_j1 += fila[1]
        suma_j2 += fila[2]
        suma_j3 += fila[3]
    
    promedio_j1 = suma_j1 // len(matriz)
    promedio_j2 = suma_j2 // len(matriz)
    promedio_j3 = suma_j3 // len(matriz)
    
    promedios_jurados = [promedio_j1, promedio_j2, promedio_j3]

    return promedios_jurados

def jurado_malo(matriz: list[int]) -> None:
    """Muestra el/los jurados que en promedio pusieron las peores notas.

    Argumentos:
        matriz (list): la matriz con los datos de los participantes.

    Devuelve:
        No devuelve nada, pero muestra el/los jurados que pusieron las peores notas.
    """

    promedios_jurados = calcular_promedio_por_jurado(matriz)

    peor_promedio = promedios_jurados[0]
    peor_jurado = 1

    if promedios_jurados[1] < peor_promedio:
        peor_promedio = promedios_jurados[1]
        peor_jurado = 2
    
    if promedios_jurados[2] < peor_promedio:
        peor_promedio = promedios_jurados[2]
        peor_jurado = 3

    print("El/Los jurado(s) que en promedio puso(ieron) las peores notas es(son):")
    
    if peor_jurado == 1:
        print("Jurado 1")
    elif peor_jurado == 2:
        print("Jurado 2")
    elif peor_jurado == 3:
        print("Jurado 3")
    else:
        print("Todos los jurados")

def mostrar_participantes_sumatoria(matriz: list[int]) -> None:
    """Muestra los participantes cuya suma de notas es igual al número ingresado por el usuario.

    Argumentos:
        matriz (list): la matriz con los datos de los participantes.

    Devuelve:
        No devuelve nada, pero muestra los participantes que cumplen la condición.
    """
    numero = validar_votos(
        mensaje="Ingrese un número entre 3 y 300: ",
        mensaje_error="Número inválido. Debe estar entre 3 y 300.",
        minimo=3,
        maximo=300,
        reintentos=3
    )

    participantes_encontrados = []
    for fila in matriz:
        suma_notas = fila[1] + fila[2] + fila[3]
        if suma_notas == numero:
            participantes_encontrados.append(fila[0])
    
    if participantes_encontrados:
        print(f"Los participantes con suma de notas igual a {numero} son:")
        for participante in participantes_encontrados:
            print(f"Participante {participante}")
    else:
        print(f"No hay participantes con suma de notas igual a {numero}")

def definir_ganador(matriz: list[int]) -> None:
    """Define al ganador y en caso de que haya más de uno, realiza el desempate.

    Argumentos:
        matriz (list): la matriz con los datos de los participantes.
    
    Devuelve:
        No devuelve nada, pero imprime al ganador o ganadores.
    """

    matriz_ordenada = ordenar_por_promedio(matriz)

    mejor_promedio = matriz_ordenada[0][-1]

    mejores_participantes = []
    for fila in matriz_ordenada:
        if fila[-1] == mejor_promedio:
            mejores_participantes.append(fila)
        else:
            break
    
    if len(mejores_participantes) == 1:
        print(f"El ganador de la competencia es el participante {mejores_participantes[0][0]}")
        return

    print("Hay un empate entre los participantes:")
    for fila in mejores_participantes:
        print(f"Participante {fila[0]}: Promedio {fila[-1]}")
    
    print("Realizando desempate...")

    votos_jurados = [0] * len(mejores_participantes)
    for i in range(1, 4):
        print(f"Jurado {i}, elija el ganador:")
        voto = validar_votos(
            mensaje=f"Ingrese el número del participante (entre 1 y {len(mejores_participantes)}): ",
            mensaje_error="Número de participante inválido.",
            minimo=1,
            maximo=len(mejores_participantes),
            reintentos=3
        )
        votos_jurados[voto - 1] += 1

    ganador_indice = 0
    mayor_votos = votos_jurados[0]
    for i in range(1, len(votos_jurados)):
        if votos_jurados[i] > mayor_votos:
            ganador_indice = i
            mayor_votos = votos_jurados[i]

    ganador = mejores_participantes[ganador_indice]
    print(f"El ganador de la competencia es el Participante {ganador[0]} con un promedio de {ganador[-1]}")

# matriz = inicializar_matriz(5, 5, 0)
# cargar_notas(matriz)
# mostrar_matriz(matriz)
# definir_ganador(matriz)