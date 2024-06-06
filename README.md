# empkins-d03-preprocessing




## Project structure

```
empkins_d03_preprocessing
│   README.md
├── empkins_d03_preprocessing  # The core library folder. All project-wide helper and algorithms go here
|
├── experiments  # The main folder for all experiements. Each experiment has its own subfolder
|   ├── 2022_05_macro  # All scripts for Macro 1.0 study
|   |   ├── biomarker
|   |   ├── unipark
|   |   ├── config.json # Set up your path here ({"data_path":"<path_to_data_repo>"})
|   |
|   ├── experiment_2
|       ├── ...
|
|   pyproject.toml  # The required python dependencies for the project
|   poetry.lock  # The frozen python dependencies to reproduce exact results
|
```

## Usage

This project was created using the mad-cookiecutter ds-base template.

To work with the project you need to install:

- [poetry](https://python-poetry.org/docs/#installation)
- [poethepoet](https://github.com/nat-n/poethepoet) in your global python env (`pip install poethepoet`)

Afterwards run:

```
poetry install
```

Then you can create a new experiment using:

```
poe experiment experiment_name
```


### Dependency management

All dependencies are manged using `poetry`.
Poetry will automatically create a new venv for the project, when you run `poetry install`.
Check out the [documentation](https://python-poetry.org/docs/basic-usage/) on how to add and remove dependencies.


### Jupyter Notebooks

To use jupyter notebooks with the project you need to add a jupyter kernel pointing to the venv of the project.
This can be done by running:

```
poe conf_jupyter
```

Afterwards a new kernel called `empkins_d03_preprocessing` should be available in the jupyter lab / jupyter notebook interface.
Use that kernel for all notebooks related to this project.



All jupyter notebooks should go into the `notebooks` subfolder of the respective experiment.
To make best use of the folder structure, the parent folder of each notebook should be added to the import path.
This can be done by adding the following lines to your first notebook cell:

```python
# Optional: Auto reloads the helper and the main empkins_d03_preprocessing module
%load_ext autoreload
%autoreload 2

from empkins_d03_preprocessing import conf_rel_path
conf_rel_path()
```

This allows to then import the helper and the script module belonging to a specific experiment as follows:

```
import helper
# or
from helper import ...
```
