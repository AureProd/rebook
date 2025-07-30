FROM ubuntu:24.04 AS builder

ARG PYTHON_VERSION=3.11

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev \
    libsqlite3-dev curl git libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev \
    libffi-dev liblzma-dev locales \
    && sed -i '/^# *fr_FR.UTF-8 UTF-8/s/^# *//' /etc/locale.gen \
    && locale-gen fr_FR.UTF-8 \
    && rm -rf /var/lib/apt/lists/*

# Install pyenv & compile custom python version
ENV PYENV_ROOT=/python
RUN curl https://pyenv.run | bash
ENV PATH=/python/shims/:/python/bin:$PATH
RUN env PYTHON_CONFIGURE_OPTS='--enable-optimizations --with-lto' PYTHON_CFLAGS='-march=native -mtune=native' pyenv install ${PYTHON_VERSION}
RUN pyenv global ${PYTHON_VERSION}

# Install poetry
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python3 -

ENV PATH="${PATH}:/opt/poetry/bin/"

WORKDIR /src

# ----------- Dependency Installation -------------
COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false \
    && poetry config virtualenvs.in-project false \
    && poetry config virtualenvs.use-poetry-python true \
    && poetry install --no-root --only main

COPY ./migrations migrations/

# ----------- Dev Stage -------------
FROM builder AS dev

RUN poetry install --no-root --with dev

ENV APP_DEBUG=1 \
    PYDEVD_DISABLE_FILE_VALIDATION=1 \
    TZ=Europe/Paris

EXPOSE 80 5678

CMD ["python", "-m", "debugpy", "--listen", "0.0.0.0:5678", "-m", "rebook"]

# ----------- Final Slim Runtime Stage -------------
FROM ubuntu:24.04

# Install required system packages
RUN apt-get update \
    && apt-get upgrade -y --no-install-recommends \
    && apt-get install -y --no-install-recommends curl tzdata libexpat1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /src

# Copy Python from builder
COPY --from=builder /python/versions /python/versions
RUN ln -s /python/versions/* /python/versions/3.11
ENV PATH=/python/versions/3.11/bin/:${PATH}

COPY ./rebook rebook/

COPY --from=builder /src/migrations migrations/

EXPOSE 80

ENV TZ=Europe/Paris

CMD ["python", "-m", "rebook"]
