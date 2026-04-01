# Automation / interoperability templates (UDF)

These files support the **agent-ready** profile described in the UDF wiki:

- [17 — Interoperabilidad y automatización](https://github.com/akasha-code/UDF/wiki/17-interoperabilidad-y-automatizacion)

## Contents

| File | Purpose |
| ---- | ------- |
| `handoff.schema.json` | JSON Schema for handoff messages between actors (human, agent, or service). |
| `artifact-manifest.example.yaml` | Example manifest for a package of work: state (`draft` / `under_review` / `accepted`), refs, provenance, gate ids. |
| `gate-checks.example.yaml` | Example list of automated vs manual checks for a Stage Review gate. |

## Usage

1. Copy the examples into your repository and remove `.example` from filenames if you treat them as live config.
2. Validate handoff JSON against `handoff.schema.json` in CI or locally (e.g. with a JSON Schema validator).
3. Align `state` transitions with your Stage Review process and ownership rules.
4. Keep `schema_version` in YAML/JSON payloads so you can evolve fields without breaking orchestrators.

## Relationship to UDF artifacts

These templates complement standard UDF artifacts (e.g. `validation_manifest.yaml`, `stage_review_board.md`, ADRs). They do not replace governance; they make handoffs and gates **machine-readable** where useful.

## License

Apache License 2.0 — see [LICENSE](../../LICENSE) in the repository root.
