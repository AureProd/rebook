"""
This module collects the environment variables used by the PureAPI.
"""

from os import getenv

APPLICATION_NAME = "ReBook"
APPLICATION_DESCRIPTION = "Website for refund books"
APPLICATION_CONTACT_NAME = "AureProd"
APPLICATION_CONTACT_EMAIL = "aureprod0@gmail.com"
APPLICATION_CONTACT_WEBSITE = "https://github.com/AureProd"

APPLICATION_VERSION = getenv("APP_VERSION", "latest")
APP_ENV = getenv("APP_ENV", default="prod")

DB_HOST = "db"
DB_PORT = 3306
DB_NAME = "db"
DB_USERNAME = "root"
DB_PASSWORD = getenv("DB_PASSWORD")

LOGS_FILE_PATH = "/logs/api/server.log"
MIGRATIONS_FOLDER_PATH = "/src/migrations"
