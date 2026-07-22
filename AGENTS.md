# UDF repository guidance

## Purpose

This repository defines the Unified Delivery Framework (UDF). Treat the wiki, schemas, templates, examples, and skill as one versioned framework.

## Operating modes

Resolve the requested mode before acting:

- `analyze`: inspect and explain; do not modify files or external systems.
- `assess`: derive a proposed UDF delivery profile; do not adopt it automatically.
- `plan`: prepare an implementation or adoption plan; do not execute it.
- `apply`: modify only the authorized scope.
- `validate`: run checks and report evidence.
- `review-gate`: assess evidence; do not approve on behalf of an accountable principal.
- `audit`: identify gaps, risks, and uncertainty without silently repairing them.

If the request does not authorize mutation, default to `analyze` or `assess`.

## Framework rules

- Keep UDF technology-agnostic. Describe durable capabilities and selection criteria before naming products.
- Treat CLI, API, MCP, ACP, skills, SDKs, GUI, and TUI as independent interfaces. Expand ambiguous protocol acronyms with specification and version.
- Treat execution location and trust boundary separately from protocol choice.
- Mark capabilities as `required`, `recommended`, `optional`, `not_applicable`, or `discouraged` with a reason.
- Preserve human or organizational accountability when work is delegated to technical agents.
- Distinguish work products, interventions, state changes, decisions, evidence, and outcomes.
- Do not make RAG, agent staffing, cloud, MCP, or any named product mandatory without contextual evidence.
- Prefer backwards-compatible schema evolution. Add a new version for breaking changes.

## Sources of truth

- Start with `README.md` and `wiki/00-overview.md`.
- Use `wiki/18-agencia-mandatos-intervenciones.md` for the actor and delegation model.
- Use `wiki/19-contexto-assurance-capacidades.md` for assessment and delivery-profile derivation.
- Use `wiki/20-arquitectura-agentic-e-integraciones.md` for LLM, agent, harness, RAG, staffing, MCP/API/CLI, local/cloud, and testing guidance.
- Use `wiki/21-documentacion-agent-ready.md` for documentation and agent discoverability.
- Use `schemas/` for machine-readable contracts.
- Use `skills/udf/` for the portable agent workflow.

## Validation

After changing normative content or schemas, run:

```bash
python scripts/validate_repository.py
python skills/udf/scripts/test_derive_profile.py
python /path/to/skill-creator/scripts/quick_validate.py skills/udf
```

Report checks actually executed and any validation that remains unavailable.
