# Getting started

Clone the generated student repository and create its locked environment:

```bash
git clone https://github.com/MarshallVielmetti/dasc_lab_starter_project.git
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

The generated repository is a student workspace.
Changes to the assignment itself belong in the canonical `dasc_lab_starter_project_base` repository and are published through `startergen`.
