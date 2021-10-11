# Testing mandatory


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
