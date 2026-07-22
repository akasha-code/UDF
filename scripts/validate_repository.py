#!/usr/bin/env python3
"""Validate UDF schemas, examples, navigation, and skill metadata without dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = {
    "context-assessment.example.json": "context-assessment.schema.json",
    "delivery-profile.example.json": "delivery-profile.schema.json",
    "mandate.example.json": "mandate.schema.json",
    "intervention-record.example.json": "intervention-record.schema.json",
}
LINK_SOURCES = [
    "README.md",
    "llms.txt",
    "schemas/README.md",
    "skills/udf/SKILL.md",
    "wiki/18-agencia-mandatos-intervenciones.md",
    "wiki/19-contexto-assurance-capacidades.md",
    "wiki/20-arquitectura-agentic-e-integraciones.md",
    "wiki/21-documentacion-agent-ready.md",
    "wiki/22-alineacion-pmi-prince2-ia.md",
]


def validate(instance: Any, schema: dict[str, Any], path: str = "$") -> list[str]:
    errors: list[str] = []
    expected_type = schema.get("type")
    type_map = {
        "object": dict,
        "array": list,
        "string": str,
        "boolean": bool,
        "integer": int,
        "number": (int, float),
    }
    if expected_type and not isinstance(instance, type_map[expected_type]):
        return [f"{path}: expected {expected_type}, got {type(instance).__name__}"]
    if "const" in schema and instance != schema["const"]:
        errors.append(f"{path}: expected constant {schema['const']!r}")
    if "enum" in schema and instance not in schema["enum"]:
        errors.append(f"{path}: value {instance!r} is not in {schema['enum']!r}")
    if isinstance(instance, dict):
        properties = schema.get("properties", {})
        for key in schema.get("required", []):
            if key not in instance:
                errors.append(f"{path}: missing required property {key!r}")
        if schema.get("additionalProperties") is False:
            for key in instance.keys() - properties.keys():
                errors.append(f"{path}: unexpected property {key!r}")
        for key, value in instance.items():
            if key in properties:
                errors.extend(validate(value, properties[key], f"{path}.{key}"))
    if isinstance(instance, list):
        if len(instance) < schema.get("minItems", 0):
            errors.append(f"{path}: expected at least {schema['minItems']} items")
        if schema.get("uniqueItems"):
            serialized = [json.dumps(item, sort_keys=True) for item in instance]
            if len(serialized) != len(set(serialized)):
                errors.append(f"{path}: items must be unique")
        item_schema = schema.get("items")
        if item_schema:
            for index, value in enumerate(instance):
                errors.extend(validate(value, item_schema, f"{path}[{index}]"))
    if isinstance(instance, str):
        if len(instance) < schema.get("minLength", 0):
            errors.append(f"{path}: string is shorter than {schema['minLength']}")
        if "pattern" in schema and not re.search(schema["pattern"], instance):
            errors.append(f"{path}: does not match {schema['pattern']!r}")
    return errors


def validate_examples() -> list[str]:
    errors: list[str] = []
    for example_name, schema_name in EXAMPLES.items():
        example_path = ROOT / "schemas" / "examples" / example_name
        schema_path = ROOT / "schemas" / schema_name
        try:
            example = json.loads(example_path.read_text(encoding="utf-8"))
            schema = json.loads(schema_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{example_name}: {exc}")
            continue
        errors.extend(f"{example_name}: {error}" for error in validate(example, schema))
    return errors


def validate_navigation() -> list[str]:
    errors: list[str] = []
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    wiki_index = (ROOT / "wiki" / "README.md").read_text(encoding="utf-8")
    llms = (ROOT / "llms.txt").read_text(encoding="utf-8")
    for number in range(23):
        matches = list((ROOT / "wiki").glob(f"{number:02d}-*.md"))
        if len(matches) != 1:
            errors.append(f"wiki: expected one document for {number:02d}, found {len(matches)}")
            continue
        filename = matches[0].name
        for label, content in (("README.md", readme), ("wiki/README.md", wiki_index)):
            if filename not in content:
                errors.append(f"{label}: missing {filename}")
    for required in ("README.md", "AGENTS.md", "skills/udf/SKILL.md", "schemas/README.md"):
        if required not in llms:
            errors.append(f"llms.txt: missing {required}")
    return errors


def validate_skill() -> list[str]:
    errors: list[str] = []
    skill = (ROOT / "skills" / "udf" / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", skill, flags=re.DOTALL)
    if not match:
        return ["skills/udf/SKILL.md: missing YAML frontmatter"]
    keys = []
    for line in match.group(1).splitlines():
        if ":" in line and not line.startswith((" ", "\t")):
            keys.append(line.split(":", 1)[0])
    if keys != ["name", "description"]:
        errors.append(f"skills/udf/SKILL.md: frontmatter keys must be name, description; got {keys}")
    if "name: udf" not in match.group(1):
        errors.append("skills/udf/SKILL.md: name must be udf")
    config = (ROOT / "skills" / "udf" / "agents" / "openai.yaml").read_text(encoding="utf-8")
    if "$udf" not in config:
        errors.append("skills/udf/agents/openai.yaml: default_prompt must mention $udf")
    return errors


def validate_local_links() -> list[str]:
    errors: list[str] = []
    pattern = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
    for relative_source in LINK_SOURCES:
        source = ROOT / relative_source
        content = source.read_text(encoding="utf-8")
        for raw_target in pattern.findall(content):
            target = raw_target.strip().strip("<>").split("#", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            resolved = (source.parent / target).resolve()
            if not resolved.exists():
                errors.append(f"{relative_source}: broken local link {raw_target!r}")
    return errors


def main() -> int:
    errors = validate_examples() + validate_navigation() + validate_skill() + validate_local_links()
    if errors:
        for error in errors:
            print(f"ERROR {error}")
        return 1
    print(f"Validated {len(EXAMPLES)} schema examples, 23 wiki entries, local links, and the UDF skill metadata.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
