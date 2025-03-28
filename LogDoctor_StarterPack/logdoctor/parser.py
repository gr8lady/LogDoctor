# Logic for parsing logs


import re
from logdoctor import utils

def leer_log(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            return f.readlines()
    except Exception as e:
        from logdoctor import runner
        runner.logging.error(f"Error leyendo archivo {filepath}: {e}")
        return []
def buscar_errores_sueltos(log_lines):
    patrones = [
        r'.*\bERROR\b.*',
        r'.*\bException\b.*',
        r'.*\bRefused\b.*',
        r'.*\bTimeout\b.*',
        r'.*\bFailure\b.*',
        r'.*\w+Error:.*',
    ]
    errores_encontrados = []
    for line in log_lines:
        for patron in patrones:
            if re.search(patron, line, re.IGNORECASE):
                errores_encontrados.append(line.strip())
                break
    return errores_encontrados
