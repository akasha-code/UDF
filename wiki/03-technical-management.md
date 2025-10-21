# 3) Gestión técnica y CI/CD

La gestión técnica en el UDF se basa en métricas objetivas, automatización y control de calidad continuo. El objetivo es garantizar que cada Stage Review (SR) tenga evidencia cuantitativa del estado de salud técnica del producto.

---

## Technical Health Index (THI)

El **Technical Health Index** es el indicador principal de la salud técnica del proyecto. Se compone de múltiples dimensiones:

### Componentes del THI

1. **Code Coverage**
   - Cobertura de pruebas unitarias
   - Cobertura de pruebas de integración
   - Cobertura de ramas (branch coverage)

2. **Technical Debt**
   - Índice de deuda técnica (SonarQube)
   - Tiempo estimado de remediation
   - Tendencia de deuda (creciente/decreciente)

3. **Code Quality**
   - Complejidad ciclomática
   - Duplicación de código
   - Violaciones de estándares (linting)

4. **Stability Metrics**
   - Tasa de defectos
   - Mean Time To Recovery (MTTR)
   - Frecuencia de hotfixes

### Cálculo del THI

```
THI = (Coverage_Score × 0.25) + 
      (Debt_Score × 0.25) + 
      (Quality_Score × 0.25) + 
      (Stability_Score × 0.25)

Donde cada score se normaliza a escala 0-100
```

### Umbrales por QEI

| QEI Level | THI Mínimo | Coverage Mínima | Debt Máximo |
| --------- | ---------- | --------------- | ----------- |
| **Low**   | 60         | 60%             | High        |
| **Medium**| 75         | 75%             | Medium      |
| **High**  | 85         | 85%             | Low         |

---

## Integración CI/CD

El UDF se integra con pipelines de integración y despliegue continuo para automatizar la validación técnica.

### Validation Manifest

El archivo `validation_manifest.yaml` define las validaciones a ejecutar en cada fase:

```yaml
# validation_manifest.yaml
version: 1.0
project:
  name: "MyProject"
  pdi: M
  qei: medium
  
validations:
  unit_tests:
    enabled: true
    framework: jest
    coverage_threshold: 75
    path: "./tests/unit"
    
  integration_tests:
    enabled: true
    framework: pytest
    coverage_threshold: 70
    path: "./tests/integration"
    
  ui_tests:
    enabled: true
    framework: playwright
    path: "./tests/e2e"
    
  static_analysis:
    enabled: true
    tools:
      - sonarqube
      - eslint
      - prettier
    quality_gate: "medium"
    
  security_scan:
    enabled: true
    tools:
      - snyk
      - owasp-dependency-check
    severity_threshold: "high"
    
  performance_tests:
    enabled: false
    framework: k6
    thresholds:
      response_time_p95: 500ms
      error_rate: 1%

gates:
  sr_e:
    - unit_tests
    - integration_tests
    - static_analysis
    - security_scan
  sr_b:
    - all_validations
    - uat_signoff
```

### Pipeline Integration

#### GitHub Actions Example

```yaml
# .github/workflows/udf-validation.yml
name: UDF Validation

on:
  pull_request:
    branches: [main, develop]
  push:
    branches: [main]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Load Validation Manifest
        run: |
          yq eval '.validations' validation_manifest.yaml
      
      - name: Run Unit Tests
        run: npm test -- --coverage
      
      - name: Run Integration Tests
        run: npm run test:integration
      
      - name: Static Analysis
        run: |
          npm run lint
          sonar-scanner
      
      - name: Security Scan
        run: npm audit
      
      - name: Calculate THI
        run: |
          python scripts/calculate_thi.py
      
      - name: Generate Technical Health Report
        run: |
          python scripts/generate_health_report.py > technical_health_report.md
      
      - name: Upload Reports
        uses: actions/upload-artifact@v3
        with:
          name: quality-reports
          path: |
            technical_health_report.md
            coverage/
```

#### GitLab CI Example

```yaml
# .gitlab-ci.yml
stages:
  - test
  - quality
  - report

variables:
  VALIDATION_MANIFEST: "validation_manifest.yaml"

unit_tests:
  stage: test
  script:
    - npm test -- --coverage
  coverage: '/All files[^|]*\|[^|]*\s+([\d\.]+)/'

integration_tests:
  stage: test
  script:
    - npm run test:integration

static_analysis:
  stage: quality
  script:
    - npm run lint
    - sonar-scanner

security_scan:
  stage: quality
  script:
    - npm audit
    - snyk test

generate_thi:
  stage: report
  script:
    - python scripts/calculate_thi.py
    - python scripts/generate_health_report.py
  artifacts:
    paths:
      - technical_health_report.md
```

---

## QA Gates

Los **QA Gates** son puntos de control automatizados que deben superarse para avanzar entre fases.

### Gate Configuration

```yaml
# qa_gate_policy.yaml
gates:
  build:
    name: "Build Quality Gate"
    conditions:
      - type: coverage
        metric: unit_test_coverage
        threshold: 75
        operator: gte
      - type: quality
        metric: sonar_quality_gate
        value: PASSED
      - type: security
        metric: critical_vulnerabilities
        threshold: 0
        operator: eq
        
  validation:
    name: "Business Validation Gate"
    conditions:
      - type: coverage
        metric: integration_test_coverage
        threshold: 70
        operator: gte
      - type: uat
        metric: uat_approval
        value: APPROVED
      - type: thi
        metric: technical_health_index
        threshold: 75
        operator: gte
```

---

## Herramientas recomendadas

### Testing
* **Unit Testing:** Jest, JUnit, pytest, NUnit
* **Integration Testing:** TestContainers, Postman, REST Assured
* **E2E Testing:** Playwright, Cypress, Selenium
* **Performance:** k6, JMeter, Gatling
* **AI/ML Testing:** Great Expectations, Evidently AI

### Quality Analysis
* **Static Analysis:** SonarQube, CodeClimate, Codacy
* **Linting:** ESLint, Pylint, RuboCop, Checkstyle
* **Security:** Snyk, OWASP Dependency-Check, Trivy
* **Complexity:** Lizard, radon, Code Metrics

### Monitoring & Observability
* **Metrics:** Prometheus, Datadog, New Relic
* **Logging:** ELK Stack, Splunk, Loki
* **Tracing:** Jaeger, Zipkin, OpenTelemetry
* **Dashboards:** Grafana, Kibana

---

## Technical Health Report

El reporte de salud técnica se genera automáticamente y se presenta en cada Stage Review:

```markdown
# Technical Health Report

**Project:** MyProject
**Date:** 2025-10-21
**Phase:** Build (SR-E)

## Technical Health Index: 78/100 ✅

### Metrics

| Metric                    | Value  | Target | Status |
| ------------------------- | ------ | ------ | ------ |
| Unit Test Coverage        | 82%    | 75%    | ✅      |
| Integration Test Coverage | 71%    | 70%    | ✅      |
| Technical Debt Ratio      | 3.5%   | <5%    | ✅      |
| Code Duplication          | 2.1%   | <3%    | ✅      |
| Critical Issues           | 0      | 0      | ✅      |
| High Issues               | 2      | <5     | ✅      |
| Cyclomatic Complexity     | 8.2    | <10    | ✅      |

### Trend Analysis
- Coverage: ↑ +5% vs last SR
- Technical Debt: ↓ -1.2% vs last SR
- Defect Rate: → stable

### Recommendations
1. Address 2 high-priority security issues
2. Increase integration test coverage to 75%
3. Refactor 3 high-complexity modules

### Gate Status: **PASSED** ✅
```

---

## Automatización y Tooling

El UDF promueve la automatización máxima de validaciones técnicas:

* **Pre-commit hooks:** Validación local antes de commits
* **PR checks:** Validación automática en pull requests
* **Scheduled scans:** Análisis periódicos de seguridad y calidad
* **Release gates:** Validación obligatoria antes de releases

---

[← Anterior: Artifacts](02-artifacts.md) | [Siguiente: Governance →](04-governance.md)
