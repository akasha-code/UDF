# 18) Mapeo de artefactos y dependencias (diagrama)

Este documento define **nombres para presentación** (inglés y español) para cada archivo convención del UDF y un **diagrama de dependencias entre artefactos** (no tareas): lectura **izquierda → derecha** por **fase** (SR-I … SR-X); dentro de cada columna el flujo típico es **de arriba abajo**.

**Convención de flechas:** A → B significa que *B se apoya en, deriva de o debe ser coherente con* A. Los ciclos de refinamiento (p. ej. prototipo que motiva nueva versión del charter) no se muestran para mantener el gráfico legible.

---

## Mapeo archivo → nombre para presentación

### Por fase (entregables principales)

| Archivo / ruta | Nombre (EN) | Nombre (ES) |
| ---------------- | ------------- | ------------- |
| `charter.md` | Project Charter | Charter del proyecto / Acta de constitución |
| `domain-model.puml` | Domain Model | Modelo de dominio |
| `use-cases/` | Use Cases | Casos de uso |
| `user-stories/` | User Stories | Historias de usuario |
| `prototype/` | UI Prototype | Prototipo de interfaz |
| `story-maps.md` | Story Map | Mapa de historias |
| `robustness.puml` | Robustness Diagrams | Diagramas de robustez |
| `class-diagram.puml` | Class Diagram | Diagrama de clases |
| `project_plan.md` | Project Plan | Plan de proyecto |
| `traceability_matrix.csv` | Traceability Matrix | Matriz de trazabilidad |
| `sequence.puml` | Sequence Diagrams | Diagramas de secuencia |
| `tests.csv` | Test Case Register | Registro de casos de prueba |
| `adr_<id>.md` | Architecture Decision Record (ADR) | Registro de decisiones de arquitectura (ADR) |
| `technical_health_report.md` | Technical Health Report | Informe de salud técnica |
| `validation_manifest.yaml` | Validation Manifest | Manifiesto de validación |
| `cutover_plan.md` | Cutover Plan | Plan de corte / puesta en marcha |
| `qa_evidence/` | QA Evidence Package | Evidencias de QA |
| `uat_signoff.pdf` | UAT Sign-off | Acta de aceptación de usuario (UAT) |
| `business_validation_report.md` | Business Validation Report | Informe de validación de negocio |
| `deployment_log.md` | Deployment Log | Registro de despliegues |
| `monitoring_dashboard.yaml` | Monitoring Configuration | Configuración de monitoreo / dashboards |
| `runbook.md` | Runbook | Manual operativo (runbook) |
| `ownership_transfer.md` | Ownership Transfer | Transferencia de responsabilidad operativa |
| `lessons_learned.md` | Lessons Learned | Lecciones aprendidas |
| `benefit_realization_plan.md` | Benefits Realization Plan | Plan de realización de beneficios |
| `project_closure_report.md` | Project Closure Report | Informe de cierre del proyecto |

### Gobierno y calidad (transversales)

| Archivo / ruta | Nombre (EN) | Nombre (ES) |
| ---------------- | ------------- | ------------- |
| `quality_charter.md` | Quality Charter | Carta de calidad |
| `architecture_governance_matrix.md` | Architecture Governance Matrix | Matriz de gobierno arquitectónico |
| `stage_review_board.md` | Stage Review Records | Actas de Stage Reviews |
| `risk_register.csv` | Risk Register | Registro de riesgos |
| `stakeholder_register.csv` | Stakeholder Register | Registro de partes interesadas |
| `status_report.md` | Status Report | Informe de estado |
| `executive_summary.md` | Executive Summary | Resumen ejecutivo |

### Testing (estrategia y políticas)

| Archivo / ruta | Nombre (EN) | Nombre (ES) |
| ---------------- | ------------- | ------------- |
| `test_strategy.yaml` | Test Strategy | Estrategia de pruebas |
| `test_matrix.csv` | Test Matrix | Matriz de pruebas |
| `qa_gate_policy.md` | QA Gate Policy | Política de gates de QA |
| `test_catalog.md` | Test Techniques Catalog | Catálogo de técnicas de prueba |

### Aprendizaje

| Archivo / ruta | Nombre (EN) | Nombre (ES) |
| ---------------- | ------------- | ------------- |
| `learning/<fecha>-<tema>.md` | Learning Log Entry | Entrada del ciclo de aprendizaje |
| `knowledge_base/` | Knowledge Base | Base de conocimiento |
| `tech_talks/` | Tech Talks | Charlas técnicas |

---

## Diagrama de dependencias (artefactos por fase)

Los nodos muestran **nombre en inglés** (presentación) y **archivo** en la segunda línea. Las aristas **punteadas** conectan fases con dependencias que cruzan el límite de la fase anterior.

```mermaid
flowchart LR
  subgraph SR_I["SR-I · Initiation"]
    direction TB
    I_ch["Project Charter<br/>charter.md"]
    I_st["Stakeholder Register<br/>stakeholder_register.csv"]
    I_rk["Risk Register<br/>risk_register.csv"]
    I_dm["Domain Model<br/>domain-model.puml"]
    I_us["User Stories<br/>user-stories/"]
    I_uc["Use Cases<br/>use-cases/"]
    I_pr["UI Prototype<br/>prototype/"]
    I_ch --> I_st
    I_ch --> I_rk
    I_ch --> I_dm
    I_ch --> I_us
    I_ch --> I_uc
    I_dm --> I_us
    I_dm --> I_uc
    I_us --> I_pr
    I_uc --> I_pr
  end

  subgraph SR_C["SR-C · Concept & Planning"]
    direction TB
    C_qc["Quality Charter<br/>quality_charter.md"]
    C_ts["Test Strategy<br/>test_strategy.yaml"]
    C_tm["Test Matrix<br/>test_matrix.csv"]
    C_sm["Story Map<br/>story-maps.md"]
    C_rb["Robustness Diagrams<br/>robustness.puml"]
    C_cl["Class Diagram<br/>class-diagram.puml"]
    C_pp["Project Plan<br/>project_plan.md"]
    C_tr["Traceability Matrix<br/>traceability_matrix.csv"]
    C_qc --> C_ts
    C_ts --> C_tm
    C_sm --> C_rb
    C_rb --> C_cl
    C_cl --> C_pp
    C_cl --> C_tr
    C_rb --> C_tr
    I_us -.-> C_sm
    I_uc -.-> C_rb
    I_dm -.-> C_rb
  end

  subgraph SR_E["SR-E · Build"]
    direction TB
    E_ad["Architecture Decision Record<br/>adr_*.md"]
    E_sq["Sequence Diagrams<br/>sequence.puml"]
    E_tc["Test Case Register<br/>tests.csv"]
    E_vm["Validation Manifest<br/>validation_manifest.yaml"]
    E_th["Technical Health Report<br/>technical_health_report.md"]
    C_cl --> E_ad
    C_rb --> E_sq
    C_cl --> E_sq
    E_ad --> E_sq
    C_tr --> E_tc
    C_tm --> E_tc
    I_us --> E_tc
    E_sq --> E_tc
    C_ts --> E_vm
    C_qc --> E_vm
    E_tc --> E_vm
    E_tc --> E_th
  end

  subgraph SR_B["SR-B · Business validation"]
    direction TB
    B_co["Cutover Plan<br/>cutover_plan.md"]
    B_qa["QA Evidence<br/>qa_evidence/"]
    B_ua["UAT Sign-off<br/>uat_signoff.pdf"]
    B_bv["Business Validation Report<br/>business_validation_report.md"]
    C_pp --> B_co
    E_ad --> B_co
    E_tc --> B_qa
    I_us --> B_ua
    B_qa --> B_ua
    B_ua --> B_bv
    B_qa --> B_bv
  end

  subgraph SR_O["SR-O · Operation"]
    direction TB
    O_dl["Deployment Log<br/>deployment_log.md"]
    O_md["Monitoring Configuration<br/>monitoring_dashboard.yaml"]
    O_rb["Runbook<br/>runbook.md"]
    O_ow["Ownership Transfer<br/>ownership_transfer.md"]
    B_co --> O_dl
    O_dl --> O_rb
    E_sq --> O_rb
    E_ad --> O_rb
    E_ad --> O_md
    O_rb --> O_ow
    O_md --> O_ow
  end

  subgraph SR_X["SR-X · Closure"]
    direction TB
    X_ll["Lessons Learned<br/>lessons_learned.md"]
    X_br["Benefits Realization Plan<br/>benefit_realization_plan.md"]
    X_pc["Project Closure Report<br/>project_closure_report.md"]
    B_bv --> X_ll
    I_ch --> X_br
    O_dl --> X_br
    X_ll --> X_pc
    X_br --> X_pc
  end

  I_ch --> C_qc
  I_us --> C_qc
```

### Notas al diagrama

* **Actas de Stage Review** (`stage_review_board.md`), **informes de estado** (`status_report.md`) y **resumen ejecutivo** (`executive_summary.md`) agregan evidencia de múltiples artefactos; no se enlazan desde cada nodo para no saturar el gráfico.
* **`validation_manifest.yaml`** aparece en Build y en la sección de testing del catálogo: en el diagrama es **un único artefacto**.
* **`architecture_governance_matrix.md`**, **`qa_gate_policy.md`**, **`test_catalog.md`** y aprendizaje (`learning/`, `knowledge_base/`, `tech_talks/`) pueden enlazarse en extensiones del mapa según PDI.

---

[← Anterior: Interoperabilidad y automatización](17-interoperabilidad-y-automatizacion.md) | [Volver a Artefactos](02-artifacts.md)
