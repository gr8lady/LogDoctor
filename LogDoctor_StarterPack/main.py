
import argparse
from logdoctor import runner

def cli():
    parser = argparse.ArgumentParser(description='LogDoctor - Analiza logs y detecta causas raíz de errores.')
    parser.add_argument('--logfile', required=True, help='Ruta del archivo de log')
    parser.add_argument('--csv', help='Exportar resultado a CSV')

    args = parser.parse_args()

    runner.run_analysis(logfile=args.logfile, csv_output=args.csv)

if __name__ == '__main__':
    cli()

