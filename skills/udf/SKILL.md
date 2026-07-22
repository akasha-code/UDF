---
name: udf
description: Analiza, evalúa, planifica, aplica, valida, revisa gates o audita proyectos con Unified Delivery Framework (UDF). Usar cuando se necesite adaptar gobierno, artefactos, calidad, delivery, agentes humanos o técnicos, mandatos, guardrails, RAG, MCP, soberanía o documentación agent-ready al contexto real de un proyecto.
---

# Unified Delivery Framework

Aplicá UDF como un marco contextual, no como una lista universal de documentos o tecnologías. Conservá la responsabilidad en personas y organizaciones aunque el trabajo sea ejecutado por agentes técnicos.

## Elegir el modo

Determiná un modo antes de actuar:

- `analyze`: explicar el estado y las alternativas sin modificar nada;
- `assess`: producir un assessment de contexto, supuestos e incertidumbres;
- `plan`: proponer perfil, artefactos, controles, responsables y validación;
- `apply`: modificar solo lo autorizado y dentro de un mandato explícito;
- `validate`: comprobar contratos, evidencia, implementación o conformidad;
- `review-gate`: preparar o evaluar una decisión Go/No-Go/Conditional Go;
- `audit`: reconstruir mandatos, intervenciones, decisiones y desviaciones.

Si el usuario pide analizar, discutir, evaluar posibilidades o dar una opinión, usá `analyze` o `assess` y mantené el trabajo en modo de solo lectura. No conviertas una exploración en cambios.

## Flujo

1. Inspeccioná instrucciones, documentación, estado y evidencia disponible.
2. Declará hechos verificados, supuestos, incertidumbres y decisiones pendientes.
3. Leé [references/ontology.md](references/ontology.md) para clasificar principal, actores, agentes, equipos, mandatos e intervenciones.
4. En `assess` o `plan`, leé [references/assessment.md](references/assessment.md) y completá el assessment antes de recomendar controles.
5. Leé [references/capabilities.md](references/capabilities.md) solo si hay que seleccionar arquitectura, herramientas o interfaces.
6. Derivá un perfil inicial con `python skills/udf/scripts/derive_profile.py <assessment.json>` cuando exista una entrada estructurada.
7. Ajustá el resultado con evidencia y juicio humano. Explicá toda divergencia respecto de las reglas automáticas.
8. En `apply`, confirmá alcance, permisos, prohibiciones, efectos sensibles y validación antes de modificar.
9. Validá con los mecanismos del proyecto y registrá evidencia observada; no afirmes resultados no ejecutados.

## Reglas invariantes

- Separá capacidad de dominio, interfaz, transporte, despliegue y límite de confianza.
- Tratá CLI, API, MCP, ACP, skill, GUI y TUI como interfaces independientes; expandí protocolos ambiguos con nombre y versión.
- No interpretes MCP como sinónimo de internet o nube.
- Distinguí una llamada directa a un LLM de un agente con objetivo, ciclo, estado, herramientas y autoridad.
- Conservá `team` como composición coordinada de actores humanos, técnicos o híbridos.
- Distinguí work product, cambio de estado, decisión, evidencia, outcome e intervención.
- Clasificá capacidades como `required`, `recommended`, `optional`, `not_applicable` o `discouraged`, siempre con una razón.
- Tratá RAG, staffing, MCP, cloud y herramientas específicas como opciones contextuales.
- Preferí mínimo privilegio, reversibilidad, trazabilidad y aprobación antes de efectos sensibles.
- No presentes marcas como requisitos de conformidad UDF.

## Salida mínima

En análisis o planificación, entregá:

1. comprensión actual;
2. hechos, supuestos e incertidumbres;
3. perfil contextual y razones;
4. riesgos y trade-offs;
5. recomendación proporcional;
6. siguiente decisión requerida.

En aplicación, agregá archivos afectados, validaciones ejecutadas, resultados observados, rollback y limitaciones.
