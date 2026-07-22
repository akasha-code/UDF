# Contratos UDF

Estos JSON Schema convierten conceptos del framework en contratos intercambiables entre personas, herramientas y agentes.

| Esquema | Finalidad |
| --- | --- |
| `context-assessment.schema.json` | Registrar hechos, supuestos e incertidumbres del contexto |
| `delivery-profile.schema.json` | Expresar el perfil derivado y el estado razonado de cada capacidad |
| `mandate.schema.json` | Acotar autoridad, permisos, tolerancias, supervisión y terminación |
| `intervention-record.schema.json` | Auditar una actuación y los resultados o efectos producidos |

Los ejemplos de `schemas/examples/` se validan con:

```bash
python scripts/validate_repository.py
```

El contrato histórico [`templates/automation/handoff.schema.json`](../templates/automation/handoff.schema.json) se mantiene compatible. Un handoff puede transportar referencias a mandatos e intervenciones sin cambiar el esquema v1.
