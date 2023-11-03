# python-project

A python project to recover data from PDF

## Technology and Resources

- [Python 3.11](https://www.python.org/downloads/release/python-3110/) - **pre-requisite**
- [Docker](https://www.docker.com/get-started) - **pre-requisite**
- [Docker Compose](https://docs.docker.com/compose/) - **pre-requisite**
- [Poetry](https://python-poetry.org/) - **pre-requisite**
- [Ruff](https://github.com/astral-sh/ruff)
- [Dynaconf](https://www.dynaconf.com/)

_Please pay attention on **pre-requisites** resources that you must install/configure._

## How to install, run and test

### Environment variables

_Use this section to explain each env variable available on your application_

| Variable | Description                | Available Values                 | Default Value | Required |
| -------- | -------------------------- | -------------------------------- | ------------- | -------- |
| ENV      | The application enviroment | `development / test / qa / prod` | `development` | Yes      |

_Note: When you run the install command (using docker or locally), a .env file will be created automatically based on [env.template](env.template)_

| Command  | Docker                 | Locally               | Description                            |
| -------- | ---------------------- | --------------------- | -------------------------------------- |
| install  | `make docker/install`  | `make local/install`  | to install                             |
| tests    | `make docker/tests`    | `make local/tests`    | to run the tests with coverage         |
| lint     | `make docker/lint`     | `make local/lint`     | to run static code analysis using ruff |
| lint/fix | `make docker/lint/fix` | `make local/lint/fix` | to fix files using ruff                |
| run      | `make docker/run`      | `make local/run`      | to run the project                     |

**Helpful commands**

_Please, check all available commands in the [Makefile](Makefile) for more information_.
