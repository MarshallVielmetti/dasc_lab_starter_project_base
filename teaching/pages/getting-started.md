# Getting started

## Prerequites

Insure the following dependencies are installed on your system:

- `Python>=3.13`
- `uv` - A modern python dependency manager
- `git` - Version control

Make sure to also create a GitHub account.

## Install the Project

Start by forking the starter repository. Follow this link to the [starter_repository](https://github.com/MarshallVielmetti/dasc_lab_starter_project).
On the top right, click 'fork', keep default settings, then hit 'create fork'.

Clone the generated student repository.

!!! tip "GitHub Insructions"
    If this is your first time working with Git or GitHub, please refer to the [DASC Wiki](https://wiki.tmvlab.com) and find the `Git` section under `Coding`.

Enter the project directory, and use `uv` to install the project test dependencies.

```bash
cd dasc_lab_starter_project
uv sync --locked --group test

```

Run the public and smoke tests:

```bash
uv run pytest
```

The exercise tests are expected to fail until you complete the corresponding implementation.

!!! tip "Work in small steps"
    Run the narrowest relevant public test while implementing an exercise, then run the complete suite before committing.
