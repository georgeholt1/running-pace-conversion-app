# Running Pace Conversion App

A simple app that converts from running pace to speed and vice versa.

Given any one of the following inputs:

- Pace in minutes per kilometer
- Pace in minutes per mile
- A distance in kilometers or miles and a time

The app will calculate pace in minutes per kilometer and per mile, as well as speed in kilometers per hour and miles per hour.

The app is deployed [here](https://running-pace-conversion.streamlit.app/).

## Installation

Start by cloning the repository.

Dependency management is performed using [Poetry](https://python-poetry.org/):

```bash
poetry install
```

## Usage

To run the app, execute the following command:

```bash
poetry run streamlit run running-pace-converter.py
```

## Development

After installing the dependencies with `poetry install`, start a shell session with

```bash
poetry shell
```

and install the pre-commit hooks with

```bash
pre-commit install
```