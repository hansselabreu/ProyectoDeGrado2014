import math
from decimal import Decimal
from calculos_proyecto import varianza, factor_z, sumatoria_varianzas
CAMPOS = ("EP", "EO", "varianza")
actividades = {"A" : {CAMPOS[0]:13, CAMPOS[1]: 5, CAMPOS[2]: 0},
               "C" : {CAMPOS[0]:8, CAMPOS[1]: 2, CAMPOS[2]: 0},
               "D" : {CAMPOS[0]:15, CAMPOS[1]: 5, CAMPOS[2]: 0},
               "E" : {CAMPOS[0]:7, CAMPOS[1]: 3, CAMPOS[2]: 0},
               "F" : {CAMPOS[0]:3, CAMPOS[1]: 1, CAMPOS[2]: 0},
               "G" : {CAMPOS[0]:3, CAMPOS[1]: 1, CAMPOS[2]: 0},
               "H" : {CAMPOS[0]:15, CAMPOS[1]: 7, CAMPOS[2]: 0},
               "P" : {CAMPOS[0]:31, CAMPOS[1]: 15, CAMPOS[2]: 0},
               "Q" : {CAMPOS[0]:15, CAMPOS[1]: 5, CAMPOS[2]: 0},
               "R" : {CAMPOS[0]:10, CAMPOS[1]: 4, CAMPOS[2]: 0},
               "S" : {CAMPOS[0]:45, CAMPOS[1]: 23, CAMPOS[2]: 0}
               }
##actividades = {"A" : {CAMPOS[0]:4, CAMPOS[1]: 2, CAMPOS[2]: 0},
##               "C" : {CAMPOS[0]:5, CAMPOS[1]: 3, CAMPOS[2]: 0},
##               "D" : {CAMPOS[0]:5, CAMPOS[1]: 3, CAMPOS[2]: 0},
##               "E" : {CAMPOS[0]:3, CAMPOS[1]: 1, CAMPOS[2]: 0},
##               "F" : {CAMPOS[0]:3, CAMPOS[1]: 1, CAMPOS[2]: 0}}


def calcular_varianzas(activs):
    for i in activs:
        result_varianza = varianza(activs[i][CAMPOS[0]],
                                   activs[i][CAMPOS[1]])
        activs[i][CAMPOS[2]] = result_varianza

def imprimir_varianzas(actividades):
    activs = dict(actividades) #para evitar modificacion accidental
    indices = list(activs.keys())
    indices.sort()

    m_factor = 28
    print("*" * m_factor)
    for i in indices:
        print("Actividad: %s Varianza: %.2f " %(i, activs[i][CAMPOS[2]]))
    print("*" * m_factor)
    
def sumar_varianzas(actividades):
    activs = dict(actividades)
    varianzas_extraidas = []
    for i in activs:
        varianzas_extraidas.append(activs[i][CAMPOS[2]])
    return sumatoria_varianzas(varianzas_extraidas)
        
if __name__ == "__main__":
    calcular_varianzas(actividades)
    imprimir_varianzas(actividades)
    sum_varianzas = sumar_varianzas(actividades)
    print("Suma de varianzas: %f" % sum_varianzas)
    z = factor_z(109, 106, sum_varianzas)
    print("Factor Z = %.1f" % z)

