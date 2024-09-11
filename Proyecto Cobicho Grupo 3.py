# TP Programación I
# Integrantes: Gonzalo Lopez Batista, Lucio Claa, Agustin Mollo, Agustina Galante, Jessica Ijelman Lipoevtzky

import random
import funciones 




# Declaracion del main
def main():
    listaProvincias, listaHabitantes, infectados = funciones.inicializarListas()
    matriz = funciones.inicializarMatriz(listaHabitantes,infectados)
    login = funciones.llamarLogin()
    
    if login == 1:
        #RONDA 1
        matriz,presupuesto = funciones.inicioDelJuego(listaProvincias,listaHabitantes,matriz)
        #RONDA 2
        matriz,presupuesto = funciones.parteUnoJuego(listaProvincias,listaHabitantes,matriz,presupuesto)
        #RONDA 3
        matriz,presupuesto = funciones.parteDosJuego(listaProvincias,listaHabitantes,matriz,presupuesto)
        #RONDA 4
        matriz,presupuesto = funciones.parteTresJuego(listaProvincias,listaHabitantes,matriz,presupuesto)
        #RONDA 5
        matriz,presupuesto,gano = funciones.parteCuatroJuego(listaProvincias,listaHabitantes,matriz,presupuesto)
        
        funciones.finJuego(listaHabitantes,matriz,gano)
        
        print("\n------------------------------------------------------------")
        print("\t\t\tINFORMES FINALES")
        print("------------------------------------------------------------ \n")
        print(" --> Informe porcentaje de mayor cantidad de infectados por Provincia: \n")
        funciones.porcentajeMayorInfectadosPorProvincia(matriz, listaProvincias)
        print(" --> Informe de mayor porcentaje de cantidad de muertos por Provincia: \n")
        funciones.porcentajeMayorMuertosporProvincia(listaProvincias,listaHabitantes,matriz)
        print(" --> Informe de porcentaje de muertes en todo el pais:\n")
        funciones.porcentajeMuertosTotal(listaHabitantes, matriz)    
    

main()
