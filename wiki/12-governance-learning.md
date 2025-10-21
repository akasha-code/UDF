# 12) Gobierno y aprendizaje

El modelo de gobierno del UDF integra control ejecutivo, técnico y de aprendizaje en un sistema coherente que permite decisiones informadas y mejora continua.

---

## Stage Reviews como mecanismo central

Los **Stage Reviews** son el punto de integración de:

1. **Governance:** Decisiones Go/No-Go y control
2. **Technical Health:** Estado técnico del proyecto
3. **Financial Management:** Presupuesto y ROI
4. **Risk Management:** Identificación y mitigación
5. **Learning:** Captura de aprendizajes

---

## Calendario de Stage Reviews

### SR-I: Initiation Review

**Timing:** Al completar charter y modelo de dominio

**Objetivos:**
- Validar viabilidad del proyecto
- Confirmar alineación estratégica
- Aprobar recursos y presupuesto

**Entregables a revisar:**
- Charter del proyecto
- Modelo de dominio
- Casos de uso o historias iniciales
- Presupuesto y cronograma high-level

**Criterios Go:**
- [ ] Business case aprobado
- [ ] Sponsor identificado y comprometido
- [ ] Recursos confirmados
- [ ] Riesgos iniciales identificados
- [ ] Viabilidad técnica validada

**Participantes:**
- Sponsor (chair)
- Product Owner
- Tech Lead / Architect
- PM / Delivery Lead
- Stakeholders clave

---

### SR-C: Concept & Planning Review

**Timing:** Al completar diseño detallado y planificación

**Objetivos:**
- Aprobar arquitectura de solución
- Validar plan de ejecución
- Confirmar estimaciones
- Establecer baselines

**Entregables a revisar:**
- Diseño de solución (robustness, classes)
- Plan de proyecto detallado
- Matriz de trazabilidad
- Arquitectura técnica
- ADRs iniciales
- Plan de pruebas
- Plan de riesgos

**Criterios Go:**
- [ ] Arquitectura aprobada por comité técnico
- [ ] Plan de proyecto aprobado
- [ ] Baselines establecidos (scope, schedule, cost)
- [ ] Team completo y comprometido
- [ ] Riesgos mayores mitigados

**Participantes:**
- Sponsor
- Product Owner
- Tech Lead / Architect
- PM / Delivery Lead
- QA Lead
- DevOps Lead
- Stakeholders técnicos

---

### SR-E: Build/Engineering Review

**Timing:** Al completar desarrollo y pruebas (puede ser múltiple)

**Objetivos:**
- Validar calidad técnica
- Confirmar cumplimiento de requisitos
- Aprobar transición a validación

**Entregables a revisar:**
- Código implementado
- Pruebas automatizadas
- Technical Health Report
- ADRs completados
- Diagramas de secuencia
- Coverage reports
- Security scan results

**Criterios Go:**
- [ ] THI ≥ threshold definido
- [ ] Cobertura de pruebas ≥ QEI target
- [ ] No defectos críticos abiertos
- [ ] ADRs aprobados
- [ ] Code review completo
- [ ] Security scan passed
- [ ] Performance baseline establecido

**Participantes:**
- Tech Lead (chair)
- Developers
- QA Lead
- DevOps
- Product Owner
- PM

---

### SR-B: Business Validation Review

**Timing:** Post-UAT, pre-producción

**Objetivos:**
- Validar que solución cumple necesidades de negocio
- Aprobar despliegue a producción
- Confirmar readiness operacional

**Entregables a revisar:**
- UAT results y sign-off
- Cutover plan
- Rollback plan
- Runbook
- Training materials
- Communication plan
- Business validation report

**Criterios Go:**
- [ ] UAT aprobado por Product Owner
- [ ] All test gates passed
- [ ] Cutover plan validado
- [ ] Rollback plan probado
- [ ] Operations team capacitado
- [ ] Monitoring configurado
- [ ] Support preparado

**Participantes:**
- Product Owner (chair)
- Business stakeholders
- PM
- Tech Lead
- DevOps
- QA Lead
- Operations

---

### SR-O: Operation Review

**Timing:** 1-2 semanas post-despliegue

**Objetivos:**
- Confirmar estabilidad operacional
- Validar cumplimiento de SLOs
- Aprobar ownership transfer

**Entregables a revisar:**
- Deployment log
- Production metrics
- Incident reports
- SLO compliance
- User feedback
- Runbook validation

**Criterios Go:**
- [ ] Sistema estable por X días
- [ ] SLOs cumplidos
- [ ] No incidentes críticos
- [ ] Monitoring funcionando
- [ ] Team operativo capacitado
- [ ] Knowledge transfer completado

**Participantes:**
- DevOps / Operations (chair)
- Product Owner
- Tech Lead
- PM
- Support team

---

### SR-X: Closure Review

**Timing:** Al cierre formal del proyecto

**Objetivos:**
- Capturar lecciones aprendidas
- Validar realización de beneficios
- Cerrar administrativamente
- Reintegrar conocimiento

**Entregables a revisar:**
- Lessons learned report
- Benefit realization assessment
- Final metrics
- Documentation completeness
- Knowledge artifacts
- Team retrospective

**Criterios de cierre:**
- [ ] Todos los entregables completados
- [ ] Lecciones aprendidas documentadas
- [ ] Conocimiento transferido
- [ ] Cierre financiero completado
- [ ] Archivos organizados
- [ ] Post-implementation review programado

**Participantes:**
- PM (chair)
- Sponsor
- Product Owner
- Tech Lead
- Team completo
- Stakeholders

---

## Governance Bodies

### Executive Steering Committee

**Composición:**
- Sponsor (chair)
- CTO / VP Engineering
- CFO / Finance rep
- Product / Business rep
- PM

**Frecuencia:** Mensual o por excepción

**Responsabilidades:**
- Aprobar Stage Reviews críticos (SR-I, SR-B, SR-X)
- Resolver escalaciones
- Aprobar cambios mayores (>10% budget/schedule)
- Ajustar prioridades estratégicas

---

### Architecture Review Board (ARB)

**Composición:**
- Enterprise Architect (chair)
- Solution Architects
- Security Architect
- Tech Leads relevantes

**Frecuencia:** Bi-weekly o por demanda

**Responsabilidades:**
- Revisar y aprobar ADRs
- Validar cumplimiento de estándares
- Evaluar impacto técnico
- Resolver conflictos arquitectónicos

---

### Change Control Board (CCB)

**Composición:**
- PM (chair)
- Product Owner
- Tech Lead
- Sponsor (para cambios mayores)

**Frecuencia:** Weekly o por demanda

**Responsabilidades:**
- Evaluar change requests
- Aprobar/rechazar cambios
- Priorizar cambios aprobados
- Comunicar decisiones

---

## Métricas de gobierno

### Project Health Dashboard

```yaml
# governance_metrics.yaml

overall_health: green

dimensions:
  technical:
    status: green
    thi: 78
    trend: improving
    
  schedule:
    status: yellow
    variance_days: +5
    cpi: 0.95
    trend: stable
    
  budget:
    status: green
    variance_pct: -2%
    forecast_at_completion: $498K
    trend: improving
    
  quality:
    status: green
    defects_critical: 0
    defects_high: 2
    test_coverage: 78%
    
  risk:
    status: yellow
    high_risks_open: 2
    mitigations_on_track: 5
    
  stakeholder_satisfaction:
    status: green
    score: 8.2
    trend: stable

alerts:
  - type: schedule
    message: "5 days behind baseline"
    severity: medium
    
  - type: risk
    message: "2 high risks need attention"
    severity: medium
```

---

## Integración de aprendizajes en governance

### Learning Review en cada SR

Cada Stage Review incluye sección dedicada:

```markdown
## Learning Review

### What worked well
1. [Success/best practice]
2. [Success/best practice]

### What needs improvement
1. [Challenge/issue]
2. [Challenge/issue]

### Key learnings
1. [Actionable insight]
2. [Actionable insight]

### Actions to take
- [ ] Action 1 - Owner: [Name] - Due: [Date]
- [ ] Action 2 - Owner: [Name] - Due: [Date]

### Process improvements
- [ ] Update process/template X
- [ ] Add control/check Y
- [ ] Remove unnecessary Z
```

---

## Reporting Structure

### Status Report (Weekly)

```markdown
# Status Report - Week [XX]

**Project:** [Name]
**Period:** [Date range]
**Overall Status:** 🟢

## Progress This Week

### Completed
- [x] Task 1
- [x] Task 2

### In Progress
- [ ] Task 3 (80%)
- [ ] Task 4 (60%)

### Planned Next Week
- [ ] Task 5
- [ ] Task 6

## Metrics

| Metric    | Target | Actual | Status |
| --------- | ------ | ------ | ------ |
| Velocity  | 25     | 23     | 🟡     |
| Quality   | 75%    | 78%    | 🟢     |
| Budget    | 42%    | 40%    | 🟢     |

## Risks & Issues

### New This Week
- R07: Vendor delay - High - Escalated to PMO

### Updated
- R03: Resource availability - Mitigated ✅

## Decisions Needed
1. [Decision point requiring input]

## Help Needed
1. [Blocker or support request]
```

---

### Executive Summary (Monthly)

```markdown
# Executive Summary - [Month]

**Status:** 🟢 On Track

## Key Highlights
- Completed SR-E with all gates passed
- Launched beta to 1,000 users
- NPS increased from 42 to 58

## Health by Dimension

| Dimension | Status | Comment                |
| --------- | ------ | ---------------------- |
| Technical | 🟢     | THI 78, all metrics OK |
| Schedule  | 🟡     | 5 days behind, recoverable |
| Budget    | 🟢     | 2% under budget        |
| Quality   | 🟢     | Zero critical defects  |
| Risk      | 🟡     | 2 high risks managed   |

## Financials
- **Budget:** $500K
- **Spent:** $198K (40%)
- **Forecast:** $498K
- **Variance:** -$2K (under budget)

## Next Month Focus
1. Complete UAT
2. Prepare production deployment
3. Finalize documentation

## Executive Actions Needed
- None at this time
```

---

## Escalation Paths

### Issue Escalation Matrix

| Severity | Response Time | Escalation Path                        |
| -------- | ------------- | -------------------------------------- |
| Critical | 1 hour        | PM → Sponsor → Steering Committee      |
| High     | 4 hours       | PM → Tech Lead → ARB (if technical)    |
| Medium   | 24 hours      | PM → appropriate owner                 |
| Low      | 1 week        | Backlog for next planning              |

---

## Audit Trail

Para proyectos regulados (PDI: XL):

```markdown
# Audit Trail

## Change Log

| Date       | Change | Justification | Approver | Document |
| ---------- | ------ | ------------- | -------- | -------- |
| 2025-01-15 | Baseline established | SR-C | PM | baseline_v1.0 |
| 2025-02-10 | Scope change CHG-001 | Business need | CCB | change_001.pdf |
| 2025-03-05 | Technical change ADR-003 | Performance | ARB | adr_003.md |

## Review History

| Date       | Review Type | Outcome | Attendees | Minutes |
| ---------- | ----------- | ------- | --------- | ------- |
| 2025-01-10 | SR-I        | GO      | Sponsor, PM, PO, Tech Lead | sr_i_minutes.md |
| 2025-02-01 | SR-C        | GO      | Full team | sr_c_minutes.md |
| 2025-03-15 | SR-E        | GO      | Technical team | sr_e_minutes.md |

## Approval Records

All formal approvals tracked with:
- Document version
- Approver name and role
- Date and signature (digital)
- Comments or conditions
```

---

## Compliance Checklist

Para proyectos con requisitos de compliance:

```markdown
# Compliance Checklist

## Documentation
- [ ] All requirements traced to tests
- [ ] All ADRs approved and signed
- [ ] Risk register current and reviewed
- [ ] Change log complete and approved
- [ ] Validation protocol executed

## Quality
- [ ] Quality metrics meet targets
- [ ] Test coverage ≥ required threshold
- [ ] Security scan passed
- [ ] Code review complete
- [ ] Static analysis clean

## Governance
- [ ] All Stage Reviews completed
- [ ] Baselines formally established
- [ ] Changes formally approved
- [ ] Audit trail complete
- [ ] Sign-offs obtained

## Operational
- [ ] Runbook validated
- [ ] Disaster recovery tested
- [ ] Backup/restore verified
- [ ] Monitoring configured
- [ ] Support trained
```

---

[← Anterior: Delivery Cube](11-delivery-cube.md) | [Siguiente: Testing, Risk & Maturity →](13-testing-risk-maturity.md)
