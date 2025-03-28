
import argparse
import os
import logging
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
    import csv
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

def cli():
    parser = argparse.ArgumentParser(description='LogDoctor - Analiza logs y detecta causas raíz de errores.')
    parser.add_argument('--logfile', required=True, help='Ruta del archivo de log')
    parser.add_argument('--csv', help='Exportar resultado a CSV')

    args = parser.parse_args()

    if not os.path.exists(args.logfile):
        print(f"❌ Archivo no encontrado: {args.logfile}")
        logging.error(f"Archivo no encontrado: {args.logfile}")
        return

    print(f"📖 Analizando: {args.logfile}")
    logging.info(f"Iniciando análisis del archivo: {args.logfile}")
    lineas = leer_log(args.logfile)
    bloques = stacktrace.extraer_stacktrace(lineas)

    resultados = []
    for i, bloque in enumerate(bloques, 1):
        causa = stacktrace.analizar_causa_raiz(bloque)
        print(f"🧪 Stack trace #{i}:")
        print(f"   ⚠️ {causa['tipo_error']} → {causa['descripcion']}")
        logging.info(f"Stack trace #{i} detectado: {causa['tipo_error']} → {causa['descripcion']}")
        resultados.append(causa)

    if args.csv:
        guardar_csv(resultados, args.csv)
        print(f"📤 Resultados exportados a: {args.csv}")

    logging.info("Análisis finalizado.")

if __name__ == '__main__':
    cli()

