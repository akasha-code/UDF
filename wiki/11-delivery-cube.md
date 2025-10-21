# 11) Delivery Cube (PDI–DSI–QEI) y Team Topology (TTI)

El **Delivery Cube** (también llamado **Delivery Polyhedron**) es el sistema de configuración del UDF que permite adaptar el framework a diferentes contextos, organizaciones y tipos de proyecto.

---

## Variables de configuración

El UDF se configura mediante cuatro variables principales:

| Variable | Nombre                       | Representa                     | Valores                           |
| -------- | ---------------------------- | ------------------------------ | --------------------------------- |
| **PDI**  | Project Depth Index          | Profundidad y trazabilidad     | XS, S, M, L, XL                   |
| **DSI**  | Delivery Structure Index     | Ritmo / estructura de entrega  | 1, 2, 3, 4, 5                     |
| **QEI**  | Quality Emphasis Index       | Énfasis en calidad / evidencia | Low, Medium, High                 |
| **TTI**  | Team Topology Index          | Topología de equipo            | Integrated, Dedicated, External   |

---

## Project Depth Index (PDI)

El PDI define el nivel de detalle, formalidad y trazabilidad requerido.

### Niveles PDI

| Level | Descripción                              | Contexto típico                    | Artefactos           |
| ----- | ---------------------------------------- | ---------------------------------- | -------------------- |
| **XS**| Mínimo viable                            | MVP, prototipos, experimentos      | ~5 artefactos core   |
| **S** | Ligero pero estructurado                 | Startups, equipos pequeños         | ~10 artefactos       |
| **M** | Estándar corporativo                     | Empresas medianas, producto        | ~15 artefactos       |
| **L** | Completo con governance                  | Empresas grandes, proyectos críticos| ~25 artefactos      |
| **XL**| Máximo, regulado, auditado               | GxP, aeroespacial, financiero      | Todos los artefactos |

### Ejemplo de artefactos por PDI

#### XS - Minimal
- `charter.md`
- `user-stories/`
- `tests.csv`
- `README.md`
- `deployment.md`

#### S - Light
- Todo XS +
- `domain-model.puml`
- `adr_*.md`
- `technical_health_report.md`
- `lessons_learned.md`

#### M - Standard
- Todo S +
- `robustness.puml`
- `sequence.puml`
- `cutover_plan.md`
- `quality_charter.md`
- `stage_review_board.md`
- `risk_register.csv`

#### L - Complete
- Todo M +
- `validation_manifest.yaml`
- `architecture_governance_matrix.md`
- `security_assessment.md`
- `runbook.md`
- `benefit_realization_plan.md`
- `stakeholder_register.csv`

#### XL - Regulated
- Todos los artefactos del UDF
- Trazabilidad V&V completa
- Validation protocols
- Audit trail completo
- Compliance documentation
- Formal sign-offs

---

## Delivery Structure Index (DSI)

El DSI define el ritmo, cadencia y estructura de entrega.

### Niveles DSI

| Level | Descripción                | Cadencia              | Metodología típica    |
| ----- | -------------------------- | --------------------- | --------------------- |
| **1** | Secuencial, waterfall      | Una entrega al final  | V-Model, PRINCE2      |
| **2** | Semi-iterativo             | Entregas cada 3 meses | Incremental           |
| **3** | Iterativo estándar         | Sprints 2-4 semanas   | Scrum, Agile          |
| **4** | Continuo, alta frecuencia  | Daily/weekly deploys  | Kanban, DevOps        |
| **5** | Continuous deployment      | Multiple deploys/day  | CD, Trunk-based       |

### Impacto del DSI

| Aspecto            | DSI 1-2              | DSI 3                | DSI 4-5              |
| ------------------ | -------------------- | -------------------- | -------------------- |
| **Planning**       | Upfront completo     | Sprint planning      | Just-in-time         |
| **Reviews**        | Al final de fase     | Sprint review        | Continuous feedback  |
| **Testing**        | Al final, formal     | Cada sprint          | Continuous testing   |
| **Deployment**     | Big bang             | Iterativo            | Continuous           |
| **Documentation**  | Formal, completa     | Just enough          | Living docs          |

---

## Quality Emphasis Index (QEI)

El QEI determina el nivel de énfasis en calidad, testing y evidencia.

### Niveles QEI

| Level      | Coverage | Testing Types                          | Evidence              |
| ---------- | -------- | -------------------------------------- | --------------------- |
| **Low**    | 60%      | Unit, Smoke, Exploratory               | Basic test reports    |
| **Medium** | 75%      | + Integration, Regression, Security    | Test matrix, metrics  |
| **High**   | 85%+     | + Performance, Validation, Compliance  | Full audit trail      |

### Configuración por QEI

```yaml
# Low QEI
quality:
  unit_tests: required
  integration_tests: recommended
  coverage_threshold: 60%
  static_analysis: basic
  security_scan: basic

# Medium QEI
quality:
  unit_tests: required
  integration_tests: required
  e2e_tests: recommended
  coverage_threshold: 75%
  static_analysis: standard
  security_scan: comprehensive
  performance_tests: basic

# High QEI
quality:
  unit_tests: required
  integration_tests: required
  e2e_tests: required
  performance_tests: required
  security_tests: required
  compliance_tests: required
  coverage_threshold: 85%
  static_analysis: strict
  validation_protocol: formal
  audit_trail: complete
```

---

## Team Topology Index (TTI)

El TTI define la estructura y modelo de responsabilidad del equipo.

### Topologías

#### Integrated Ownership
**Descripción:** "You build it, you run it"

**Características:**
- Mismo equipo desarrolla, despliega y opera
- DevOps completo
- Feedback loop directo
- Alta autonomía

**Ventajas:**
- Mínima fricción
- Rápida respuesta
- Alta calidad (ownership)

**Desventajas:**
- Requiere habilidades amplias
- On-call burden en el equipo

**Mejor para:** Startups, equipos producto, cloud-native

#### Dedicated Support
**Descripción:** Equipo de desarrollo entrega a equipo de operaciones

**Características:**
- Separación dev/ops
- Handover formal
- SLAs entre equipos
- Especialización

**Ventajas:**
- Especialización clara
- Carga operativa distribuida
- Soporte 24/7 factible

**Desventajas:**
- Fricción en handover
- Feedback loop más lento
- Posible blame game

**Mejor para:** Empresas medianas/grandes, sistemas legacy

#### External Delivery
**Descripción:** Vendor/consultora entrega a cliente

**Características:**
- Relación contractual
- Entregables formales
- Transferencia de conocimiento
- Warranty period

**Ventajas:**
- Expertise externo
- Flexibilidad de capacidad
- Costo predecible

**Desventajas:**
- Mayor overhead documental
- Riesgo de vendor lock-in
- Knowledge transfer crítico

**Mejor para:** Proyectos específicos, capacidad temporal

---

## Configuración del Delivery Cube

### Archivo de configuración

```yaml
# project_config.yaml

project:
  name: "MyProject"
  code: "PRJ-001"
  
delivery_cube:
  pdi: M
  dsi: 3
  qei: medium
  tti: integrated

artifacts:
  auto_enable: true
  enabled:
    # PDI M artifacts
    - charter.md
    - domain-model.puml
    - user-stories/
    - robustness.puml
    - sequence.puml
    - adr/
    - tests.csv
    - cutover_plan.md
    - technical_health_report.md
    - quality_charter.md
    - stage_review_board.md
    - lessons_learned.md

phases:
  initiation:
    duration: 2_weeks
    reviews: [SR-I]
    
  planning:
    duration: 4_weeks
    reviews: [SR-C]
    
  build:
    duration: 12_weeks
    sprints: 6
    sprint_duration: 2_weeks
    reviews: [SR-E]
    
  validation:
    duration: 2_weeks
    reviews: [SR-B]
    
  operation:
    duration: 2_weeks
    reviews: [SR-O]
    
  closure:
    duration: 1_week
    reviews: [SR-X]

testing:
  strategy: agile
  automation_target: 80%
  frameworks:
    unit: jest
    integration: testcontainers
    e2e: playwright
  thresholds:
    unit_coverage: 75%
    integration_coverage: 70%
    e2e_coverage: 60%

ci_cd:
  platform: github_actions
  pipeline:
    - lint
    - unit_tests
    - integration_tests
    - static_analysis
    - security_scan
    - build
    - deploy_staging
    - e2e_tests
    - deploy_production

governance:
  stage_reviews: formal
  change_control: ccb_required
  architecture_review: required
  security_review: required
```

---

## Escenarios de configuración

### Escenario 1: Startup MVP
```yaml
delivery_cube:
  pdi: XS
  dsi: 5
  qei: low
  tti: integrated

context: "Move fast, iterate, learn"
focus: "Speed to market, user validation"
```

### Escenario 2: Producto Enterprise
```yaml
delivery_cube:
  pdi: L
  dsi: 3
  qei: high
  tti: dedicated

context: "Corporate product, multiple teams"
focus: "Quality, governance, stability"
```

### Escenario 3: Proyecto Regulado
```yaml
delivery_cube:
  pdi: XL
  dsi: 1
  qei: high
  tti: external

context: "GxP, aerospace, medical device"
focus: "Compliance, traceability, validation"
```

### Escenario 4: Transformación Digital
```yaml
delivery_cube:
  pdi: M
  dsi: 3
  qei: medium
  tti: integrated

context: "Modernization, agile adoption"
focus: "Balance speed and control"
```

---

## Matriz de combinaciones

| PDI | DSI | QEI    | TTI       | Perfil típico                    |
| --- | --- | ------ | --------- | -------------------------------- |
| XS  | 5   | Low    | Integrated| Startup experimental             |
| S   | 4   | Medium | Integrated| Producto ágil pequeño            |
| M   | 3   | Medium | Integrated| Producto corporativo             |
| M   | 3   | High   | Dedicated | Enterprise aplicación crítica    |
| L   | 2   | High   | Dedicated | Proyecto estratégico grande      |
| L   | 1   | High   | External  | Outsourcing grande               |
| XL  | 1   | High   | External  | Proyecto regulado formal         |

---

## Delivery Polyhedron Visualization

```
           PDI (Depth)
              ▲
              │ XL
              │  │ L
              │  │  │ M
              │  │  │  │ S
              │  │  │  │  │ XS
              └──┴──┴──┴──┴─────► DSI (Cadence)
             ╱              1→5
            ╱
           ╱ TTI (Topology)
          ╱  Integrated/Dedicated/External
         ▼
      QEI (Quality)
      Low/Medium/High
```

Cada proyecto se posiciona en este espacio multidimensional, determinando su configuración específica de artefactos, procesos y controles.

---

## Ajuste y evolución

El Delivery Cube **no es estático**:

* Proyectos pueden evolucionar (ej: XS → S → M)
* Contexto cambia (startup → scale-up → enterprise)
* Aprendizajes ajustan configuración
* Madurez organizacional permite cambios

### Ejemplo de evolución

```yaml
# Phase 1: MVP
pdi: XS
dsi: 5
qei: low

# Phase 2: Product-Market Fit
pdi: S
dsi: 4
qei: medium

# Phase 3: Scale
pdi: M
dsi: 3
qei: medium

# Phase 4: Enterprise
pdi: L
dsi: 3
qei: high
```

---

[← Anterior: Learning Loop](10-learning-loop.md) | [Siguiente: Governance & Learning →](12-governance-learning.md)
