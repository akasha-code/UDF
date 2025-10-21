# 16) Unified Test Strategy (UTS)

## 16.1 Propósito

El **Unified Test Strategy (UTS)** es el subsistema del UDF dedicado a la planificación, selección y ejecución de pruebas. Su misión es asegurar que todas las técnicas de testeo —desde las más simples hasta las más avanzadas— tengan un lugar dentro del marco, y que su aplicación sea proporcional a la complejidad, criticidad y cadencia del proyecto (PDI, QEI, DSI, TTI).

---

## 16.2 Clasificación general de técnicas

Las técnicas se agrupan en tres capas principales:

### A. Pruebas de caja y visibilidad del sistema

#### Black-box Testing
**Descripción:** Validación basada en comportamiento observable sin conocimiento de implementación interna.

**Cuándo usar:**
- Validación funcional
- Testing de aceptación
- Validación de requisitos de negocio

**Técnicas asociadas:**
- Equivalence partitioning
- Boundary value analysis
- Decision tables
- State transition
- Use case testing

**Ventajas:**
- Perspectiva del usuario
- Independiente de implementación
- Fácil de entender para no-técnicos

**Limitaciones:**
- No valida lógica interna
- Puede perder casos edge internos

---

#### White-box Testing
**Descripción:** Validación basada en estructura interna del código.

**Cuándo usar:**
- Unit testing
- Code coverage analysis
- Security code review
- Performance optimization

**Técnicas asociadas:**
- Statement coverage
- Branch coverage
- Path coverage
- Condition coverage

**Ventajas:**
- Alta cobertura estructural
- Detecta lógica muerta
- Optimización de performance

**Limitaciones:**
- Requiere conocimiento técnico
- Puede perder perspectiva de usuario

---

#### Grey-box Testing
**Descripción:** Balance entre black-box y white-box; conocimiento parcial de estructura.

**Cuándo usar:**
- Integration testing
- API testing
- Database testing
- Security testing

**Ventajas:**
- Balance entre perspectivas
- Eficiencia en cobertura
- Práctico para la mayoría de casos

---

#### Static Testing
**Descripción:** Análisis sin ejecutar código.

**Técnicas:**
- Code reviews
- Inspections
- Walkthroughs
- Static analysis tools (SonarQube, ESLint)

**Ventajas:**
- Detecta problemas temprano
- No requiere entorno de ejecución
- Económico

---

#### Dynamic Testing
**Descripción:** Validación ejecutando código con datos reales.

**Todas las técnicas de ejecución caen aquí:**
- Unit, Integration, System, E2E, Performance, etc.

---

### B. Pruebas funcionales y estructurales

#### Unit Testing
**Objetivo:** Validar componentes individuales aislados.

**Herramientas:**
- Jest (JavaScript/TypeScript)
- JUnit (Java)
- pytest (Python)
- NUnit (C#)
- Go test (Go)

**Best Practices:**
- Test una cosa a la vez
- Usar mocks para dependencias
- Tests rápidos (<100ms)
- Cobertura >75%

**Ejemplo:**
```javascript
describe('Calculator', () => {
  test('adds two numbers correctly', () => {
    const result = add(2, 3);
    expect(result).toBe(5);
  });
  
  test('handles negative numbers', () => {
    const result = add(-2, 3);
    expect(result).toBe(1);
  });
});
```

---

#### Integration Testing
**Objetivo:** Validar interacción entre componentes.

**Herramientas:**
- TestContainers (Docker-based)
- Postman/Newman (API)
- REST Assured (Java)
- Supertest (Node.js)

**Niveles:**
- Component integration (2-3 components)
- System integration (multiple subsystems)
- External integration (3rd party services)

**Ejemplo:**
```yaml
# integration_test.yaml
test: user_registration_flow
steps:
  - call: POST /api/users
    body:
      email: test@example.com
      password: securepass123
    expect:
      status: 201
      
  - call: POST /api/auth/login
    body:
      email: test@example.com
      password: securepass123
    expect:
      status: 200
      body.token: exists
```

---

#### System Testing
**Objetivo:** Validar sistema completo end-to-end.

**Aspectos validados:**
- Funcionalidad completa
- Integración de todos los componentes
- Configuraciones de producción
- Data flow completo

**Herramientas:**
- Playwright
- Cypress
- Selenium
- Puppeteer

---

#### Acceptance Testing / UAT
**Objetivo:** Validar que el sistema cumple necesidades de negocio.

**Tipos:**
- User Acceptance Testing (UAT)
- Operational Acceptance Testing (OAT)
- Contract Acceptance Testing
- Compliance/Regulatory Acceptance

**Proceso:**
1. Define acceptance criteria
2. Create test scenarios from user perspective
3. Execute with business stakeholders
4. Document results and sign-off

---

#### End-to-End Testing
**Objetivo:** Validar flujos completos de usuario en ambiente similar a producción.

**Características:**
- Real databases
- External services (or mocks)
- Full authentication
- Complete workflows

**Ejemplo de flujo:**
```
E2E: Purchase Flow
1. User lands on homepage
2. Search for product
3. Add to cart
4. Checkout
5. Enter payment details
6. Confirm order
7. Receive confirmation email
8. Verify order in admin panel
```

---

#### Regression Testing
**Objetivo:** Asegurar que cambios no rompieron funcionalidad existente.

**Estrategia:**
- Automatizar casos críticos (>80%)
- Ejecutar en cada release
- Priorizar por riesgo y uso
- Mantener suite actualizada

**Optimización:**
- Parallel execution
- Smart test selection (only affected tests)
- Test impact analysis

---

#### Smoke Testing
**Objetivo:** Validación rápida de funcionalidad crítica básica.

**Características:**
- Tests superficiales pero amplios
- Ejecución rápida (<5 min)
- Bloquea si falla (no vale la pena testing profundo)

**Ejemplo:**
```markdown
Smoke Test Suite:
- [ ] Application starts
- [ ] Homepage loads
- [ ] User can login
- [ ] Critical API endpoints respond
- [ ] Database connection works
```

---

### C. Pruebas especializadas y de propósito

#### Performance Testing

##### Load Testing
**Objetivo:** Validar comportamiento bajo carga esperada.

**Herramientas:**
- k6
- JMeter
- Gatling
- Locust

**Métricas:**
- Response time (p50, p95, p99)
- Throughput (req/s)
- Error rate
- Resource utilization

**Ejemplo k6:**
```javascript
import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
  stages: [
    { duration: '2m', target: 100 }, // Ramp-up
    { duration: '5m', target: 100 }, // Sustained
    { duration: '2m', target: 0 },   // Ramp-down
  ],
  thresholds: {
    http_req_duration: ['p(95)<500'], // 95% < 500ms
    http_req_failed: ['rate<0.01'],   // <1% errors
  },
};

export default function () {
  let res = http.get('https://api.example.com/products');
  check(res, {
    'status 200': (r) => r.status === 200,
    'response time OK': (r) => r.timings.duration < 500,
  });
  sleep(1);
}
```

##### Stress Testing
**Objetivo:** Encontrar límites del sistema.

**Características:**
- Incrementar carga gradualmente
- Identificar breaking point
- Validar degradación graceful
- Recovery testing

##### Spike Testing
**Objetivo:** Validar comportamiento con picos súbitos.

##### Endurance/Soak Testing
**Objetivo:** Validar estabilidad prolongada.
- Duración: 8-24 horas
- Detectar memory leaks
- Degradación gradual

---

#### Security Testing

##### Vulnerability Scanning
**Herramientas:**
- Snyk
- OWASP Dependency-Check
- Trivy
- npm audit / pip-audit

**Frecuencia:** Continua (cada build)

##### Penetration Testing
**Objetivo:** Simular ataque real.

**Tipos:**
- Black-box (sin conocimiento)
- White-box (con código)
- Grey-box (conocimiento parcial)

**Herramientas:**
- Burp Suite
- OWASP ZAP
- Metasploit

##### Fuzz Testing
**Objetivo:** Inputs aleatorios para encontrar crashes.

**Herramientas:**
- AFL (American Fuzzy Lop)
- libFuzzer
- Jazzer (Java)

**Ejemplo:**
```python
# Simple fuzzer
import random
import string

def fuzz_test(function, iterations=1000):
    for i in range(iterations):
        input_data = ''.join(
            random.choices(
                string.ascii_letters + string.digits + string.punctuation,
                k=random.randint(1, 100)
            )
        )
        try:
            function(input_data)
        except Exception as e:
            print(f"Crash with input: {input_data}")
            print(f"Error: {e}")
```

##### Security Code Review
**Checklist:**
- Input validation
- SQL injection prevention
- XSS prevention
- CSRF protection
- Authentication/authorization
- Cryptography usage
- Secret management

---

#### Usability Testing
**Objetivo:** Validar experiencia de usuario.

**Métodos:**
- User interviews
- A/B testing
- Heatmaps
- Session recordings
- Think-aloud protocol

**Métricas:**
- Task completion rate
- Time on task
- Error rate
- Satisfaction score (SUS)

---

#### Accessibility Testing
**Objetivo:** Validar accesibilidad (WCAG compliance).

**Herramientas:**
- axe DevTools
- WAVE
- Lighthouse
- Screen readers (NVDA, JAWS)

**Aspectos:**
- Keyboard navigation
- Screen reader compatibility
- Color contrast
- Alt text for images
- ARIA labels

---

#### Compatibility Testing
**Objetivo:** Validar funcionamiento en diferentes entornos.

**Dimensiones:**
- Browsers (Chrome, Firefox, Safari, Edge)
- OS (Windows, macOS, Linux, iOS, Android)
- Devices (desktop, tablet, mobile)
- Screen sizes / resolutions

**Herramientas:**
- BrowserStack
- Sauce Labs
- LambdaTest

---

#### Exploratory Testing
**Objetivo:** Descubrimiento de defectos sin scripts.

**Características:**
- Simultaneous learning, test design, execution
- Charter-based (time-boxed sessions)
- Requires skilled testers

**Session Template:**
```markdown
# Exploratory Testing Session

**Charter:** Explore checkout flow focusing on edge cases
**Tester:** Jane Doe
**Date:** 2025-10-21
**Duration:** 90 minutes

## Areas Explored
- Cart with 0 items
- Cart with 100+ items
- Invalid coupon codes
- Expired payment methods
- Network interruption during payment

## Findings
1. Bug: Cart crashes with 150+ items
2. UX Issue: No feedback on invalid coupon
3. Enhancement: Could show estimated delivery earlier

## Coverage
- Checkout flow: 80%
- Edge cases: 60%
- Error handling: 70%
```

---

#### Boundary Value Analysis
**Objetivo:** Testar valores en los límites.

**Ejemplo:**
```
Campo: Age (valid range: 18-65)
Test values:
- 17 (just below min)
- 18 (min valid)
- 19 (just above min)
- 64 (just below max)
- 65 (max valid)
- 66 (just above max)
```

---

#### Equivalence Partitioning
**Objetivo:** Dividir inputs en clases equivalentes.

**Ejemplo:**
```
Campo: Discount code
Partitions:
1. Valid codes → Test: "SAVE20"
2. Expired codes → Test: "OLD2020"
3. Invalid format → Test: "abc"
4. Empty → Test: ""
5. SQL injection → Test: "'; DROP TABLE--"
```

---

#### Decision Table Testing
**Objetivo:** Validar todas las combinaciones de condiciones.

**Ejemplo:**
```
| Condition          | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 |
| ------------------ | -- | -- | -- | -- | -- | -- | -- | -- |
| User logged in?    | Y  | Y  | Y  | Y  | N  | N  | N  | N  |
| Has items in cart? | Y  | Y  | N  | N  | Y  | Y  | N  | N  |
| Has valid payment? | Y  | N  | Y  | N  | Y  | N  | Y  | N  |
| **Action**         | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
```

---

#### State Transition Testing
**Objetivo:** Validar cambios de estado.

**Ejemplo:**
```
Order States:
Created → Paid → Shipped → Delivered → Closed

Invalid transitions to test:
- Created → Shipped (skip payment)
- Delivered → Paid (backwards)
- Closed → Shipped (after closed)
```

---

#### Property-based Testing
**Objetivo:** Validar propiedades invariantes con inputs generados.

**Herramientas:**
- QuickCheck (Haskell)
- Hypothesis (Python)
- fast-check (JavaScript)

**Ejemplo:**
```python
from hypothesis import given
import hypothesis.strategies as st

@given(st.integers(), st.integers())
def test_addition_commutative(a, b):
    assert add(a, b) == add(b, a)

@given(st.lists(st.integers()))
def test_reverse_twice_is_identity(lst):
    assert reverse(reverse(lst)) == lst
```

---

#### Combinatorial Testing
**Objetivo:** Testar todas las combinaciones relevantes de parámetros.

**Herramientas:**
- PICT (Microsoft)
- ACTS (NIST)

**Ejemplo:**
```
Parameters:
- Browser: Chrome, Firefox, Safari
- OS: Windows, macOS, Linux
- Resolution: 1920x1080, 1366x768, 2560x1440

Traditional: 3 × 3 × 3 = 27 tests
Pairwise: ~9 tests (covers all pairs)
```

---

#### AI/ML Model Testing

##### Data Validation
**Objetivo:** Validar calidad de datos de entrenamiento.

**Herramientas:**
- Great Expectations
- Pandera
- Deequ

**Checks:**
- Schema validation
- Null values
- Outliers
- Distribution shifts

##### Model Bias Detection
**Objetivo:** Detectar sesgos en predicciones.

**Técnicas:**
- Fairness metrics (demographic parity, equal opportunity)
- Subgroup analysis
- Counterfactual testing

##### Explainability Testing
**Objetivo:** Validar que modelo es interpretable.

**Herramientas:**
- SHAP
- LIME
- InterpretML

##### Drift Detection
**Objetivo:** Detectar degradación del modelo en producción.

**Tipos:**
- Data drift (input distribution changes)
- Concept drift (relationship X→Y changes)
- Prediction drift (output distribution changes)

**Herramientas:**
- Evidently AI
- Alibi Detect
- NannyML

---

## 16.3 Entornos de aplicación

| Tipo de sistema                                                   | Técnicas recomendadas                                                                      |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **Software de aplicación (web, móvil)**                           | Black-box, Unit, Integration, Regression, Usability, Security, Performance                 |
| **Sistemas embebidos / hardware-software**                        | White-box, State transition, Boundary, Stress, Fuzz, Property-based                        |
| **Sistemas críticos o regulados (GxP, aeroespacial, financiero)** | Full V-Model: URS–SRS trace, Validation protocol, System & Acceptance Testing, Audit trail |
| **Sistemas IA / ML**                                              | Property-based, Differential, Data validation, Bias detection, Explainability testing      |
| **Plataformas de datos / APIs**                                   | Integration, Contract, Security, Performance, Combinatorial, Exploratory                   |

---

## 16.4 Assessment y superposición de técnicas

Las técnicas pueden **superponerse** según el enfoque. El framework propone un *Assessment Matrix* para entender compatibilidades, equivalencias y redundancias.

| Técnica                         | Equivalente o compatible con    | Comentario                                                                          |
| ------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------- |
| **Black-box**                   | Boundary, Equivalence, Use-case | Enfoque de comportamiento; se puede combinar con decisión o estado.                 |
| **White-box**                   | Unit, Integration               | Evalúa cobertura interna; complementa black-box.                                    |
| **Grey-box**                    | Black + White                   | Balance entre validación funcional y técnica.                                       |
| **Exploratory**                 | Check-list, Session-based       | Complementa pruebas automatizadas; no sustituye cobertura formal.                   |
| **Boundary Value**              | Equivalence partitioning        | Ambas enfocadas en validación de dominios; la segunda más general.                  |
| **Decision Table**              | State transition                | La primera es estática, la segunda dinámica.                                        |
| **System / Regression**         | Integration, UAT                | Solapan en cobertura; se diferencian en propósito.                                  |
| **Performance / Load / Stress** | Integration                     | Miden confiabilidad y escalabilidad; complementan pero no reemplazan funcionalidad. |
| **Fuzz / Security**             | Penetration                     | Fuzz busca robustez; penetration evalúa vulnerabilidad.                             |
| **Property-based**              | Random, Differential            | Recomendado para IA o cálculos complejos; requiere automatización.                  |

> **Regla de oro:** la superposición no es problema si cada técnica aporta un ángulo distinto (funcionalidad, estructura, rendimiento, seguridad). La redundancia negativa ocurre cuando dos técnicas prueban exactamente el mismo comportamiento sin aportar evidencia adicional.

---

## 16.5 Selección guiada de técnicas

La selección de técnicas se rige por las variables del proyecto:

| Contexto           | Técnicas mínimas                       | Técnicas recomendadas                  |
| ------------------ | -------------------------------------- | -------------------------------------- |
| XS / Low Quality   | Smoke, Unit, Exploratory               | Boundary, Regression                   |
| M / Medium Quality | Integration, System, Regression        | Usability, Performance                 |
| L / High Quality   | Full trace V&V, Security, Stress, Fuzz | Combinatorial, Property-based          |
| XL / Regulated     | V-Model completo, Audit trail          | Validation protocol, Acceptance formal |

### Test Strategy Configuration

```yaml
# test_strategy.yaml
project:
  name: "E-commerce Platform"
  pdi: L
  qei: high
  dsi: 3
  domain: web_application
  criticality: high

test_techniques:
  functional:
    - unit_testing:
        enabled: true
        coverage_target: 85%
        frameworks: [jest, pytest]
        
    - integration_testing:
        enabled: true
        coverage_target: 75%
        frameworks: [testcontainers, supertest]
        
    - system_testing:
        enabled: true
        frameworks: [playwright]
        critical_flows: 100%
        
    - regression_testing:
        enabled: true
        automation_rate: 90%
        execution: every_release
        
  non_functional:
    - performance_testing:
        enabled: true
        types: [load, stress, spike]
        framework: k6
        frequency: weekly
        
    - security_testing:
        enabled: true
        types: [vulnerability_scan, penetration, fuzz]
        tools: [snyk, owasp-zap]
        frequency: continuous
        
    - usability_testing:
        enabled: true
        methods: [user_interviews, a_b_testing]
        frequency: monthly
        
  specialized:
    - exploratory_testing:
        enabled: true
        session_duration: 90min
        frequency: weekly
        
    - accessibility_testing:
        enabled: true
        standard: WCAG_2.1_AA
        tools: [axe, lighthouse]
        
validation:
  entry_criteria:
    - code_review_approved
    - unit_tests_passed
    - static_analysis_clean
    
  exit_criteria:
    - all_tests_passed
    - coverage_thresholds_met
    - no_critical_defects
    - performance_baselines_met
```

---

## 16.6 Artefactos UTS

* **`test_strategy.yaml`** – define técnicas y criterios de activación
* **`test_matrix.csv`** – mapeo de requerimiento ↔ caso ↔ técnica ↔ evidencia
* **`validation_manifest.yaml`** – amplía definición de herramientas y frameworks
* **`qa_gate_policy.md`** – define políticas de aprobación por fase
* **`test_catalog.md`** – catálogo completo de técnicas, objetivos, precondiciones y herramientas sugeridas

### Test Matrix Example

```csv
Requirement_ID,Test_Case_ID,Technique,Priority,Automation,Status,Evidence
US-001,TC-001,Unit,High,Yes,Passed,coverage_report.html
US-001,TC-002,Integration,High,Yes,Passed,api_test_results.json
US-001,TC-003,E2E,Critical,Yes,Passed,playwright_report.html
US-002,TC-004,Unit,Medium,Yes,Passed,coverage_report.html
US-002,TC-005,Exploratory,Medium,No,Passed,session_notes.md
US-003,TC-006,Performance,High,Yes,Passed,k6_results.json
US-003,TC-007,Security,Critical,Yes,Passed,snyk_report.pdf
```

---

## 16.7 Integración con CI/CD y THI

Los pipelines CI/CD consumen `test_strategy.yaml` para ejecutar pruebas según nivel QEI.

```yaml
# .github/workflows/test-pipeline.yml
name: Test Pipeline

on: [push, pull_request]

jobs:
  unit-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run unit tests
        run: npm test -- --coverage
      - name: Upload coverage
        uses: codecov/codecov-action@v3

  integration-tests:
    runs-on: ubuntu-latest
    needs: unit-tests
    steps:
      - uses: actions/checkout@v3
      - name: Start services
        run: docker-compose up -d
      - name: Run integration tests
        run: npm run test:integration

  e2e-tests:
    runs-on: ubuntu-latest
    needs: integration-tests
    steps:
      - uses: actions/checkout@v3
      - name: Run E2E tests
        run: npm run test:e2e

  performance-tests:
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v3
      - name: Run k6 tests
        run: k6 run tests/performance/load-test.js

  security-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run Snyk
        run: snyk test --severity-threshold=high

  calculate-thi:
    needs: [unit-tests, integration-tests, security-tests]
    runs-on: ubuntu-latest
    steps:
      - name: Calculate Technical Health Index
        run: python scripts/calculate_thi.py
      - name: Update dashboard
        run: python scripts/update_dashboard.py
```

Los resultados alimentan el *Technical Health Index* (THI) y el `stage_review_board.md`, integrando testing y gobernanza de forma automatizada.

---

## 16.8 Filosofía del UTS

* **Universalidad:** Todas las técnicas tienen cabida; el framework nunca excluye ninguna
* **Contextualidad:** Cada técnica se activa por necesidad, riesgo o tipo de sistema
* **Escalabilidad:** Permite comenzar con lo mínimo y crecer hacia validaciones formales
* **No redundancia:** La superposición se gestiona mediante Assessment Matrix
* **Transparencia:** Cada decisión de prueba queda documentada, automatizada o justificada
* **Pragmatismo:** Probar lo necesario, no probar por probar
* **Automatización:** Maximizar automatización manteniendo balance con exploratory

> En síntesis: el UTS convierte el testing en una disciplina de diseño y evidencia, no de postvalidación. Su propósito no es probar más, sino **probar mejor**, alineando esfuerzo de validación con el valor y el riesgo del sistema.

---

[← Anterior: Synthesis](15-synthesis.md) | [Volver al Overview](00-overview.md)
