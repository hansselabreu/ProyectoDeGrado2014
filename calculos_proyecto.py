import math
def varianza(EP, EO):
    ''' Calcula la varianza de los tiempos de la actividad
        EP = Estimación Pesimista
        EO = Estimación Optimista
        Retorna α^2 (Varianza)
        Ejemplo: >> varianza(4,2)
                 0.11111111111111
    '''
    if(EP < EO):
        raise Exception("EP no puede ser menor que EO")

    return ((EP - EO)/6)**2

def factor_z(TS, TM, suma_de_varianzas):
    ''' Calcula el factor Z de probabilidad de realización
        de un proyecto.
        TS = Tiempo predeterminado cualquiera
        TM = Tiempo mínimo de duración de realización de un evento
        suma_de_varianzas = Sumatoria de la varianza de las
        actividades.
        Retorna Z (factor Z de probabilidad)
        Ejemplo: >> factor_z(16, 15, 0.55)
                 1.348399724926484
    '''
    return (TS - TM)/math.sqrt(suma_de_varianzas)

def sumatoria_varianzas(varianzas):
    return sum(varianzas)

