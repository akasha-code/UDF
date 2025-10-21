# 4) Gobierno y Project Management

El gobierno en el UDF integra gestión técnica, financiera y de riesgos en un proceso unificado que mantiene transparencia y control sin sacrificar agilidad.

---

## Stage Review Board

Los **Stage Reviews** son el mecanismo central de gobierno del UDF. Cada SR consolida el estado del proyecto en tres dimensiones: técnica, financiera y de riesgos.

### Estructura del Stage Review

El documento `stage_review_board.md` contiene:

```markdown
# Stage Review Board - [Fase]

**Proyecto:** [Nombre]
**Fecha:** [YYYY-MM-DD]
**Fase:** [Initiation/Concept/Build/Validation/Operation/Closure]
**Revisión:** SR-[I/C/E/B/O/X]

## 1. Estado Técnico

### Technical Health Index (THI)
- **Score actual:** [valor]/100
- **Tendencia:** [↑/→/↓]
- **Status:** [✅ PASS / ⚠️ WARNING / ❌ FAIL]

### Métricas técnicas
| Métrica                | Actual | Target | Status |
| ---------------------- | ------ | ------ | ------ |
| Code Coverage          | XX%    | XX%    | ✅/⚠️/❌ |
| Technical Debt         | XX%    | <X%    | ✅/⚠️/❌ |
| Critical Defects       | X      | 0      | ✅/⚠️/❌ |
| Architecture Compliance| XX%    | XX%    | ✅/⚠️/❌ |

### ADRs Cerrados
- [ADR-001: Decision Title](adr_001.md) - Approved
- [ADR-002: Another Decision](adr_002.md) - Approved

### Issues Técnicos Abiertos
1. [Issue #XX] - Description - Priority: HIGH
2. [Issue #YY] - Description - Priority: MEDIUM

## 2. Estado Financiero

### Presupuesto
- **Presupuesto total:** $[valor]
- **Costo actual:** $[valor]
- **Variación:** ±[valor] ([±XX%])
- **Forecast al cierre:** $[valor]

### Métricas financieras
| Métrica                | Valor  | Target | Status |
| ---------------------- | ------ | ------ | ------ |
| Cost Performance Index | X.XX   | ≥1.0   | ✅/⚠️/❌ |
| Schedule Performance   | X.XX   | ≥1.0   | ✅/⚠️/❌ |
| Budget Consumption     | XX%    | XX%    | ✅/⚠️/❌ |
| ROI Esperado          | XX%    | XX%    | ✅/⚠️/❌ |

### Cambios de Alcance
- [CHG-001] - Description - Impact: $[valor] / [X] days
- [CHG-002] - Description - Impact: $[valor] / [X] days

## 3. Gestión de Riesgos

### Riesgos Activos

| ID  | Descripción | Probabilidad | Impacto | Score | Mitigación | Owner |
| --- | ----------- | ------------ | ------- | ----- | ---------- | ----- |
| R01 | [desc]      | [H/M/L]      | [H/M/L] | XX    | [plan]     | [name]|
| R02 | [desc]      | [H/M/L]      | [H/M/L] | XX    | [plan]     | [name]|

### Riesgos Materializados
- [R03] - Description - Impact: [descripción] - Response: [acción]

### Oportunidades
- [O01] - Description - Potential benefit: [descripción]

## 4. Decisiones Ejecutivas

### Decisiones tomadas
1. **[Decisión 1]:** [Descripción y justificación]
   - Owner: [Nombre]
   - Deadline: [Fecha]
   
2. **[Decisión 2]:** [Descripción y justificación]
   - Owner: [Nombre]
   - Deadline: [Fecha]

### Acciones pendientes
| ID  | Acción | Owner | Deadline | Status |
| --- | ------ | ----- | -------- | ------ |
| A01 | [desc] | [name]| [date]   | [status]|
| A02 | [desc] | [name]| [date]   | [status]|

## 5. Aprendizajes

### Lecciones de esta fase
1. [Aprendizaje 1] - Aplicar en: [dónde]
2. [Aprendizaje 2] - Aplicar en: [dónde]

### Mejoras al proceso
- [Mejora sugerida 1]
- [Mejora sugerida 2]

## 6. Decisión Go/No-Go

**Criterios de avance:**
- [ ] THI ≥ [threshold]
- [ ] Presupuesto dentro de rango aceptable
- [ ] No hay riesgos bloqueantes sin mitigación
- [ ] Todos los entregables de fase completados
- [ ] Aprobación de stakeholders clave

**Decisión:** [GO ✅ / NO-GO ❌ / GO CON CONDICIONES ⚠️]

**Justificación:** [Explicación de la decisión]

**Aprobadores:**
- [ ] Project Manager: [Nombre] - [Fecha]
- [ ] Tech Lead: [Nombre] - [Fecha]
- [ ] Product Owner: [Nombre] - [Fecha]
- [ ] Sponsor: [Nombre] - [Fecha]

## 7. Próximos pasos

1. [Acción 1] - Owner: [Nombre] - Deadline: [Fecha]
2. [Acción 2] - Owner: [Nombre] - Deadline: [Fecha]
3. [Acción 3] - Owner: [Nombre] - Deadline: [Fecha]

---

**Próximo Stage Review:** SR-[X] - [Fecha estimada]
```

---

## Frecuencia de Stage Reviews

| Fase            | SR       | Frecuencia típica          |
| --------------- | -------- | -------------------------- |
| Initiation      | SR-I     | Al completar charter       |
| Concept         | SR-C     | Al completar diseño        |
| Build           | SR-E     | Cada 2-4 semanas (según DSI)|
| Validation      | SR-B     | Pre-producción             |
| Operation       | SR-O     | Post-despliegue (1-2 sem)  |
| Closure         | SR-X     | Al cierre del proyecto     |

---

## Control de Cambios

### Change Control Board (CCB)

Cambios formales al baseline requieren aprobación del CCB:

```yaml
# change_request.yaml
id: CHG-001
title: "Add new payment method"
type: [scope/schedule/budget/quality]
requestor: "Product Owner"
date: "2025-10-21"
description: |
  Detailed description of the change
impact:
  scope: "Added feature"
  schedule: "+2 weeks"
  budget: "+$5,000"
  quality: "Requires additional testing"
  risks:
    - "Integration complexity"
    - "Timeline pressure"
justification: |
  Business justification for the change
alternatives_considered:
  - "Alternative 1"
  - "Alternative 2"
decision: [approved/rejected/deferred]
approved_by:
  - role: "Sponsor"
    name: "John Doe"
    date: "2025-10-22"
  - role: "PM"
    name: "Jane Smith"
    date: "2025-10-22"
```

### Baseline Management

Los baselines se establecen en momentos clave:

1. **Scope Baseline:** Post SR-C (Planning)
2. **Schedule Baseline:** Post SR-C (Planning)
3. **Cost Baseline:** Post SR-C (Planning)
4. **Quality Baseline:** Post SR-E (Build)
5. **Technical Baseline:** Post SR-E (Build)

Cada baseline se marca con un Git tag:
```bash
git tag -a baseline-sr-c -m "Scope, Schedule, Cost Baseline"
git tag -a baseline-sr-e -m "Quality and Technical Baseline"
```

---

## Compatibilidad con marcos estándar

### PMBOK Knowledge Areas

| PMBOK Area           | UDF Implementation                          |
| -------------------- | ------------------------------------------- |
| Integration          | Stage Reviews, `stage_review_board.md`      |
| Scope                | `charter.md`, `use-cases/`, traceability    |
| Schedule             | `project_plan.md`, DSI configuration        |
| Cost                 | Financial section in SR, CPI/SPI tracking   |
| Quality              | QEI, `quality_charter.md`, THI              |
| Resources            | `stakeholder_register.csv`, RACI matrices   |
| Communications       | `status_report.md`, `executive_summary.md`  |
| Risk                 | `risk_register.csv`, SR risk section        |
| Procurement          | External TTI, vendor management             |
| Stakeholders         | `stakeholder_register.csv`, UAT signoff     |

### PRINCE2 Themes

| PRINCE2 Theme    | UDF Implementation                        |
| ---------------- | ----------------------------------------- |
| Business Case    | `charter.md`, `benefit_realization_plan.md`|
| Organization     | Roles (see [section 5](05-roles-interactions.md))|
| Quality          | `quality_charter.md`, QEI, THI            |
| Plans            | `project_plan.md`, phase plans            |
| Risk             | `risk_register.csv`, SR risk analysis     |
| Change           | CCB, `change_request.yaml`                |
| Progress         | Stage Reviews, `status_report.md`         |

### SAFe Alignment

| SAFe Element         | UDF Equivalent                            |
| -------------------- | ----------------------------------------- |
| PI Planning          | Concept & Planning (SR-C)                 |
| Sprint               | Build iterations (adjusted by DSI)        |
| System Demo          | Business Validation (SR-B)                |
| Inspect & Adapt      | Learning Loop, `lessons_learned.md`       |
| ART Sync             | Stage Reviews                             |
| Release Train        | Operation (SR-O)                          |

---

## Executive Summary

El `executive_summary.md` proporciona visión ejecutiva para stakeholders de alto nivel:

```markdown
# Executive Summary - [Project Name]

**Date:** [YYYY-MM-DD]
**Status:** [🟢 On Track / 🟡 At Risk / 🔴 Critical]

## Highlights

### Achievements this period
- [Achievement 1]
- [Achievement 2]
- [Achievement 3]

### Key Metrics
- **Progress:** XX% complete
- **Budget:** XX% consumed
- **Schedule:** [On time / X weeks delay]
- **Quality:** THI XX/100

## Status by dimension

| Dimension | Status | Trend | Comment                    |
| --------- | ------ | ----- | -------------------------- |
| Technical | 🟢     | ↑     | Quality metrics improving  |
| Financial | 🟡     | →     | Budget pressure in Q2      |
| Schedule  | 🟢     | ↑     | Recovered 1-week delay     |
| Risk      | 🟡     | →     | 2 high risks under control |

## Top 3 Risks
1. [Risk 1] - Mitigation: [plan]
2. [Risk 2] - Mitigation: [plan]
3. [Risk 3] - Mitigation: [plan]

## Decisions Needed
1. [Decision point 1]
2. [Decision point 2]

## Next Milestone
**[Milestone name]** - [Date] - [Description]
```

---

## Reporting Cadence

| Report Type          | Frequency    | Audience              |
| -------------------- | ------------ | --------------------- |
| Status Report        | Weekly       | Team, PM              |
| Executive Summary    | Bi-weekly    | Sponsors, Executives  |
| Stage Review         | Per phase    | All stakeholders      |
| Technical Health     | Per SR       | Tech Lead, QA, PM     |
| Financial Report     | Monthly      | PM, Finance, Sponsor  |
| Risk Report          | Weekly       | PM, Risk Owner        |

---

[← Anterior: Technical Management](03-technical-management.md) | [Siguiente: Roles & Interactions →](05-roles-interactions.md)
