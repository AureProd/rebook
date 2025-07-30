import logging
import sys
from pathlib import Path

from rebook.core import env


def setup_logger():
    logger = logging.getLogger()

    logger.setLevel(logging.DEBUG)  # Global logger must be set to the **lowest** level you want to capture anywhere.

    formatter = logging.Formatter(
        fmt="{asctime} {levelname} - {filename} - {message}", datefmt="%Y-%m-%d %H:%M:%S", style="{"
    )

    # Console handler (INFO and above)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File handler (DEBUG and above)
    log_file_path = Path(env.LOGS_FILE_PATH)
    file_handler = logging.FileHandler(log_file_path, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.info(f"Logger setup and ready. Logs will also be written to '{log_file_path}'.")
