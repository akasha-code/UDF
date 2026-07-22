#!/usr/bin/env python3
"""Derive a conservative UDF delivery profile from a context assessment."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


ORDER = {"low": 0, "medium": 1, "high": 2, "critical": 3}
DOCS = ["minimal", "light", "standard", "complete", "regulated"]


def _capability(identifier: str, status: str, reason: str) -> dict[str, str]:
    return {"id": identifier, "status": status, "reason": reason}


def derive_profile(assessment: dict[str, Any]) -> dict[str, Any]:
    required = {
        "assessment_id",
        "criticality",
        "reversibility",
        "regulated",
        "data_sensitivity",
        "sovereignty",
        "autonomy",
        "execution_topology",
        "change_cadence",
        "organizational_maturity",
    }
    missing = sorted(required - assessment.keys())
    if missing:
        raise ValueError(f"Missing required fields: {', '.join(missing)}")

    criticality = assessment["criticality"]
    reversibility = assessment["reversibility"]
    sensitivity = assessment["data_sensitivity"]
    autonomy = assessment["autonomy"]
    maturity = assessment["organizational_maturity"]
    regulated = assessment["regulated"]
    sovereignty = assessment["sovereignty"]

    score = ORDER[criticality]
    rationale = [f"La criticidad {criticality} establece la base de assurance."]
    if regulated:
        score = max(score, 2)
        rationale.append("La regulación requiere trazabilidad y documentación reforzadas.")
    if reversibility in {"difficult", "irreversible"}:
        score = max(score, 2 if reversibility == "difficult" else 3)
        rationale.append(f"La reversibilidad {reversibility} eleva supervisión y recuperación.")
    if sensitivity == "restricted":
        score = max(score, 3)
        rationale.append("Los datos restringidos exigen controles críticos.")
    elif sensitivity == "confidential":
        score = max(score, 2)
        rationale.append("Los datos confidenciales elevan los controles de acceso y auditoría.")
    if autonomy == "high":
        score = max(score, 3)
        rationale.append("La autonomía alta requiere assurance y supervisión continuas.")
    elif autonomy in {"bounded", "supervised"}:
        score = max(score, 2)
        rationale.append("La ejecución autónoma acotada requiere límites y observabilidad.")

    assurance = ["low", "medium", "high", "critical"][score]
    doc_index = score
    documentation = "regulated" if regulated else DOCS[min(doc_index, len(DOCS) - 1)]

    if regulated or reversibility == "irreversible" or score == 3:
        oversight = "mandatory"
    elif autonomy in {"approval_required", "bounded", "supervised", "high"}:
        oversight = "approval_on_effect" if autonomy in {"approval_required", "bounded"} else "supervised"
    else:
        oversight = "advisory"
    if maturity == "initial" and autonomy in {"bounded", "supervised", "high"}:
        oversight = "mandatory"
        rationale.append("La madurez inicial impide confiar solo en autonomía técnica.")

    audit_status = "required" if regulated or score >= 2 else "recommended"
    sandbox_status = "required" if autonomy in {"bounded", "supervised", "high"} else "recommended"
    approval_status = "required" if oversight != "advisory" else "recommended"
    sovereignty_status = "required" if sovereignty == "required" else ("recommended" if sovereignty == "preferred" else "optional")
    rag_requested = bool(assessment.get("rag_requested"))
    knowledge_volume = assessment.get("knowledge_volume", "small")
    if rag_requested:
        rag_status = "recommended"
        rag_reason = "RAG fue solicitado; requiere procedencia, permisos y evaluación de recuperación."
    elif knowledge_volume in {"large", "distributed"}:
        rag_status = "optional"
        rag_reason = "El conocimiento amplio puede justificar RAG si la recuperación simple no alcanza."
    else:
        rag_status = "not_applicable"
        rag_reason = "El contexto informado no demuestra necesidad de recuperación aumentada."
    staffing_requested = bool(assessment.get("staffing_requested"))
    staffing_status = "recommended" if staffing_requested else "not_applicable"
    staffing_reason = (
        "La selección dinámica de actores fue solicitada; debe respetar mandato, presupuesto y auditoría."
        if staffing_requested
        else "No se solicitó selección dinámica de actores."
    )

    capabilities = [
        _capability("audit_trail", audit_status, "Trazabilidad proporcional a regulación, criticidad y datos."),
        _capability("least_privilege", "required" if autonomy != "none" else "recommended", "Limita el alcance de una intervención comprometida o errónea."),
        _capability("execution_sandbox", sandbox_status, "Aísla efectos cuando actores técnicos pueden ejecutar herramientas."),
        _capability("human_approval", approval_status, "Ubica control humano antes de efectos que exceden el modo asistivo."),
        _capability("rollback", "required" if reversibility != "easy" else "recommended", "La recuperación debe corresponder a la reversibilidad del efecto."),
        _capability("sovereignty_controls", sovereignty_status, "Residencia, jurisdicción, claves y portabilidad se deciden por contexto."),
        _capability("rag", rag_status, rag_reason),
        _capability("agent_staffing", staffing_status, staffing_reason),
        _capability("mcp_interface", "optional", "MCP aporta valor si varios clientes necesitan herramientas o recursos; no es obligatorio."),
        _capability("browser_testing", "optional", "Activar cuando una superficie web forme parte del comportamiento crítico."),
    ]

    return {
        "schema_version": "1.0.0",
        "assessment_id": assessment["assessment_id"],
        "documentation_depth": documentation,
        "assurance_level": assurance,
        "human_oversight": oversight,
        "capabilities": capabilities,
        "rationale": rationale,
        "unknowns": assessment.get("unknowns", []),
        "requires_human_confirmation": True,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("assessment", type=Path, help="Path to a context assessment JSON file")
    parser.add_argument("--output", type=Path, help="Write the profile to this file")
    args = parser.parse_args()
    try:
        assessment = json.loads(args.assessment.read_text(encoding="utf-8"))
        profile = derive_profile(assessment)
    except (OSError, json.JSONDecodeError, KeyError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    payload = json.dumps(profile, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
