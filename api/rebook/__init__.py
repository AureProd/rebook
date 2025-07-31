import sys

from rebook.core.logger import setup_logger

if "pytest" not in sys.modules:
    setup_logger()
