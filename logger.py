# logger.py
import logging

logging.basicConfig(
    filename="logs/assistant.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def log_operation(expression, result):
    logging.info(f"Calculation: {expression} = {result}")
