import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

def log_event(event: str):
    logging.info(event)
