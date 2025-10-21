# 13) Testing, riesgo y madurez

El UDF adapta el nivel de testing, gestión de riesgos y procesos según la madurez organizacional y criticidad del proyecto.

---

## Testing proporcional

El nivel de testing es proporcional al **PDI** (profundidad) y **QEI** (énfasis en calidad):

### XS–S: Minimal Testing

**Contexto:** MVPs, prototipos, experimentos

**Enfoque:**
- Unit tests básicos (>60% coverage)
- Smoke tests manuales
- Exploratory testing ad-hoc

**Tools:**
- Jest/Pytest para unit tests
- Manual testing para critical paths

**Frequency:**
- Unit: cada commit
- Smoke: cada deploy
- Exploratory: semanal

---

### M: Standard Testing

**Contexto:** Productos corporativos, aplicaciones estándar

**Enfoque:**
- Unit tests completos (>75% coverage)
- Integration tests automatizados
- Regression suite básica
- Security scanning
- Basic performance tests

**Tools:**
- Jest/JUnit/Pytest para unit
- TestContainers para integration
- Playwright para E2E crítico
- SonarQube para static analysis
- Snyk para security

**Frequency:**
- Unit: cada commit
- Integration: cada PR
- Regression: cada sprint
- Security: diario
- Performance: semanal

---

### L–XL: Comprehensive Testing

**Contexto:** Sistemas críticos, regulados, alta escala

**Enfoque:**
- Unit tests exhaustivos (>85% coverage)
- Integration tests completos
- System tests automatizados
- Full regression suite
- Performance & load testing
- Security penetration testing
- Compliance validation
- Validation protocols (si regulado)

**Tools:**
- Full test automation stack
- Performance tools (k6, JMeter)
- Security tools (penetration, fuzzing)
- Compliance tools (validation frameworks)

**Frequency:**
- Unit: cada commit
- Integration: cada PR
- System: cada build
- Regression: cada release
- Performance: cada release
- Security: continuo + quarterly audit
- Compliance: formal validation cycle

---

## Gestión de riesgos proporcional

### XS–S: Lightweight Risk Management

**Herramienta:** Tablero Kanban de issues con labels

```
Issues Board:
- Label: risk-high
- Label: risk-medium
- Label: risk-low
```

**Proceso:**
- Identificar riesgos en planning
- Tracking como issues en board
- Review semanal en standup
- Mitigaciones como tasks

**Documentación:**
```markdown
# Risks (in README or Wiki)

## High Priority
- **R01:** Vendor delay - Mitigation: backup vendor identified

## Medium Priority
- **R02:** Skill gap in React - Mitigation: training scheduled
```

---

### M: Standard Risk Management

**Herramienta:** Risk Register (CSV/Excel)

```csv
ID,Description,Probability,Impact,Score,Status,Mitigation,Owner,Review_Date
R01,Vendor delivery delay,High,High,9,Active,Backup vendor contract,PM,2025-11-15
R02,Resource availability,Medium,Medium,4,Mitigated,Cross-training complete,PM,2025-11-01
R03,Technology complexity,Low,High,3,Monitoring,POC successful,Tech Lead,2025-11-20
```

**Proceso:**
- Risk identification workshop
- Matriz probabilidad/impacto
- Score = Probability × Impact
- Review semanal en team meeting
- Escalación de high risks a PM
- Update en Stage Reviews

---

### L–XL: Formal Risk Management

**Herramienta:** Risk & Opportunity Register + Risk Dashboard

```yaml
# risk_register.yaml
risks:
  - id: R001
    title: "Integration complexity with legacy system"
    category: technical
    probability: high
    impact: high
    score: 9
    status: active
    
    mitigation:
      strategy: reduce
      actions:
        - description: "POC with legacy API"
          owner: "Tech Lead"
          due: "2025-11-10"
          status: in_progress
          
        - description: "Adapter pattern implementation"
          owner: "Senior Dev"
          due: "2025-11-15"
          status: planned
    
    contingency:
      plan: "Implement temporary manual process"
      trigger: "POC fails or exceeds 2 weeks"
      owner: "PM"
    
    owner: "Tech Lead"
    review_frequency: weekly
    last_review: "2025-10-20"
    next_review: "2025-10-27"
    
  - id: O001
    title: "Early delivery may enable Q4 revenue"
    type: opportunity
    probability: medium
    benefit: high
    exploitation:
      actions:
        - "Prioritize critical features"
        - "Add resources if available"
```

**Proceso:**
- Formal risk identification (brainstorming, Delphi, SWOT)
- Quantitative risk analysis (Monte Carlo para schedule)
- Risk response planning (Avoid, Transfer, Mitigate, Accept)
- Risk monitoring y control continuo
- Dashboard de riesgos en tiempo real
- Escalación formal a Steering Committee
- Risks & Opportunities en todos los SR

---

## Madurez organizacional

El UDF mide madurez en cinco pilares:

### 1. Governance Maturity

| Level | Descripción                                      | Indicadores                          |
| ----- | ------------------------------------------------ | ------------------------------------ |
| **1** | Ad-hoc, reactivo                                 | No hay Stage Reviews formales        |
| **2** | Repetible, básico                                | SRs informales, inconsistentes       |
| **3** | Definido, estándar                               | SRs formales, documentados           |
| **4** | Gestionado, medido                               | SRs con métricas, decisiones basadas en datos |
| **5** | Optimizado, continuo                             | SRs automatizados, mejora continua   |

### 2. Technical Maturity

| Level | Descripción                                      | Indicadores                          |
| ----- | ------------------------------------------------ | ------------------------------------ |
| **1** | Código sin tests, no CI/CD                       | Manual builds, no automation         |
| **2** | Tests básicos, CI manual                         | Some unit tests, manual deployment   |
| **3** | CI/CD básico, testing estándar                   | Automated builds, basic test suite   |
| **4** | CI/CD avanzado, testing completo                 | Full automation, high coverage       |
| **5** | Continuous deployment, testing exhaustivo        | Zero-touch deployment, >85% coverage |

### 3. Quality Maturity

| Level | Descripción                                      | Indicadores                          |
| ----- | ------------------------------------------------ | ------------------------------------ |
| **1** | Testing manual, ad-hoc                           | No quality metrics                   |
| **2** | Testing básico, inconsistente                    | Basic metrics, reactive QA           |
| **3** | Testing automatizado, quality gates              | Standard metrics, proactive QA       |
| **4** | Testing exhaustivo, calidad medida               | Comprehensive metrics, predictive QA |
| **5** | Testing continuo, calidad optimizada             | Real-time quality, automated remediation |

### 4. Learning Maturity

| Level | Descripción                                      | Indicadores                          |
| ----- | ------------------------------------------------ | ------------------------------------ |
| **1** | No hay captura de aprendizajes                   | No retrospectives, no lessons learned|
| **2** | Aprendizajes ocasionales, no documentados        | Informal retros, no follow-up        |
| **3** | Aprendizajes documentados, no aplicados          | Documented but not actioned          |
| **4** | Aprendizajes aplicados, mejora medida            | Actions tracked, improvements measured|
| **5** | Organización que aprende, mejora continua        | Learning culture, continuous improvement|

### 5. Value Maturity

| Level | Descripción                                      | Indicadores                          |
| ----- | ------------------------------------------------ | ------------------------------------ |
| **1** | No hay métricas de valor                         | No business metrics tracked          |
| **2** | Métricas básicas, no accionables                 | Vanity metrics only                  |
| **3** | Métricas de valor, tracking básico               | Business metrics tracked             |
| **4** | Métricas vinculadas a decisiones                 | Data-driven product decisions        |
| **5** | Optimización continua de valor                   | Continuous experimentation, optimization|

---

## Maturity Assessment

### Assessment Template

```markdown
# UDF Maturity Assessment

**Organization:** [Name]
**Date:** [YYYY-MM-DD]
**Assessor:** [Name]

## Scores by Pillar

| Pillar       | Level | Score | Target | Gap |
| ------------ | ----- | ----- | ------ | --- |
| Governance   | 3     | 65%   | 80%    | -15%|
| Technical    | 4     | 78%   | 85%    | -7% |
| Quality      | 3     | 70%   | 80%    | -10%|
| Learning     | 2     | 45%   | 70%    | -25%|
| Value        | 3     | 68%   | 75%    | -7% |
| **Overall**  | **3** | **65%**|**78%**|**-13%**|

## Strengths
1. Strong technical practices (CI/CD, automation)
2. Good quality metrics and gates
3. Defined governance process

## Gaps
1. Learning culture weak (no structured retrospectives)
2. Value metrics not consistently tracked
3. Governance not yet optimized

## Recommendations

### Immediate (0-3 months)
- [ ] Implement structured retrospectives with action tracking
- [ ] Define and track core value metrics (NPS, conversion, etc.)
- [ ] Automate Stage Review report generation

### Short-term (3-6 months)
- [ ] Establish learning repository and knowledge sharing practices
- [ ] Integrate value metrics into product decisions
- [ ] Implement continuous improvement process

### Long-term (6-12 months)
- [ ] Build learning culture with regular tech talks and workshops
- [ ] Establish experimentation framework for value optimization
- [ ] Fully automate governance reporting and decision support
```

---

## Roadmap to Maturity

### Level 2 → 3 (Defined)

**Focus:** Standardization and consistency

**Actions:**
- Document all processes
- Create standard templates
- Implement basic automation
- Establish quality baselines
- Regular Stage Reviews

**Timeline:** 3-6 months

---

### Level 3 → 4 (Managed)

**Focus:** Measurement and data-driven decisions

**Actions:**
- Implement comprehensive metrics
- Automate reporting and dashboards
- Data-driven decision making
- Predictive analytics (risk, quality)
- Continuous learning practices

**Timeline:** 6-12 months

---

### Level 4 → 5 (Optimizing)

**Focus:** Continuous optimization

**Actions:**
- AI/ML for predictive insights
- Fully automated pipelines
- Real-time optimization
- Organization-wide learning culture
- Innovation and experimentation framework

**Timeline:** 12-24 months

---

## Risk Appetite

Different project types have different risk appetites:

| Project Type      | Risk Appetite | Testing Level | PDI | QEI  |
| ----------------- | ------------- | ------------- | --- | ---- |
| MVP/Experiment    | High          | Minimal       | XS  | Low  |
| Internal Tool     | Medium        | Standard      | S   | Med  |
| Customer Product  | Low           | Comprehensive | M   | Med  |
| Critical System   | Very Low      | Exhaustive    | L   | High |
| Regulated System  | Zero          | Validation    | XL  | High |

---

## Testing Investment vs Risk

```
Testing Investment
        ▲
    XL  │         ◆ Regulated
        │
    L   │       ◆ Critical
        │
    M   │     ◆ Standard
        │
    S   │   ◆ Basic
        │
    XS  │ ◆ Minimal
        └─────────────────────► Risk/Criticality
         Low  Med  High  Critical
```

El UDF permite encontrar el balance óptimo entre inversión en testing/proceso y el nivel de riesgo aceptable para cada contexto.

---

## Quality Debt vs Technical Debt

**Technical Debt:** Compromises en código y arquitectura

**Quality Debt:** Compromises en testing y evidencia

Ambos deben gestionarse activamente:

```yaml
# debt_management.yaml

technical_debt:
  current: "3.2% of codebase"
  target: "< 5%"
  status: acceptable
  items:
    - description: "Legacy authentication module"
      effort: 8_days
      priority: medium
      
quality_debt:
  current: "15% of code without tests"
  target: "< 10%"
  status: needs_attention
  items:
    - description: "Payment processing not fully tested"
      effort: 5_days
      priority: high
```

---

[← Anterior: Governance & Learning](12-governance-learning.md) | [Siguiente: Adoption Plan →](14-adoption-plan.md)
