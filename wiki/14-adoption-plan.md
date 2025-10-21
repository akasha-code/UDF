# 14) Plan de adopción

El UDF se adopta de forma progresiva, permitiendo a las organizaciones comenzar con lo mínimo e ir incrementando madurez sin disrupciones mayores.

---

## Principios de adopción

1. **Incremental, no disruptivo:** Adoptar en fases, sin reemplazar todo de golpe
2. **Value-driven:** Comenzar donde hay más dolor o mayor valor
3. **Adaptativo:** Ajustar PDI/DSI/QEI al contexto actual
4. **Evidence-based:** Medir impacto y ajustar
5. **Team-centric:** Involucrar al equipo desde el inicio

---

## Fases de adopción

### Fase 0: Assessment (Semana 1-2)

**Objetivo:** Entender estado actual y definir objetivos

**Actividades:**
- [ ] Evaluar madurez actual en 5 pilares
- [ ] Identificar pain points principales
- [ ] Definir objetivos de adopción
- [ ] Determinar configuración inicial (PDI, DSI, QEI, TTI)
- [ ] Identificar proyecto piloto

**Entregables:**
- Maturity assessment report
- Adoption goals documento
- Project configuration (project_config.yaml)
- Piloto identificado

**Participantes:**
- Leadership team
- PM/Tech Lead del piloto
- Change champion

---

### Fase 1: Foundation (Semana 3-4)

**Objetivo:** Establecer bases mínimas del UDF

**Actividades:**
- [ ] Crear estructura de repositorio
- [ ] Establecer artefactos mínimos (según PDI)
- [ ] Configurar Stage Review básico (SR-I template)
- [ ] Definir Technical Health Index inicial
- [ ] Setup básico de CI/CD si no existe

**Entregables:**
```
project/
├── charter.md
├── domain-model.puml
├── user-stories/
├── README.md
├── project_config.yaml
└── .github/
    └── stage_review_templates/
        └── sr_template.md
```

**Quick Wins:**
- Charter documento como single source of truth
- Stage Review da visibilidad ejecutiva
- Estructura organizada reduce búsqueda de información

**Participantes:**
- PM (lead)
- Tech Lead
- Team del piloto

---

### Fase 2: Core Implementation (Semana 5-8)

**Objetivo:** Implementar prácticas core del UDF

**Actividades:**
- [ ] Ejecutar primer Stage Review formal (SR-I o SR-C)
- [ ] Implementar matriz de trazabilidad básica
- [ ] Configurar Technical Health monitoring
- [ ] Establecer quality gates en CI/CD
- [ ] Crear primeros ADRs
- [ ] Iniciar risk register

**Entregables:**
- Stage Review completado con decisiones documentadas
- Traceability matrix vinculando requisitos a implementación
- Technical Health Report automatizado
- CI/CD con gates configurados
- 3-5 ADRs documentados
- Risk register inicial

**Métricas de éxito:**
- Stage Review ejecutado en <2 horas
- THI calculado y reportado
- Quality gates funcionando (>0 failures capturados)
- Equipo reporta mayor claridad en decisiones

**Participantes:**
- Equipo completo del piloto
- Sponsor (para SR)
- Stakeholders clave

---

### Fase 3: Expansion (Mes 2-3)

**Objetivo:** Expandir UDF a aspectos avanzados y más proyectos

**Actividades:**
- [ ] Implementar todos los Stage Reviews del ciclo
- [ ] Integrar testing strategy completa
- [ ] Establecer Learning Loop
- [ ] Agregar governance artifacts (executive summary, status reports)
- [ ] Extender a segundo proyecto piloto
- [ ] Capacitar más equipos

**Entregables:**
- Ciclo completo de SRs ejecutado
- Test strategy documentada y automatizada
- Primera learning entry creada
- Executive summaries mensuales
- Segundo proyecto adoptando UDF

**Métricas de éxito:**
- Proyecto piloto completa al menos 4 Stage Reviews
- Test automation rate >70%
- Al menos 3 learning entries documentadas
- Segundo equipo onboarded exitosamente

**Participantes:**
- Equipos piloto (1 y 2)
- Leadership team
- Change champions

---

### Fase 4: Optimization (Mes 3-6)

**Objetivo:** Optimizar procesos y escalar a organización

**Actividades:**
- [ ] Automatizar generación de reportes
- [ ] Implementar dashboards en tiempo real
- [ ] Establecer portfolio layer (si aplica)
- [ ] Crear templates y herramientas reutilizables
- [ ] Capacitación organizacional
- [ ] Integrar con sistemas existentes (JIRA, etc.)

**Entregables:**
- Scripts de automatización de reportes
- Dashboards en Grafana/PowerBI
- Portfolio dashboard (si aplica)
- Library de templates
- Training materials
- Integraciones configuradas

**Métricas de éxito:**
- 5+ proyectos usando UDF
- Tiempo de preparación de SR reducido en 50%
- Portfolio visibility establecida
- Net Promoter Score del UDF >70

**Participantes:**
- Equipos múltiples
- PMO/Portfolio team
- Tools/automation team

---

## Adoption Roadmap

```
Month 0-1: Foundation
├── Week 1-2: Assessment
├── Week 3-4: Foundation setup
└── Quick wins visible

Month 2-3: Core Implementation
├── Stage Reviews operational
├── Quality gates working
├── First learnings captured
└── Team confidence high

Month 3-6: Expansion
├── Multiple teams onboarded
├── Full cycle executed
├── Learning culture starting
└── Value demonstrated

Month 6+: Optimization
├── Organization-wide adoption
├── Automated and optimized
├── Portfolio visibility
└── Continuous improvement
```

---

## Configuración inicial recomendada

### Startup / Small Team

```yaml
delivery_cube:
  pdi: XS
  dsi: 5
  qei: low
  tti: integrated

adoption_approach: minimal_viable
focus: speed_and_learning

phase_1_artifacts:
  - charter.md
  - user-stories/
  - README.md
  
phase_2_artifacts:
  - tests.csv
  - technical_health_report.md
  - stage_review_board.md
```

### Mid-size Company

```yaml
delivery_cube:
  pdi: M
  dsi: 3
  qei: medium
  tti: integrated

adoption_approach: standard_implementation
focus: balance_speed_control

phase_1_artifacts:
  - charter.md
  - domain-model.puml
  - user-stories/
  - project_config.yaml
  
phase_2_artifacts:
  - robustness.puml
  - sequence.puml
  - adr/
  - tests.csv
  - quality_charter.md
  - stage_review_board.md
```

### Enterprise / Regulated

```yaml
delivery_cube:
  pdi: L
  dsi: 2
  qei: high
  tti: dedicated

adoption_approach: comprehensive_implementation
focus: compliance_and_quality

phase_1_artifacts:
  - charter.md
  - requirements.yaml
  - domain-model.puml
  - stakeholder_register.csv
  
phase_2_artifacts:
  - all_design_artifacts
  - validation_manifest.yaml
  - architecture_governance_matrix.md
  - quality_charter.md
  - risk_register.csv
  - stage_review_board.md
```

---

## Change Management

### Stakeholder Engagement

| Stakeholder        | Concerns                          | Address By                         |
| ------------------ | --------------------------------- | ---------------------------------- |
| **Executives**     | ROI, time investment, disruption  | Quick wins, metrics, pilot results |
| **PM/Managers**    | Overhead, bureaucracy             | Streamlined process, automation    |
| **Tech Leads**     | Technical debt, new tools         | Technical value (ADRs, THI)        |
| **Developers**     | More documentation, process       | Better clarity, less rework        |
| **QA**             | More work, responsibility         | Empowerment, quality visibility    |

### Communication Plan

| Phase      | Message                                      | Channel              | Frequency |
| ---------- | -------------------------------------------- | -------------------- | --------- |
| Pre-launch | Why UDF, benefits, pilot announcement        | Town hall, email     | Once      |
| Launch     | Pilot kickoff, training sessions             | Workshops, docs      | Weekly    |
| Pilot      | Progress updates, quick wins                 | Newsletter, standup  | Bi-weekly |
| Expansion  | Success stories, learnings, next steps       | Town hall, showcase  | Monthly   |
| Steady     | Continuous improvement, celebrations         | Multiple channels    | Ongoing   |

### Training Program

#### Level 1: Awareness (1 hour)
**Audience:** All stakeholders
**Content:**
- What is UDF
- Why we're adopting it
- High-level phases and benefits

#### Level 2: Practitioner (4 hours)
**Audience:** Team members
**Content:**
- Deep dive into phases
- Hands-on with artifacts
- Tools and automation
- Q&A and scenarios

#### Level 3: Master (2 days)
**Audience:** PMs, Tech Leads, Champions
**Content:**
- Complete UDF methodology
- Configuration and customization
- Advanced topics (portfolio, compliance)
- Coaching and facilitation skills

---

## Success Metrics

### Leading Indicators (What to watch during adoption)

| Metric                          | Target        | Status |
| ------------------------------- | ------------- | ------ |
| Team training completion        | 100%          | Track  |
| Stage Reviews scheduled/executed| 100%          | Track  |
| Artifacts created on time       | >90%          | Track  |
| Team confidence score           | >7/10         | Survey |
| Adoption blockers identified    | All resolved  | Track  |

### Lagging Indicators (Value delivered)

| Metric                              | Baseline | Target | Actual |
| ----------------------------------- | -------- | ------ | ------ |
| Project predictability (on-time %)  | 60%      | 80%    | TBD    |
| Quality (defects in production)     | 15       | <5     | TBD    |
| Technical Health Index              | N/A      | >75    | TBD    |
| Time to Stage Review                | N/A      | <2h    | TBD    |
| Team satisfaction                   | 6.5/10   | >8/10  | TBD    |
| Leadership visibility score         | 5/10     | >8/10  | TBD    |

---

## Common Pitfalls and Mitigation

### Pitfall 1: Too much too fast
**Risk:** Team overwhelmed, adoption fails

**Mitigation:**
- Start with minimal configuration (PDI: XS or S)
- Focus on 1-2 quick wins first
- Gradual expansion based on readiness

### Pitfall 2: Lack of executive support
**Risk:** No authority, no resources

**Mitigation:**
- Secure sponsor before starting
- Regular executive updates with metrics
- Tie to strategic objectives

### Pitfall 3: Tool before culture
**Risk:** Process without understanding

**Mitigation:**
- Training and coaching first
- Pilot with engaged team
- Celebrate and share learnings

### Pitfall 4: One-size-fits-all
**Risk:** Force same config on all projects

**Mitigation:**
- Customize PDI/DSI/QEI per project
- Allow flexibility within guardrails
- Learn and adapt

### Pitfall 5: No feedback loop
**Risk:** Adoption issues not addressed

**Mitigation:**
- Regular retrospectives on adoption
- Open channels for feedback
- Rapid adjustment of approach

---

## Pilot Project Selection

### Ideal Pilot Characteristics

✅ **Good pilot candidates:**
- Medium complexity (not too simple, not too complex)
- Engaged and open-minded team
- Executive visibility but not mission-critical
- Timeline 3-6 months
- Mix of technical and business stakeholders

❌ **Avoid for first pilot:**
- Brand new team without trust
- Mission-critical with no room for learning
- Very short timeline (<1 month)
- Purely technical or purely business (no balance)
- Team resistant to change

---

## Support Model

### During Adoption

**Change Champions:**
- 1-2 people per team
- Trained in UDF
- First point of contact
- Facilitate Stage Reviews

**COE (Center of Excellence):**
- Centralized support team
- Maintain templates and tools
- Provide coaching
- Track metrics

**Office Hours:**
- Weekly Q&A sessions
- Drop-in support
- Share learnings across teams

### Post-Adoption

**Community of Practice:**
- Regular meetups
- Knowledge sharing
- Continuous improvement
- Innovation showcase

---

[← Anterior: Testing, Risk & Maturity](13-testing-risk-maturity.md) | [Siguiente: Synthesis →](15-synthesis.md)
