# DASC Lab Canonical Project

This repository is the source for the DASC lab starter project.

Implement and test complete reference solutions here, describe which parts become student exercises under `teaching/`, and use `startergen` to generate the student-facing repository.

The checked-in canonical project should always contain working solutions.

`startergen` creates the incomplete student version; do not replace canonical implementations with stubs by hand.

## Project flow

```text
completed canonical project (this repository)
                    |
                    | startergen validate/build/docs/check
                    v
             build/starter
                    |
                    | startergen release
                    v
    MarshallVielmetti/dasc_lab_starter_project
```

## Repository map

| Path | Purpose | Included in the student project? |
| --- | --- | --- |
| `src/dasc_lab/` | Completed reference implementations | Yes, after declared exercise bodies are replaced |
| `tests/public/` | Student-visible behavioral tests | Yes |
| `tests/private/` | Instructor-only checks for the completed project | No |
| `tests/smoke/` | Installation and import checks | Yes |
| `examples/` | Student-facing examples | Yes |
| `teaching/config.yml` | Project, output, allowlist, documentation, and release settings | No |
| `teaching/exercises.yml` | Exercise targets, dependencies, scaffolds, and expected baseline failures | No |
| `teaching/project.md` | Main student instructions | Rendered into generated documentation |
| `teaching/templates/` | Generated README templates | Rendered into generated documentation |
| `teaching/assets/` | Images and other documentation assets | Yes, through documentation generation |
| `teaching/background/` | Student-facing background material | Yes, through documentation generation |
| `build/` | Disposable generated artifacts and reports | Never commit |

## Initial setup

Install [uv](https://docs.astral.sh/uv/) and use Python 3.11 through 3.14.

Create the locked development environment:

```bash
uv sync --locked --group test
```

Run all canonical tests:

```bash
uv run pytest
```

The canonical private, public, and smoke suites must all pass before generating a student artifact.

## Modify the project

### Change or add completed code

The complete instructor implementation is given under `src/dasc_lab/`.

Keep exercise targets as ordinary top-level functions or class methods with stable qualified names, such as `UnicycleDynamics.f`.

Add corresponding tests:

- Put the behavioral contract students can see in `tests/public/`.
- Put edge cases or instructor-only checks in `tests/private/`.
- Update `tests/smoke/` when new packages or important imports are introduced.

Run `uv run pytest` until the completed canonical project passes every test.

### Add or modify an exercise

Edit `teaching/exercises.yml` and add one entry for each implementation that `startergen` should replace.

Each entry defines:

- `id`: a stable lowercase kebab-case identifier.
- `source.file`: the source path relative to this repository.
- `source.symbol`: the exact qualified function or method name.
- `requires`: exercise IDs that must be restored first.
- `starter.body`: `null` for the standard `NotImplementedError`, or a custom body string for a different scaffold.
- `starter.docstring`: whether to `preserve` or `drop` the canonical docstring.
- `tests.public`: the exact pytest node IDs owned by the exercise.
- `tests.baseline`: the expected initial student failure for each public test.

Use `expected: stub_error` when the generated function should raise `NotImplementedError`.

Use `expected: assertion_failure` for a custom scaffold that runs but returns deliberately incomplete behavior, and provide its exact `assertion_message`.

Keep public test node IDs and baseline node IDs in one-to-one correspondence.

### Change student documentation

Edit `teaching/project.md` for the main instructions.

Insert an exercise link with a standalone directive:

```text
{{ exercise("unicycle-dynamics") }}
```

Place images in `teaching/assets/`, background readings in `teaching/background/`, and README layout changes in `teaching/templates/README.md.j2`.

`startergen docs` resolves exercise links against the final transformed source, so generated line numbers should not be maintained manually.

### Change dependencies or distributed files

Edit `pyproject.toml`, then refresh and verify the lockfile:

```bash
uv lock
uv sync --locked --group test
uv run pytest
```

Update `starter.include` in `teaching/config.yml` whenever a new student-facing file or directory must be copied.

Keep completed solutions, private tests, credentials, caches, generator tooling, and instructor-only material out of the allowlist.

## Run `startergen`

These commands assume `project_generator` is checked out next to this repository:

```text
repos/
├── dasc_lab_starter_project_base/
├── dasc_lab_starter_project/
└── project_generator/
```

Run the commands below from this repository's root.

### 1. Validate authoring metadata

```bash
uv run --project ../project_generator/tools/startergen \
  startergen validate --root .
```

This checks YAML schemas, paths, exercise symbols, dependency ordering, test references, and output safety without changing generated outputs.

### 2. Build the student source tree

```bash
uv run --project ../project_generator/tools/startergen \
  startergen build --root .
```

Inspect `build/starter/` to confirm that only allowlisted student files are present and every declared exercise has the intended scaffold.

The build records deterministic file hashes and input provenance in `build/starter/.startergen/manifest.json`.

### 3. Generate student documentation

```bash
uv run --project ../project_generator/tools/startergen \
  startergen docs --root .
```

Inspect these outputs:

- `build/starter/README.md` for the generated student README.
- `build/docs-src/` for generated source documentation and exercise metadata.
- `build/site/` for the versioned documentation site.

External HTTP links are skipped by default.

Add `--check-external-links` only when network-backed link checking is intended.

### 4. Run the complete isolated check

```bash
uv run --project ../project_generator/tools/startergen \
  startergen check --root . --json
```

This is the main pre-release command.

It verifies that:

- The completed canonical private, public, and smoke tests pass.
- The generated package installs in a clean temporary environment.
- Student smoke tests pass.
- Every unfinished exercise fails for its declared baseline reason.
- Restoring exercises in dependency order makes the appropriate tests pass.
- The fully restored student project passes all public tests.
- Two independent builds produce identical artifacts and documentation.

## Publish a student release

Before publishing:

1. Update `publication.release_id` in `teaching/config.yml` to a new immutable release ID.
2. Run the full `startergen check` successfully with that release ID.
3. Commit the canonical changes so this checkout is clean and the source revision is auditable.
4. Ensure the separate `dasc_lab_starter_project` checkout is on its clean `main` branch.

Create and inspect a release plan without modifying the student repository:

```bash
uv run --project ../project_generator/tools/startergen \
  startergen release --root . --dry-run --json
```

The dry run writes the reviewable transaction to `build/release/<release_id>/transaction.json`.

Publish the validated artifact and versioned documentation:

```bash
uv run --project ../project_generator/tools/startergen \
  startergen release \
  --root . \
  --starter-worktree ../dasc_lab_starter_project \
  --docs-root ../dasc_lab_starter_project_docs \
  --json
```

The real release replaces all non-Git contents of the student checkout with the validated artifact, commits and pushes `main`, creates the immutable release tag, verifies both remote references, and publishes the versioned documentation tree.

Do not run a real release with uncommitted canonical or student-repository changes.

## Routine change checklist

For a normal exercise update:

1. Implement the complete solution in `src/dasc_lab/`.
2. Add or update public, private, and smoke tests.
3. Update `teaching/exercises.yml` and student documentation.
4. Run `uv run pytest`.
5. Run `startergen validate`.
6. Run `startergen build` and `startergen docs`, then inspect their outputs.
7. When preparing a release, increment `publication.release_id`.
8. Run the complete `startergen check --json`.
9. Commit the canonical project, review a release dry run, and publish when ready.

## Repository boundary

The canonical repository is the only source of truth for completed implementations, private tests, exercise metadata, and teaching content.

The student repository and everything under `build/` are generated outputs.

Do not fix generated student files directly; make the change here and rerun `startergen`.
