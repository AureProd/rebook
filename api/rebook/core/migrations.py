from logging import getLogger

from alembic import command
from alembic.config import Config

from rebook.core import env

LOGGER = getLogger(__name__)


def run_migrations():
    # Dynamically build Alembic config
    config = Config()

    # Path to your migration scripts
    config.set_main_option("script_location", env.MIGRATIONS_FOLDER_PATH)

    # Set your DB connection string (from env, or a config file, etc.)
    config.set_main_option(
        "sqlalchemy.url",
        f"mysql+pymysql://{env.DB_USERNAME}:{env.DB_PASSWORD}@{env.DB_HOST}:{env.DB_PORT}/{env.DB_NAME}",
    )

    command.upgrade(config, "head")

    LOGGER.info("Migrations applied.")
