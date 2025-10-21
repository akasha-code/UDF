# 2) Artefactos principales

El UDF define un conjunto de artefactos estándar que garantizan la trazabilidad, calidad y gobernanza del proyecto. Estos artefactos están disponibles como plantillas en formato Markdown, CSV o YAML para facilitar su adopción y versionado.

---

## Artefactos por fase

### Initiation (SR-I)
* **`charter.md`** - Documento fundacional del proyecto
* **`domain-model.puml`** - Modelo de dominio en PlantUML
* **`use-cases/`** - Directorio de casos de uso
* **`user-stories/`** - Directorio de historias de usuario
* **`prototype/`** - Prototipos de interfaz de usuario

### Concept & Planning (SR-C)
* **`robustness.puml`** - Diagramas de robustez
* **`story-maps.md`** - Story maps (si aplica Agile)
* **`class-diagram.puml`** - Diseño de clases
* **`project_plan.md`** - Plan detallado del proyecto
* **`traceability_matrix.csv`** - Matriz de trazabilidad

### Build (SR-E)
* **`sequence.puml`** - Diagramas de secuencia
* **`tests.csv`** - Registro de casos de prueba
* **`adr_<id>.md`** - Architecture Decision Records
* **`technical_health_report.md`** - Reporte de salud técnica
* **`validation_manifest.yaml`** - Configuración de validaciones

### Business Validation (SR-B)
* **`cutover_plan.md`** - Plan de transición a producción
* **`uat_signoff.pdf`** - Evidencias de UAT y aprobación
* **`qa_evidence/`** - Directorio de evidencias de QA
* **`business_validation_report.md`** - Reporte de validación de negocio

### Operation (SR-O)
* **`deployment_log.md`** - Log de despliegue
* **`runbook.md`** - Manual operativo
* **`monitoring_dashboard.yaml`** - Configuración de monitoreo
* **`ownership_transfer.md`** - Documento de transferencia

### Closure (SR-X)
* **`lessons_learned.md`** - Lecciones aprendidas
* **`benefit_realization_plan.md`** - Realización de beneficios
* **`project_closure_report.md`** - Reporte de cierre

---

## Artefactos de gobierno y calidad

Estos artefactos transversales aplican a lo largo del ciclo de vida:

* **`quality_charter.md`** - Carta de calidad del proyecto
* **`architecture_governance_matrix.md`** - Matriz de gobierno arquitectónico
* **`stage_review_board.md`** - Actas de Stage Reviews
* **`risk_register.csv`** - Registro de riesgos y oportunidades
* **`stakeholder_register.csv`** - Registro de stakeholders
* **`status_report.md`** - Reportes de estado periódicos
* **`executive_summary.md`** - Resumen ejecutivo

---

## Artefactos de testing

* **`test_strategy.yaml`** - Estrategia de pruebas
* **`test_matrix.csv`** - Matriz de pruebas
* **`validation_manifest.yaml`** - Manifiesto de validación
* **`qa_gate_policy.md`** - Políticas de aprobación
* **`test_catalog.md`** - Catálogo de técnicas de prueba

Ver [Unified Test Strategy](16-unified-test-strategy.md) para detalles completos.

---

## Artefactos de aprendizaje

* **`learning/<fecha>-<tema>.md`** - Entradas del Learning Loop
* **`knowledge_base/`** - Base de conocimiento del proyecto
* **`tech_talks/`** - Presentaciones técnicas

---

## Formatos estándar

| Formato      | Uso                                              |
| ------------ | ------------------------------------------------ |
| **Markdown** | Documentación narrativa y decisiones             |
| **YAML**     | Configuración, manifiestos, estrategias          |
| **CSV**      | Matrices, registros, datos tabulares             |
| **PlantUML** | Diagramas UML (dominio, clases, secuencia)       |
| **PDF**      | Evidencias formales, sign-offs, entregas oficiales |

---

## Versionado y control

* Todos los artefactos se gestionan bajo control de versión (Git)
* Los cambios formales requieren aprobación en Stage Reviews
* Las baselines se establecen en cada SR mediante tags de Git
* Los ADRs son inmutables una vez aprobados (nuevos ADRs superseden anteriores)

---

## Configuración por PDI

El nivel de profundidad del proyecto (PDI) determina qué artefactos son obligatorios:

| PDI Level | Artefactos obligatorios                                       |
| --------- | ------------------------------------------------------------- |
| **XS**    | charter.md, user-stories/, tests.csv                          |
| **S**     | + domain-model.puml, adr_*.md                                 |
| **M**     | + robustness.puml, sequence.puml, cutover_plan.md             |
| **L**     | + quality_charter.md, validation_manifest.yaml                |
| **XL**    | Todos los artefactos + auditoría completa + trazabilidad V&V |

---

## Ejemplo de configuración YAML

```yaml
# project_config.yaml
pdi: M
dsi: 3
qei: medium
tti: integrated

auto_enable:
  - charter.md
  - use-cases.md
  - robustness.puml
  - sequence.puml
  - tests.csv
  - cutover_plan.md
  - technical_health_report.md
  - stage_review_board.md
```

---

[← Anterior: Lifecycle Phases](01-lifecycle-phases.md) | [Siguiente: Technical Management →](03-technical-management.md)
