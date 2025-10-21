# 7) Arquitectura y observabilidad

El control arquitectónico en el UDF garantiza decisiones técnicas alineadas con requisitos de negocio, escalabilidad, mantenibilidad y cumplimiento. La observabilidad asegura que el sistema sea monitoreado y medido continuamente.

---

## Architecture Governance Matrix

El `architecture_governance_matrix.md` define roles, responsabilidades y procesos de gobernanza arquitectónica:

```markdown
# Architecture Governance Matrix

## Roles Arquitectónicos

| Rol                      | Responsabilidad                                                 | Ámbito        |
| ------------------------ | --------------------------------------------------------------- | ------------- |
| **Enterprise Architect** | Estándares corporativos, alineación estratégica                 | Organización  |
| **Solution Architect**   | Diseño de solución end-to-end, integración entre sistemas       | Programa/Proyecto |
| **Application Architect**| Diseño de aplicación, patrones, frameworks                      | Aplicación    |
| **Data Architect**       | Modelos de datos, integridad, governance de datos               | Datos         |
| **Security Architect**   | Seguridad, compliance, privacidad                               | Seguridad     |
| **Cloud/Infra Architect**| Infraestructura, cloud, redes, despliegue                       | Plataforma    |

## Áreas de control

### 1. Estándares y patrones
- **Patrones de diseño aprobados**
- **Stack tecnológico permitido**
- **Frameworks y librerías corporativas**
- **Convenciones de código**

### 2. Decisiones arquitectónicas
- **Architecture Decision Records (ADRs)**
- **Trade-offs y alternativas evaluadas**
- **Justificación técnica y de negocio**
- **Riesgos y mitigaciones**

### 3. Calidad y no funcionales
- **Performance requirements**
- **Scalability patterns**
- **Security requirements**
- **Availability and resilience**

### 4. Integración y interoperabilidad
- **APIs y contratos**
- **Protocolos de comunicación**
- **Formatos de datos**
- **Event-driven patterns**

## Proceso de revisión

| Fase     | Revisión                   | Participantes             | Entregable            |
| -------- | -------------------------- | ------------------------- | --------------------- |
| SR-C     | Architecture Review        | Solution + App Architects | Architecture Overview |
| SR-E     | Technical Design Review    | Tech Lead + Dev Team      | Detailed Design + ADRs|
| SR-B     | Security & Compliance      | Security + QA             | Security Assessment   |
| SR-O     | Operational Readiness      | DevOps + Platform         | Runbook + Monitoring  |
```

---

## Architecture Decision Records (ADR)

Los ADRs documentan decisiones arquitectónicas significativas de forma inmutable.

### Template ADR

```markdown
# ADR-XXX: [Título de la Decisión]

**Estado:** [Propuesta / Aceptada / Rechazada / Deprecada / Supersedida por ADR-YYY]

**Fecha:** YYYY-MM-DD

**Contexto:** 
Describe el problema o necesidad que motiva esta decisión.
Incluye restricciones técnicas, de negocio o regulatorias.

**Decisión:**
Describe la decisión tomada de forma clara y concisa.

**Alternativas consideradas:**
1. **Alternativa 1:** [Descripción] - Rechazada porque [razón]
2. **Alternativa 2:** [Descripción] - Rechazada porque [razón]

**Consecuencias:**

**Positivas:**
- Consecuencia positiva 1
- Consecuencia positiva 2

**Negativas:**
- Consecuencia negativa 1 (aceptable porque [razón])
- Consecuencia negativa 2 (mitigada mediante [acción])

**Riesgos:**
- Riesgo 1: [Descripción] - Mitigación: [plan]
- Riesgo 2: [Descripción] - Mitigación: [plan]

**Aprobadores:**
- Tech Lead: [Nombre] - [Fecha]
- Solution Architect: [Nombre] - [Fecha]
- Security Architect: [Nombre] (si aplica) - [Fecha]

**Referencias:**
- [Link a documentación relevante]
- [Link a POC o spike]
- [Link a discusiones]
```

### Ejemplo ADR

```markdown
# ADR-001: Uso de PostgreSQL como base de datos principal

**Estado:** Aceptada

**Fecha:** 2025-10-15

**Contexto:**
El proyecto requiere una base de datos relacional que soporte:
- Transacciones ACID
- Consultas complejas con JOINs
- JSON storage para configuraciones
- Escalabilidad horizontal (futuro)
- Soporte de comunidad activo

**Decisión:**
Utilizaremos PostgreSQL 15+ como base de datos principal.

**Alternativas consideradas:**
1. **MySQL:** Rechazada por menor soporte de JSON y extensiones
2. **MongoDB:** Rechazada por requisitos de transacciones complejas
3. **SQLite:** Rechazada por limitaciones de concurrencia

**Consecuencias:**

**Positivas:**
- Soporte completo de SQL estándar
- JSON/JSONB nativo con indexación
- Extensiones (PostGIS, TimescaleDB) disponibles
- Ecosistema maduro de herramientas

**Negativas:**
- Mayor complejidad operativa vs SQLite
- Requiere servidor dedicado

**Riesgos:**
- Costo de hosting: Mitigado con RDS o managed services
- Curva de aprendizaje: Mitigado con capacitación

**Aprobadores:**
- Tech Lead: Jane Smith - 2025-10-15
- Solution Architect: John Doe - 2025-10-16

**Referencias:**
- [PostgreSQL vs MySQL comparison](link)
- [JSON support benchmark](link)
```

---

## SLOs y SLIs

Los Service Level Objectives (SLOs) definen targets medibles de calidad de servicio.

### SLO Definition

```yaml
# slos.yaml
slos:
  availability:
    objective: 99.9%
    measurement_window: 30d
    error_budget: 43m
    
  latency:
    p50: 100ms
    p95: 500ms
    p99: 1s
    measurement_window: 1h
    
  error_rate:
    objective: 0.1%
    measurement_window: 1h
    
  throughput:
    objective: 1000 req/s
    peak_capacity: 5000 req/s
    
slis:
  - name: http_request_duration
    type: histogram
    buckets: [0.01, 0.05, 0.1, 0.5, 1, 5]
    
  - name: http_request_errors
    type: counter
    labels: [status_code, endpoint]
    
  - name: service_availability
    type: gauge
    calculation: successful_requests / total_requests
```

---

## Observability Stack

### Tres pilares de observabilidad

#### 1. Metrics (Métricas)
* **Herramientas:** Prometheus, Datadog, New Relic
* **Tipos:**
  - RED: Rate, Errors, Duration
  - USE: Utilization, Saturation, Errors
  - Golden Signals: Latency, Traffic, Errors, Saturation

#### 2. Logs (Registros)
* **Herramientas:** ELK Stack, Splunk, Loki
* **Estructura:** Structured logging (JSON)
* **Niveles:** ERROR, WARN, INFO, DEBUG, TRACE

#### 3. Traces (Trazas)
* **Herramientas:** Jaeger, Zipkin, OpenTelemetry
* **Contexto:** Request tracing end-to-end
* **Sampling:** Head-based, tail-based

### Monitoring Configuration

```yaml
# monitoring.yaml
monitoring:
  metrics:
    provider: prometheus
    scrape_interval: 15s
    retention: 30d
    exporters:
      - node_exporter
      - postgres_exporter
      - application_exporter
      
  logging:
    provider: loki
    format: json
    retention: 90d
    levels:
      production: INFO
      staging: DEBUG
      
  tracing:
    provider: jaeger
    sampling_rate: 0.1
    retention: 7d
    
  alerting:
    provider: alertmanager
    channels:
      - slack: #alerts-prod
      - pagerduty: team-oncall
      - email: ops@example.com
```

---

## Dashboards

### Application Dashboard

```yaml
# grafana-dashboard.json
dashboard:
  title: "Application Health"
  panels:
    - title: "Request Rate"
      type: graph
      datasource: prometheus
      query: rate(http_requests_total[5m])
      
    - title: "Error Rate"
      type: graph
      datasource: prometheus
      query: rate(http_requests_total{status=~"5.."}[5m])
      
    - title: "P95 Latency"
      type: graph
      datasource: prometheus
      query: histogram_quantile(0.95, http_request_duration_seconds_bucket)
      
    - title: "Service Health (THI)"
      type: gauge
      datasource: prometheus
      query: technical_health_index
      thresholds: [60, 75, 85]
```

---

## Security Architecture

### Security Controls

| Control                  | Implementation                          | Validation        |
| ------------------------ | --------------------------------------- | ----------------- |
| Authentication           | OAuth2 / JWT                            | Security tests    |
| Authorization            | RBAC / ABAC                             | Access tests      |
| Encryption at rest       | AES-256                                 | Compliance scan   |
| Encryption in transit    | TLS 1.3+                                | SSL Labs scan     |
| Input validation         | Schema validation, sanitization         | Security tests    |
| SQL injection protection | Parameterized queries / ORM             | OWASP ZAP         |
| XSS protection           | Content Security Policy, escaping       | Security tests    |
| CSRF protection          | CSRF tokens                             | Security tests    |
| Rate limiting            | API Gateway / middleware                | Load tests        |
| Audit logging            | Immutable audit trail                   | Compliance review |

### Security Checklist

```markdown
# Security Checklist - SR-B

## Authentication & Authorization
- [ ] Passwords hasheados con bcrypt/argon2
- [ ] Tokens JWT con expiración adecuada
- [ ] MFA implementado para usuarios admin
- [ ] RBAC configurado correctamente
- [ ] Session management seguro

## Data Protection
- [ ] Datos sensibles encriptados at rest
- [ ] TLS 1.3 en todas las comunicaciones
- [ ] Backup encriptados
- [ ] PII identificado y protegido
- [ ] Data retention policy implementada

## Application Security
- [ ] Input validation en todos los endpoints
- [ ] SQL injection prevención verificada
- [ ] XSS protection implementada
- [ ] CSRF tokens en formularios
- [ ] Dependencies sin vulnerabilidades críticas

## Infrastructure Security
- [ ] Firewall configurado
- [ ] Ports innecesarios cerrados
- [ ] Secrets management (Vault, AWS Secrets)
- [ ] Network segmentation
- [ ] DDoS protection

## Compliance
- [ ] GDPR compliance (si aplica)
- [ ] HIPAA compliance (si aplica)
- [ ] SOC2 requirements (si aplica)
- [ ] Audit logging completo
- [ ] Incident response plan documentado
```

---

## Runbook

El runbook es el manual operativo del sistema:

```markdown
# Runbook - [System Name]

## System Overview
- **Purpose:** [Descripción]
- **Architecture:** [Diagrama o descripción]
- **Dependencies:** [Servicios externos, bases de datos, APIs]

## Deployment
- **Deployment Process:** [Pasos detallados]
- **Rollback Process:** [Pasos de rollback]
- **Configuration:** [Variables de entorno, secrets]

## Monitoring
- **Dashboard:** [Link a Grafana]
- **Alerts:** [Lista de alertas configuradas]
- **SLOs:** [Objetivos de servicio]

## Common Issues

### Issue: High memory usage
**Symptoms:** Memory > 80%, OOMKilled pods
**Diagnosis:** Check memory metrics in Grafana
**Resolution:** 
1. Check for memory leaks in logs
2. Restart service if necessary
3. Scale horizontally if sustained

### Issue: Database connection timeout
**Symptoms:** 504 errors, slow response
**Diagnosis:** Check DB connection pool metrics
**Resolution:**
1. Check DB health
2. Increase connection pool size
3. Check network connectivity

## Escalation
- **L1 Support:** DevOps on-call (Slack: #devops-oncall)
- **L2 Support:** Tech Lead (email: tech-lead@example.com)
- **L3 Support:** Architect (email: architect@example.com)

## Maintenance
- **Backup Schedule:** Daily at 2 AM UTC
- **Backup Retention:** 30 days
- **Patching Schedule:** Monthly, 3rd Sunday
```

---

[← Anterior: Quality & Testing](06-quality-testing.md) | [Siguiente: Product & Value →](08-product-value.md)
