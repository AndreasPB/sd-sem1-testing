# Testing mandatory
[![codecov](https://codecov.io/gh/AndreasPB/sd-sem1-testing/branch/master/graph/badge.svg?token=DDUU0AX37Q)](https://codecov.io/gh/AndreasPB/sd-sem1-testing)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/AndreasPB/sd-sem1-testing/master.svg)](https://results.pre-commit.ci/latest/github/AndreasPB/sd-sem1-testing/master)
[![CodeFactor status](https://www.codefactor.io/repository/github/AndreasPB/sd-sem1-testing/badge)](https://www.codefactor.io/repository/github/AndreasPB/sd-sem1-testing)

### First time setup
Preqrequisites:
* Git

```bash
$ git clone <clone method of choice>
$ pip install pre-commit
$ pre-commit install
$ git checkout -b <branch name>
$ git add .
$ git commit -m "<commit message>"
$ git push --force-with-lease origin <branch name>
```

### How to build and run the tests
Preqrequisites:
* Docker

```bash
$ docker build -t testing .
$ docker run -it testing pytest
```
