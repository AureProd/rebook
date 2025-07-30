# Rebook

Rebook is a website allowing students to resell school books to each other.

## Requirements

- [git](https://git-scm.com/book/fr/v2/D%C3%A9marrage-rapide-Installation-de-Git)
- [docker](https://docs.docker.com/engine/install/ubuntu/)
- [python](https://vegastack.com/tutorials/how-to-install-python-3-11-on-ubuntu-22-04/)
- [poetry](https://pypi.org/project/poetry/)
- [pyenv](https://github.com/pyenv/pyenv)

## Quick start

### To setup the developpement instance

```bash
./setup
```

### To start the instance

```bash
docker compose up -d
```

### To stop the instance

```bash
docker compose down
```

### To see containers of the instance

```bash
docker compose ps
```

### To see api container logs

```bash
docker compose logs -f api
```

## For install poetry for dev in local

```bash
poetry install
```

## To run tests in local

### Linter and formater tests :

```sh
poetry run pre-commit run -a
```

## Pre-commit

For install pre-commit in your local repository

```bash
poetry run pre-commit install
```

## Naming convention

### For branchs

Format of branch name :
```txt
<type>/<name of branch>
```

Availables type :

- `feat` Add a feature
- `fix` Fix a bug
- `clean` Clean the codebase
- `refactor` Refactor the codebase

### For commits

Format of commit messages :

```txt
<type>(<scope>): <subject of commit>
```

Availables type :

- `feat` Add a feature
- `fix` Fix a bug
- `clean` Clean the codebase
- `ci` Change a file or add feature in link with the deployment of the application (Jenkins, Travis, Ansible, gitlabCI, npm, grunt, gulp, webpack, etc.)
- `docs` Add documentation (README, JSdoc, comments, etc.)
- `refactor` Change codebase without add feature or fix bug
- `test` Add test
