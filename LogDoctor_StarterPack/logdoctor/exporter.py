# CSV/JSON export logic

import csv
from logdoctor import utils

def guardar_csv(resultados, output_file):
    try:
        with open(output_file, 'w', newline='') as csvfile:
            fieldnames = ['tipo_error', 'descripcion', 'causa_raiz']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for r in resultados:
                writer.writerow(r)
        utils.log_info(f"Exportación a CSV exitosa: {output_file}")
    except Exception as e:
        utils.log_error(f"Error exportando CSV: {e}")

