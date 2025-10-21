# 6) Calidad y pruebas

El enfoque de calidad del UDF es contextual, basado en riesgo y proporcional a las necesidades del proyecto. El Quality Emphasis Index (QEI) determina el nivel de rigurosidad y cobertura de pruebas.

---

## Quality Emphasis Index (QEI)

El QEI define el nivel de énfasis en calidad y determina qué tipos de prueba son obligatorios:

| Nivel      | QEI    | Tipos de prueba                                  | Cobertura mínima |
| ---------- | ------ | ------------------------------------------------ | ---------------- |
| **XS–S**   | Low    | Unit / Smoke / Exploratory                       | 60%              |
| **M**      | Medium | Integration / Black-Gray Box                     | 75%              |
| **L–XL**   | High   | Regression / Validation Protocol / AI Model Test | 85%              |

---

## Quality Charter

El `quality_charter.md` define las políticas y métricas de calidad del proyecto:

```markdown
# Quality Charter - [Project Name]

## Objetivos de calidad

1. **Funcionalidad:** El sistema cumple con todos los requisitos funcionales
2. **Confiabilidad:** El sistema es estable y predecible
3. **Usabilidad:** El sistema es intuitivo y accesible
4. **Eficiencia:** El sistema responde dentro de SLOs definidos
5. **Mantenibilidad:** El código es limpio, documentado y testeable
6. **Portabilidad:** El sistema funciona en entornos objetivo

## Métricas de calidad mínimas

### Cobertura de pruebas
- **Unit Test Coverage:** ≥ 75%
- **Integration Test Coverage:** ≥ 70%
- **E2E Test Coverage:** ≥ 60% de flujos críticos

### Calidad de código
- **Technical Debt Ratio:** < 5%
- **Code Duplication:** < 3%
- **Cyclomatic Complexity:** < 10 (promedio)
- **Maintainability Index:** ≥ 65

### Defectos
- **Critical Defects:** 0 en producción
- **High Defects:** < 5 en producción
- **Defect Density:** < 2 defectos por KLOC
- **Defect Escape Rate:** < 10%

### Automatización
- **Test Automation Rate:** ≥ 80% de casos de prueba
- **CI/CD Pipeline Success Rate:** ≥ 95%
- **Deployment Frequency:** Según DSI target

## Políticas de aprobación

### Build Phase (SR-E)
- [ ] Todos los unit tests pasan
- [ ] Cobertura ≥ threshold definido
- [ ] No hay defectos críticos abiertos
- [ ] SonarQube quality gate: PASSED
- [ ] Security scan: No vulnerabilidades críticas

### Business Validation (SR-B)
- [ ] UAT completado exitosamente
- [ ] Sign-off de Product Owner
- [ ] Documentación actualizada
- [ ] Runbook validado
- [ ] Plan de rollback probado

## Herramientas de calidad

- **Testing:** [Jest, Pytest, Playwright]
- **Static Analysis:** [SonarQube, ESLint]
- **Security:** [Snyk, OWASP]
- **Performance:** [k6, Lighthouse]
- **Monitoring:** [Datadog, Grafana]
```

---

## Tipos de prueba por contexto

### Pruebas básicas (QEI: Low)

#### Unit Testing
* **Objetivo:** Validar componentes individuales
* **Framework:** Jest, JUnit, pytest, NUnit
* **Cobertura mínima:** 60%
* **Fase:** Build (SR-E)

#### Smoke Testing
* **Objetivo:** Verificar funcionalidad crítica básica
* **Enfoque:** Manual o automatizado básico
* **Frecuencia:** Cada build
* **Fase:** Build/Validation

#### Exploratory Testing
* **Objetivo:** Descubrir defectos no obvios
* **Enfoque:** Manual, basado en experiencia
* **Documentación:** Session notes
* **Fase:** Build/Validation

---

### Pruebas intermedias (QEI: Medium)

#### Integration Testing
* **Objetivo:** Validar interacción entre componentes
* **Framework:** TestContainers, Postman, REST Assured
* **Cobertura mínima:** 70%
* **Fase:** Build (SR-E)

#### Black-Box Testing
* **Objetivo:** Validar comportamiento sin conocer implementación
* **Técnicas:** Equivalence partitioning, boundary value
* **Fase:** Build/Validation

#### Gray-Box Testing
* **Objetivo:** Balance entre caja negra y blanca
* **Aplicación:** APIs, servicios, integraciones
* **Fase:** Build/Validation

#### Regression Testing
* **Objetivo:** Asegurar que cambios no rompan funcionalidad existente
* **Automatización:** Alta (>80%)
* **Frecuencia:** Cada release
* **Fase:** Build/Validation

---

### Pruebas avanzadas (QEI: High)

#### Validation Protocol
* **Objetivo:** Cumplimiento regulatorio (GxP, ISO)
* **Formato:** Protocolo formal + evidencias
* **Trazabilidad:** Completa (URS → Test → Evidence)
* **Fase:** Validation (SR-B)

#### Performance Testing
* **Tipos:**
  - Load testing: Comportamiento bajo carga esperada
  - Stress testing: Límites del sistema
  - Spike testing: Picos súbitos
  - Endurance testing: Estabilidad prolongada
* **Framework:** k6, JMeter, Gatling
* **Fase:** Build/Validation

#### Security Testing
* **Tipos:**
  - Vulnerability scanning
  - Penetration testing
  - Security code review
  - Dependency scanning
* **Tools:** Snyk, OWASP ZAP, Burp Suite
* **Fase:** Build/Validation

#### AI Model Testing
* **Técnicas:**
  - Data validation
  - Model bias detection
  - Explainability testing
  - Drift detection
  - A/B testing
* **Framework:** Great Expectations, Evidently AI
* **Fase:** Build/Validation

---

## Test Automation Strategy

### Pirámide de automatización

```
        E2E (10-20%)
    ────────────────
   Integration (20-30%)
  ────────────────────────
     Unit (50-70%)
────────────────────────────────
```

### Configuración de automatización

```yaml
# test_automation.yaml
automation_strategy:
  target_rate: 80%
  priority: [critical, high, medium, low]
  
  unit_tests:
    framework: jest
    coverage_target: 75%
    run_on: [commit, pr]
    
  integration_tests:
    framework: testcontainers
    coverage_target: 70%
    run_on: [pr, merge]
    
  e2e_tests:
    framework: playwright
    critical_flows: 100%
    run_on: [merge, release]
    parallel: true
    
  performance_tests:
    framework: k6
    baseline: true
    run_on: [release, scheduled]
    
  security_tests:
    static: snyk
    dynamic: owasp-zap
    run_on: [pr, merge, scheduled]
```

---

## Test Execution Plan

### Test Matrix

| Test Type      | Priority | Owner    | Environment | Frequency    | Automation |
| -------------- | -------- | -------- | ----------- | ------------ | ---------- |
| Unit           | Critical | Dev      | Local       | Every commit | 100%       |
| Integration    | High     | Dev/QA   | CI          | Every PR     | 90%        |
| E2E            | High     | QA       | Staging     | Every merge  | 80%        |
| Smoke          | Critical | QA       | All         | Every deploy | 100%       |
| Regression     | High     | QA       | Staging     | Every sprint | 85%        |
| Performance    | Medium   | DevOps   | Perf env    | Weekly       | 100%       |
| Security       | High     | SecOps   | All         | Daily        | 100%       |
| UAT            | Critical | Business | Staging     | Pre-release  | 20%        |

---

## Defect Management

### Clasificación de defectos

| Severity  | Descripción                                      | SLA Response | SLA Fix      |
| --------- | ------------------------------------------------ | ------------ | ------------ |
| Critical  | Sistema no funciona, pérdida de datos           | 1 hora       | 24 horas     |
| High      | Funcionalidad clave afectada                     | 4 horas      | 3 días       |
| Medium    | Funcionalidad menor afectada, hay workaround     | 24 horas     | 1 semana     |
| Low       | Cosméticos, mejoras                              | 1 semana     | Próx. release|

### Workflow de defectos

```
New → Triaged → In Progress → Fixed → Testing → Verified → Closed
                                        ↓
                                    Reopen
```

---

## Quality Gates

Los Quality Gates son puntos de control automáticos que deben superarse para avanzar:

### Gate Build (SR-E)

```yaml
gate_build:
  conditions:
    - unit_test_coverage >= 75%
    - integration_test_coverage >= 70%
    - sonar_quality_gate == "PASSED"
    - critical_defects == 0
    - high_defects <= 3
    - security_vulnerabilities_critical == 0
```

### Gate Validation (SR-B)

```yaml
gate_validation:
  conditions:
    - uat_approval == "APPROVED"
    - regression_tests == "PASSED"
    - performance_baseline == "PASSED"
    - security_scan == "PASSED"
    - documentation == "COMPLETE"
    - runbook == "VALIDATED"
```

---

## Acceptance Criteria

Cada historia de usuario / caso de uso debe tener criterios de aceptación claros:

```markdown
## US-001: User Login

### Acceptance Criteria
- [ ] Usuario puede ingresar email y password
- [ ] Sistema valida credenciales contra base de datos
- [ ] Usuario exitoso es redirigido a dashboard
- [ ] Usuario inválido recibe mensaje de error
- [ ] Sistema bloquea cuenta después de 3 intentos fallidos
- [ ] Sistema registra todos los intentos de login en audit log

### Test Cases
- TC-001: Login exitoso con credenciales válidas
- TC-002: Login fallido con password incorrecta
- TC-003: Login fallido con usuario inexistente
- TC-004: Bloqueo de cuenta tras 3 intentos
- TC-005: Validación de formato de email

### Non-Functional Requirements
- Tiempo de respuesta: < 500ms (p95)
- Disponibilidad: 99.9%
- Seguridad: Passwords hasheados con bcrypt
```

---

## QA in CI/CD Pipeline

Integración de calidad en el pipeline:

```yaml
# .github/workflows/qa-pipeline.yml
name: QA Pipeline

on: [pull_request, push]

jobs:
  unit-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run unit tests
        run: npm test -- --coverage
      - name: Check coverage threshold
        run: |
          coverage=$(jq '.total.lines.pct' coverage/coverage-summary.json)
          if (( $(echo "$coverage < 75" | bc -l) )); then
            echo "Coverage $coverage% is below 75%"
            exit 1
          fi

  integration-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Start test containers
        run: docker-compose -f docker-compose.test.yml up -d
      - name: Run integration tests
        run: npm run test:integration

  static-analysis:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run SonarQube scan
        run: sonar-scanner

  security-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run Snyk
        run: snyk test

  quality-gate:
    needs: [unit-tests, integration-tests, static-analysis, security-scan]
    runs-on: ubuntu-latest
    steps:
      - name: Check quality gate
        run: python scripts/check_quality_gate.py
```

---

[← Anterior: Roles & Interactions](05-roles-interactions.md) | [Siguiente: Architecture →](07-architecture.md)
