# 5) Roles, Interacciones y Modelos de Responsabilidad

## 5.1 Propósito

Definir con claridad las responsabilidades, interacciones y dependencias entre los distintos roles que participan en el UDF, garantizando compatibilidad con marcos de trabajo como V-Model, Agile, DevOps, PRINCE2 y SAFe. El objetivo es que los equipos puedan adaptar el grado de estructura o autonomía sin perder trazabilidad ni responsabilidad.

---

## 5.2 Roles base y responsabilidades

Cada rol tiene un área de responsabilidad definida y una relación clara de autoridad y consulta (modelo RACI).

| Rol                         | Responsible                                                     | Accountable                                     | Consulted                         | Informed                         |
| --------------------------- | --------------------------------------------------------------- | ----------------------------------------------- | --------------------------------- | -------------------------------- |
| **PM / Delivery Lead**      | Coordinación general, seguimiento de entregables, Stage Reviews | Cumplimiento de plazos, presupuesto y alcance   | QA Lead, Architect, Product Owner | Stakeholders, Steering Committee |
| **Product Owner / UX Lead** | Historias de usuario, priorización, validación de negocio       | Valor entregado y satisfacción del cliente      | PM, Tech Lead                     | Stakeholders, QA                 |
| **Tech Lead / Architect**   | Diseño técnico, robustez, ADRs                                  | Integridad técnica y cumplimiento de estándares | PM, Dev Team, QA                  | Operations, Security             |
| **DevOps / Platform**       | Integración continua, infraestructura, monitoreo                | Estabilidad operativa y despliegues             | QA, Developers                    | PM, Operations                   |
| **Developers (FE/BE/FS)**   | Implementación, unit testing, code review                       | Cumplimiento de requisitos técnicos             | Tech Lead, QA                     | PM                               |
| **QA / Compliance**         | Planes y ejecución de prueba, QA gates, evidencias              | Garantía de calidad y conformidad               | Dev Team, PM                      | Stakeholders, Audit              |
| **Customer / Stakeholder**  | Feedback, UAT, demos                                            | Validación de valor                             | Product Owner, PM                 | Comité ejecutivo                 |

### Notas importantes

* **La representación puede delegarse**, pero la voz técnica o funcional nunca puede ser omitida.
* **La comunicación asincrónica** (repos, foros, SR logs) asegura continuidad.
* **La accountability es individual**, la responsabilidad puede ser compartida.

---

## 5.3 Interacciones según topología de equipo (TTI)

El Team Topology Index (TTI) define cómo se organizan y relacionan los equipos en el proyecto.

| Topología                | Dinámica                                                                                              | Responsabilidad compartida                                                      |
| ------------------------ | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| **Integrated Ownership** | El mismo equipo desarrolla, opera y da soporte. Se reduce la fricción entre desarrollo y operaciones. | QA, Dev y Ops comparten responsabilidad del Runbook y THI.                      |
| **Dedicated Support**    | Desarrollo entrega a un equipo de mantenimiento. Hay transferencia formal de conocimiento.            | QA valida el handover, Operations mantiene KPIs post-release.                   |
| **External Delivery**    | Consultoras o vendors entregan al cliente final.                                                      | PM asegura trazabilidad contractual y KT Plan. QA valida calidad y conformidad. |

### Influencia del TTI en Stage Reviews

* **Integrated:** Las decisiones son del equipo. SR aprobado por Tech Lead + PO.
* **Dedicated:** Requiere sign-off formal de equipo receptor en SR-O.
* **External:** Requiere aprobación contractual y validación del cliente.

---

## 5.4 Compatibilidad metodológica

El UDF se alinea con los principales marcos sin perder independencia conceptual.

| UDF Fase                       | V-Model                               | Agile / SAFe                     | PRINCE2 / PMBOK                         |
| ------------------------------ | ------------------------------------- | -------------------------------- | --------------------------------------- |
| **Initiation (SR-I)**          | User Requirements Specification (URS) | Epic Definition / Product Vision | Starting up / Business Case             |
| **Concept & Planning (SR-C)**  | System Design Specification (SDS)     | Sprint 0 / PI Planning           | Initiating / Planning                   |
| **Build (SR-E)**               | Implementation + Unit Testing         | Sprint Execution / Iteration     | Controlling / Managing Product Delivery |
| **Business Validation (SR-B)** | System & Acceptance Testing           | Sprint Review / PI System Demo   | Managing Stage Boundaries               |
| **Operation (SR-O)**           | Deployment & Qualification            | Release & Operate                | Managing Product Delivery               |
| **Closure (SR-X)**             | Validation Summary Report             | Inspect & Adapt / Retrospective  | Closing Stage / Lessons Learned         |

De este modo, el UDF puede implementarse como marco ágil, regulado o híbrido sin pérdida de trazabilidad ni consistencia documental.

---

## 5.5 Ejemplo operativo de V-Model dentro del UDF

En contextos regulados (GxP, aeroespacial, financiero), el UDF permite un flujo espejo tipo V-Model:

### Estructura del V-Model

```
URS ────────────────────────────────── Acceptance Test
 │                                            ▲
 │                                            │
SDS ─────────────────────────── System Test  │
 │                                      ▲     │
 │                                      │     │
Detail Design ──────── Integration Test│     │
 │                              ▲       │     │
 │                              │       │     │
Implementation ──── Unit Test ──┘       │     │
                                        │     │
                                        └─────┘
```

### Fases del V-Model en UDF

* **Descenso del V (Definición):**
  1. URS (User Requirements Specification) → `charter.md`, `use-cases/`
  2. SDS (System Design Specification) → `robustness.puml`, `class-diagram.puml`
  3. Detail Design → `sequence.puml`, `adr_*.md`
  4. Implementation → Código fuente

* **Ascenso del V (Verificación):**
  1. Unit Test → `tests.csv`, test automatizados
  2. Integration Test → `integration_plan.md`
  3. System Test → `system_test_plan.md`
  4. Acceptance Test → `uat_signoff.pdf`

### Trazabilidad bidireccional

Cada fase descendente se vincula con su espejo de validación en el `validation_manifest.yaml`:

```yaml
# validation_manifest.yaml - V-Model configuration
v_model:
  enabled: true
  traceability:
    - requirement_id: URS-001
      design_ref: SDS-001
      detail_design: SEQ-001
      implementation: src/module/feature.py
      unit_test: tests/unit/test_feature.py
      integration_test: tests/integration/test_module.py
      system_test: tests/system/test_workflow.py
      acceptance_test: uat/test_case_001.md
      
    - requirement_id: URS-002
      design_ref: SDS-002
      detail_design: SEQ-002
      implementation: src/module/another.py
      unit_test: tests/unit/test_another.py
      integration_test: tests/integration/test_integration.py
      system_test: tests/system/test_system.py
      acceptance_test: uat/test_case_002.md
```

### Artefactos involucrados

* `charter.md` - Charter del proyecto
* `requirements.yaml` - Especificación de requisitos (URS)
* `system_design.md` - Diseño del sistema (SDS)
* `implementation.md` - Documentación de implementación
* `unit_tests.csv` - Registro de pruebas unitarias
* `integration_plan.md` - Plan de integración
* `uat_signoff.pdf` - Aprobación de UAT

### Stage Reviews como checkpoints

Los Stage Reviews (SR-C, SR-E, SR-B) actúan como checkpoints de verificación del V:

* **SR-C:** Valida que el diseño cumple con los requisitos (URS ↔ SDS)
* **SR-E:** Valida que la implementación cumple con el diseño y tiene pruebas (Unit + Integration)
* **SR-B:** Valida que el sistema cumple con los requisitos (System + Acceptance)

Esto mantiene cumplimiento regulatorio y control de calidad sin sacrificar agilidad en los ciclos inferiores.

---

## 5.6 Interoperabilidad cultural

El nivel de documentación es exhaustivo por diseño, pero el grado de implementación depende del PDI/DSI/TTI.

### Configuración por contexto

| Contexto                  | PDI | DSI | QEI    | TTI        | Énfasis                          |
| ------------------------- | --- | --- | ------ | ---------- | -------------------------------- |
| Startup ágil              | XS  | 5   | Medium | Integrated | Velocidad, producto mínimo       |
| Empresa corporativa       | L   | 2   | High   | Dedicated  | Proceso, cumplimiento            |
| Proyecto regulado         | XL  | 1   | High   | External   | Trazabilidad, auditoría          |
| Transformación digital    | M   | 3   | Medium | Integrated | Balance agilidad-gobierno        |

### Principio de implementación progresiva

El framework puede ser aplicado en modo liviano o corporativo:

1. **Modo liviano (XS-S):**
   - Artefactos mínimos (charter, stories, tests)
   - SRs informales (reuniones + notas)
   - Automatización básica

2. **Modo estándar (M):**
   - Artefactos core completos
   - SRs formales con documentación
   - CI/CD con gates básicos

3. **Modo corporativo (L-XL):**
   - Todos los artefactos
   - SRs con comité de aprobación
   - Full compliance y auditoría

La pedagogía y simplificación visual (dashboards, checklists, asistentes IA) se aplican **después**, sin debilitar la estructura metodológica.

---

## 5.7 Matriz de decisiones por rol

| Decisión                        | PM | PO | Tech Lead | DevOps | Dev | QA | Stakeholder |
| ------------------------------- | -- | -- | --------- | ------ | --- | -- | ----------- |
| Aprobación de requisitos        | C  | A  | C         | I      | I   | C  | I           |
| Decisiones de arquitectura      | I  | C  | A         | C      | C   | I  | I           |
| Aprobación de cambios           | A  | C  | C         | I      | I   | C  | I           |
| Go/No-Go en Stage Review        | A  | C  | C         | C      | I   | C  | C           |
| Priorización de backlog         | C  | A  | C         | I      | C   | I  | C           |
| Aprobación de despliegue        | C  | C  | C         | A      | I   | C  | I           |
| Definición de casos de prueba   | I  | C  | C         | I      | C   | A  | C           |
| Aceptación de UAT               | I  | C  | I         | I      | I   | C  | A           |

**Leyenda:** R=Responsible, A=Accountable, C=Consulted, I=Informed

---

## 5.8 Comunicación y ceremonias

### Ceremonias por fase

| Fase       | Ceremonia                | Frecuencia      | Participantes             |
| ---------- | ------------------------ | --------------- | ------------------------- |
| Initiation | Kickoff Meeting          | Once            | All stakeholders          |
| Planning   | Planning Workshop        | Once per phase  | PM, PO, Tech Lead, Team   |
| Build      | Daily Standup            | Daily           | Dev Team, QA              |
| Build      | Sprint Review/Demo       | Per iteration   | Team, PO, Stakeholders    |
| Build      | Technical Review         | Weekly          | Tech Lead, Developers, QA |
| All        | Stage Review             | Per phase       | All stakeholders          |
| All        | Retrospective            | Per iteration   | Team                      |
| Closure    | Lessons Learned Session  | Once            | All stakeholders          |

### Canales de comunicación

| Tipo               | Canal                  | Audiencia                |
| ------------------ | ---------------------- | ------------------------ |
| Sincrónico formal  | Stage Reviews          | Stakeholders             |
| Sincrónico técnico | Technical Sync         | Team técnico             |
| Asincrónico        | Git commits/PRs        | Developers, QA           |
| Asincrónico        | Documentation (wiki)   | All                      |
| Dashboard          | Grafana/Project Board  | PM, Tech Lead, PO        |
| Reporting          | Status Reports         | Management, Sponsors     |

---

> **En síntesis:** el UDF define con precisión quién hace qué, cuándo y con qué nivel de evidencia, permitiendo coexistir prácticas Agile, V-Model y DevOps bajo un lenguaje común.

---

[← Anterior: Governance](04-governance.md) | [Siguiente: Quality & Testing →](06-quality-testing.md)
