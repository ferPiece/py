# parahumanos.py

SUFIJOS = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
           1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

def tamanyo_aproximado(tamanyo, un_kilobyte_es_1024_bytes=True):
    '''
    Convierte un tamaño de fichero en formato legible para personas

    Argumentos/parametros:
    tamanyo --- tamaño de fichero en bytes
    un_kilobyte_es_1024_bytes --- si True (por defecto),
                                  usa multiplos de 1024
                                  si False, esa multiplos de 1000
    retorna : string
    ''' 
    if tamanyo < 0:
        raise ValueError('el numero debe ser no negativo')                             
    
    multiplo = 1024 if un_kilobyte_es_1024_bytes else 1000
    for sufijo in SUFIJOS[multiplo]:
        tamanyo /= multiplo
        if tamanyo < multiplo:
            return '{0:.1f}{1}'.format(tamanyo, sufijo)

    raise ValueError('numero demasiado grande')

if __name__ == '__main__':
    print(tamanyo_aproximado(1000000, False))
    print(tamanyo_aproximado(1000000))