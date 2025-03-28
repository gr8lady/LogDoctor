# Utility functions like timestamps

import logging

logging.basicConfig(
    filename='logs/logdoctor.log',
    filemode='a',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

def log_info(msg):
    print(f"[INFO] {msg}")
    logging.info(msg)

def log_error(msg):
    print(f"[ERROR] {msg}")
    logging.error(msg)

