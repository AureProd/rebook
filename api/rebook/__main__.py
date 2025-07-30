"""Main module of the Rebook API."""

from logging import getLogger

import uvicorn

from rebook.core import env

LOGGER = getLogger(__name__)

if __name__ == "__main__":
    UVICORN_APP = "rebook.core.app:app"
    UVICORN_HOST = "0.0.0.0"
    UVICORN_PORT = 80

    if env.APP_ENV == "dev":
        config = uvicorn.Config(
            app=UVICORN_APP,
            host=UVICORN_HOST,
            port=UVICORN_PORT,
            log_config=None,
            reload=True,
            reload_dirs="/src/rebook",
        )
    else:
        config = uvicorn.Config(app=UVICORN_APP, host=UVICORN_HOST, port=UVICORN_PORT, log_config=None)

    server = uvicorn.Server(config)
    server.run([config.bind_socket()])
