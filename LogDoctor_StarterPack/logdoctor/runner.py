
import os
import logging
import csv
from logdoctor import stacktrace
from logdoctor import parser, exporter, utils


# Configurar logging interno
logging.basicConfig(
    filename='logs/logdoctor.log',
    filemode='a',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)


def run_analysis(logfile, csv_output=None):
    if not os.path.exists(logfile):
        print(f"❌ Archivo no encontrado: {logfile}")
        logging.error(f"Archivo no encontrado: {logfile}")
        return

    print(f"📖 Analizando: {logfile}")
    logging.info(f"Iniciando análisis del archivo: {logfile}")
    lineas = parser.leer_log(logfile)
    bloques = stacktrace.extraer_stacktrace(lineas)

    resultados = []
    for i, bloque in enumerate(bloques, 1):
        causa = stacktrace.analizar_causa_raiz(bloque)
        print(f"🧪 Stack trace #{i}:")
        print(f"   ⚠️ {causa['tipo_error']} → {causa['descripcion']}")
        logging.info(f"Stack trace #{i} detectado: {causa['tipo_error']} → {causa['descripcion']}")
        resultados.append(causa)

    if csv_output:
        exporter.guardar_csv(resultados, csv_output)
        print(f"📤 Resultados exportados a: {csv_output}")

# Errores sueltos
    errores_sueltos = parser.buscar_errores_sueltos(lineas)
    if errores_sueltos:
        print("\n📛 Errores sueltos detectados:")
        for idx, err in enumerate(errores_sueltos, 1):
            print(f"   🧨 Línea {idx}: {err}")
        utils.log_info(f"{len(errores_sueltos)} errores sueltos encontrados en el log.")
    else:
        print("\n✅ No se encontraron errores sueltos.")
        utils.log_info("No se encontraron errores sueltos en el log.")

    if csv_output:
        exporter.guardar_csv(resultados, csv_output)
        print(f"📤 Resultados exportados a: {csv_output}")

    logging.info("Análisis finalizado.")

