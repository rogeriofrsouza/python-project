# python-project

A python project to recover data from a PDF.

## Technology and Resources

- [Python 3.11](https://www.python.org/downloads/release/python-3110/) - **pre-requisite**
- [Docker](https://www.docker.com/get-started) - **pre-requisite**
- [Docker Compose](https://docs.docker.com/compose/) - **pre-requisite**
- [Poetry](https://python-poetry.org/) - **pre-requisite**
- [Ruff](https://github.com/astral-sh/ruff)


## How to install, run and test

| Command  | Docker                 | Locally               | Description                            |
| -------- | ---------------------- | --------------------- | -------------------------------------- |
| install  | `make docker/install`  | `make local/install`  | to install                             |
| tests    | `make docker/tests`    | `make local/tests`    | to run the tests with coverage         |
| lint     | `make docker/lint`     | `make local/lint`     | to run static code analysis using ruff |
| lint/fix | `make docker/lint/fix` | `make local/lint/fix` | to fix files using ruff                |
| run      | `make docker/run`      | `make local/run`      | to run the project                     |
