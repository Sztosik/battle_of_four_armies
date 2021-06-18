# The Battle of the Four Armies 

## Setup

```
$ git clone https://github.com/Sztosik/battle_of_four_armies.git
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
$ cd battle_of_four_armies
$ poetry shell
$ poetry install
$ python -m battle.simulation.init_window
```

## Scripts
__run formatting script__
```
$ cd scripts
$ ./formatting_check.sh
```

__run pylint_check.sh__
```
$ cd scripts
$ ./pylint_check.sh 
```

__run mypy_check.sh__
```
$ cd scripts
$ ./mypy_check.sh
```