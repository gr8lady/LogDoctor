
import os
import logging
import csv
from logdoctor import stacktrace

# Configurar logging interno
logging.basicConfig(
    filename='logs/logdoctor.log',
    filemode='a',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

def leer_log(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            return f.readlines()
    except Exception as e:
        logging.error(f"Error leyendo archivo {filepath}: {e}")
        return []

def guardar_csv(resultados, output_file):
    try:
        with open(output_file, 'w', newline='') as csvfile:
            fieldnames = ['tipo_error', 'descripcion', 'causa_raiz']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for r in resultados:
                writer.writerow(r)
        logging.info(f"Exportación a CSV exitosa: {output_file}")
    except Exception as e:
        logging.error(f"Error exportando CSV: {e}")

def run_analysis(logfile, csv_output=None):
    if not os.path.exists(logfile):
        print(f"❌ Archivo no encontrado: {logfile}")
        logging.error(f"Archivo no encontrado: {logfile}")
        return

    print(f"📖 Analizando: {logfile}")
    logging.info(f"Iniciando análisis del archivo: {logfile}")
    lineas = leer_log(logfile)
    bloques = stacktrace.extraer_stacktrace(lineas)

    resultados = []
    for i, bloque in enumerate(bloques, 1):
        causa = stacktrace.analizar_causa_raiz(bloque)
        print(f"🧪 Stack trace #{i}:")
        print(f"   ⚠️ {causa['tipo_error']} → {causa['descripcion']}")
        logging.info(f"Stack trace #{i} detectado: {causa['tipo_error']} → {causa['descripcion']}")
        resultados.append(causa)

    if csv_output:
        guardar_csv(resultados, csv_output)
        print(f"📤 Resultados exportados a: {csv_output}")

    logging.info("Análisis finalizado.")

