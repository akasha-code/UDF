# 17) Núcleo, extensiones e interoperabilidad con automatización

Este documento define **cómo adoptar el UDF sin cargar todo el marco**, qué tratar como **extensión opcional** (capa tipo PMO) y un **perfil agent-ready**: contratos, estados de artefacto, capacidades y gates verificables para integrar orquestadores, pipelines o agentes **sin sustituir** roles humanos ni Stage Reviews donde el contexto los exija.

**Plantillas en el repositorio:** [templates/automation/](https://github.com/akasha-code/UDF/tree/main/templates/automation) (JSON Schema de handoff, ejemplos YAML de manifiesto y checks de gate).

---

## Parte A — Modo de adopción: núcleo vs extensiones

### A.1 Núcleo (recomendado para PDI XS–S)

Conjunto mínimo alineado con [Delivery Cube (PDI–DSI–QEI–TTI)](11-delivery-cube.md):

| Elemento | Descripción |
| -------- | ----------- |
| Fases y Stage Reviews | Avance por fase con decisión Go/No-Go documentada |
| Artefactos mínimos por fase | Según [Artefactos principales](02-artifacts.md) y PDI |
| Evidencia trazable | Lo producido es verificable (tests, firmas, enlaces) |
| Learning loop | Captura de aprendizajes ligada al cierre o retrospectivas |

El **Quick Start** del README del repo (charter, historias, tests, THI, stage review) encaja en este núcleo.

### A.2 Extensiones (opt-in)

Activar solo si el **contexto** (compliance, multi-proyecto, contrato, auditoría) lo exige:

| Extensión | Cuándo considerarla |
| --------- | ------------------- |
| Portfolio y planificación densa | Multi-proyecto, OKRs/roadmaps corporativos — ver [09-portfolio](09-portfolio.md) |
| Baseline financiero / presupuesto formal | Proyectos con control económico estricto |
| Comités tipo CCB, cambios formales multi-nivel | Regulación o gobierno centralizado |
| RACI y documentación PMO al máximo | Equipos grandes o auditoría externa |

Estas piezas **compatibilizan** con PMBOK, PRINCE2 o SAFe; no son obligatorias para usar el UDF en equipos pequeños o productos iterativos.

---

## Parte B — Perfil agent-ready (interoperabilidad)

### B.1 Definición

Un proyecto o repositorio es **agent-ready** respecto del UDF cuando:

1. Los **handoffs** entre actores (humanos o automatizados) siguen un **contrato** con versión de esquema (`schema_version`).
2. Los **artefactos** o paquetes de trabajo tienen **estado** explícito y reglas de promoción.
3. Las **capacidades** (qué puede leer/escribir/aprobar cada actor) están definidas, incluidas **prohibiciones explícitas** (`must_not_touch`).
4. Los **gates** pueden expresarse como **lista de checks** (automáticos y/o manuales).
5. La **provenance** mínima permite auditar origen de cambios (útil para ADRs y [Learning Loop](10-learning-loop.md)).

Esto **complementa** [Gobierno](04-governance.md) y [Roles](05-roles-interactions.md); no reemplaza la responsabilidad humana donde corresponda.

### B.2 Ciclo de vida de artefacto (estados)

Estados sugeridos (etiquetas en inglés habituales para herramientas y esquemas):

| Estado | Significado |
| ------ | ----------- |
| `draft` | Trabajo en curso; no es verdad acordada del proyecto. |
| `under_review` | Pendiente de revisión o Stage Review; candidato a promover. |
| `accepted` | Aprobado según criterios del gate; forma parte de la línea base acordada. |

Ejemplo de manifiesto por paquete: [artifact-manifest.example.yaml](https://github.com/akasha-code/UDF/blob/main/templates/automation/artifact-manifest.example.yaml).

**Transiciones:** solo actores con capacidad `can_approve` (o política equivalente) pasan a `accepted`. Pasar a `under_review` puede requerir `can_request_review` o el flujo de PR/revisión del equipo. Las reglas concretas se documentan en el proyecto y deben alinearse con los Stage Reviews de la fase activa.

### B.3 Contrato de handoff

Un **handoff** es un mensaje o registro que transfiere trabajo entre emisor y receptor. Campos mínimos recomendados:

| Campo | Descripción |
| ----- | ----------- |
| `schema_version` | Versión del contrato (p. ej. `1.0.0`) para evolucionar sin romper consumidores. |
| `correlation_id` | Id único del intento (útil para idempotencia y trazas). |
| `from` / `to` | Identificador del emisor y del receptor (rol, agente, servicio). |
| `artifact_refs` | Referencias a rutas, commits o URIs de artefactos incluidos. |
| `evidence_refs` | Enlaces a pruebas, métricas o evidencia de cumplimiento. |
| `open_risks` | Riesgos o incertidumbres que el receptor debe considerar. |
| `requested_decision` | Decisión explícita pedida (Go/No-Go, alcance, alternativa). |

**Idempotencia y reintentos:** el orquestador debe poder detectar reenvíos del mismo `correlation_id` y no aplicar dos veces efectos secundarios (por ejemplo, doble promoción a `accepted`). Las políticas concretas son responsabilidad de la implementación.

**Esquema JSON:** ver [handoff.schema.json](https://github.com/akasha-code/UDF/blob/main/templates/automation/handoff.schema.json).

### B.4 Matriz de capacidades por actor

Complemento opcional al RACI cuando hay automatización o muchos especialistas:

| Capacidad | Significado |
| --------- | ----------- |
| `can_write` | Ámbitos o prefijos donde el actor puede crear o modificar contenido. |
| `can_approve` | Puede aprobar transiciones de estado o gates que lo requieran. |
| `can_request_review` | Puede marcar trabajo como listo para revisión (`under_review`). |
| `must_not_touch` | Lista explícita de rutas, secretos, entornos o tipos de recurso que el actor **no debe** modificar (ni leer, si la política lo exige), aunque tenga acceso técnico. |

La denegación explícita reduce ambigüedad frente a “no listado en `can_write`”.

### B.5 Gates como lista verificable

Los criterios Go/No-Go de [Stage Reviews](04-governance.md) pueden desglosarse en **checks**:

- **Automáticos:** linters, tests, validación de esquema YAML, presencia de campos obligatorios en manifiesto.
- **Manuales:** revisión de negocio, seguridad, firmas.

Ejemplo de estructura: [gate-checks.example.yaml](https://github.com/akasha-code/UDF/blob/main/templates/automation/gate-checks.example.yaml).

### B.6 Provenance (trazabilidad del origen)

Campos sugeridos al registrar producción o cambio de artefactos:

| Campo | Uso |
| ----- | --- |
| `run_id` | Identificador de ejecución del pipeline u orquestador. |
| `actor_id` | Humano, agente o servicio responsable del cambio. |
| `tool_refs` | Herramientas o llamadas relevantes (sin secretos). |
| `commit_ref` | SHA o enlace al commit cuando aplique. |

Esto refuerza trazabilidad hacia [ADRs](07-architecture.md) y el learning loop.

### B.7 Mapeo fase UDF — promoción y foco

| Fase UDF | Foco típico de handoff / gate | Notas |
| -------- | ----------------------------- | ----- |
| Initiation (SR-I) | Visión, alcance, riesgos iniciales | `accepted` en charter/riesgos según política |
| Planning (SR-C) | Diseño, plan, trazabilidad requisitos | Alineación con definición de hecho por disciplina |
| Build (SR-E) | Implementación, revisiones técnicas, THI | Gates de calidad de código y pruebas |
| Validation (SR-B) | Validación de negocio / UAT | Evidencia de prueba y sign-off |
| Operation (SR-O) | Despliegue, runbook, monitoreo | Readiness operativa |
| Closure (SR-X) | Lecciones aprendidas, cierre formal | Cierre de riesgos y aprendizajes |

---

## Navegación

- [Overview](00-overview.md)
- [Artefactos principales](02-artifacts.md)
- [Mapeo de artefactos y dependencias (diagrama)](18-artifact-map-and-dependencies.md)
- [Roles e interacciones](05-roles-interactions.md)
- [Plan de adopción](14-adoption-plan.md)
