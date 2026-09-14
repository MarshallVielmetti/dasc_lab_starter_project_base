# DASC Lab Canonical Project

This repository is the source for the DASC lab starter project.

Implement complete reference solutions here, define the student exercises under `teaching/`, and use `startergen` to create and validate the student-facing repository.

## Set up the canonical project

Install the locked development environment:

```bash
uv sync --locked --group test
```

Run all canonical tests:

```bash
uv run pytest
```

The canonical checkout should pass its private, public, and smoke tests before generating a student artifact.

## Generate the student project

With `project_generator` checked out as a sibling directory, validate the teaching metadata:

```bash
uv run --project ../project_generator/tools/startergen \
  startergen validate --root .
```

Run the complete isolated check:

```bash
uv run --project ../project_generator/tools/startergen \
  startergen check --root . --json
```

The check validates the canonical tests, generates `build/starter`, verifies the intended incomplete-exercise failures, restores solutions in dependency order, and confirms deterministic output.

Use `startergen build` and `startergen docs` separately when you want to inspect intermediate outputs.

## Repository boundary

The completed implementations, private tests, and `teaching/` inputs belong only in this canonical repository.

The generated `build/starter` tree contains the student stubs, public and smoke tests, generated README, documentation assets, and provenance manifest.

Do not manually maintain generated files in the student repository because a `startergen release` replaces its contents with the validated artifact.
