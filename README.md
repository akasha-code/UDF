# Unified Delivery Framework (UDF)

Diseño de un marco híbrido, pragmático y trazable que cruza ICONIX con las mejores prácticas de gobierno, calidad y entrega. Compatible con PMBOK, PRINCE2 y SAFe, integra métricas técnicas, artefactos YAML, control de calidad automatizado, gobernanza y aprendizaje continuo.

## 📚 Documentación

La documentación completa del UDF está disponible en el directorio [wiki/](wiki/):

### Contenido Principal

0. **[Overview](wiki/00-overview.md)** - Resumen ejecutivo y navegación
1. **[Fases del ciclo de vida](wiki/01-lifecycle-phases.md)** - Initiation, Planning, Build, Validation, Operation, Closure
2. **[Artefactos principales](wiki/02-artifacts.md)** - Plantillas y documentos estándar
3. **[Gestión técnica y CI/CD](wiki/03-technical-management.md)** - Technical Health Index, automation
4. **[Gobierno y Project Management](wiki/04-governance.md)** - Stage Reviews, control de cambios
5. **[Roles, Interacciones y Responsabilidades](wiki/05-roles-interactions.md)** - RACI, topologías de equipo
6. **[Calidad y pruebas](wiki/06-quality-testing.md)** - QEI, Quality Charter, testing
7. **[Arquitectura y observabilidad](wiki/07-architecture.md)** - ADRs, SLOs, monitoring
8. **[Producto y valor](wiki/08-product-value.md)** - User stories, outcome metrics
9. **[Portfolio y planificación](wiki/09-portfolio.md)** - OKRs, roadmaps, multi-proyecto
10. **[Learning Loop activo](wiki/10-learning-loop.md)** - Captura de aprendizajes
11. **[Delivery Cube (PDI–DSI–QEI–TTI)](wiki/11-delivery-cube.md)** - Configuración del framework
12. **[Gobierno y aprendizaje](wiki/12-governance-learning.md)** - Stage Reviews detallados
13. **[Testing, riesgo y madurez](wiki/13-testing-risk-maturity.md)** - Gestión proporcional
14. **[Plan de adopción](wiki/14-adoption-plan.md)** - Roadmap de implementación
15. **[Síntesis](wiki/15-synthesis.md)** - Resumen integral del UDF
16. **[Unified Test Strategy (UTS)](wiki/16-unified-test-strategy.md)** - Estrategia completa de testing

## 🚀 Quick Start

### 1. Evalúa tu contexto

Determina tu configuración inicial:
- **PDI** (Depth): XS, S, M, L, XL - ¿Cuánta profundidad documental necesitas?
- **DSI** (Structure): 1-5 - ¿Qué tan iterativo es tu proceso?
- **QEI** (Quality): Low, Medium, High - ¿Cuánto énfasis en calidad?
- **TTI** (Topology): Integrated, Dedicated, External - ¿Cómo se estructura tu equipo?

### 2. Comienza con lo mínimo

Para un proyecto básico (PDI: XS):
```
project/
├── charter.md                    # Visión y alcance
├── user-stories/                 # Requisitos
├── tests.csv                     # Plan de pruebas
├── technical_health_report.md    # Métricas técnicas
└── stage_review_board.md         # Decisiones y governance
```

### 3. Ejecuta tu primer Stage Review

- Usa las plantillas en `wiki/04-governance.md`
- Revisa objetivos, entregables y criterios Go/No-Go
- Documenta decisiones

### 4. Mide y aprende

- Calcula tu Technical Health Index (THI)
- Captura aprendizajes en `learning/`
- Ajusta tu configuración según resultados

## 💡 Casos de uso

### Startup MVP
```yaml
pdi: XS
dsi: 5
qei: low
tti: integrated
# Enfoque: velocidad, aprendizaje, iteración rápida
```

### Producto Corporativo
```yaml
pdi: M
dsi: 3
qei: medium
tti: integrated
# Enfoque: balance agilidad-control, calidad estándar
```

### Sistema Regulado
```yaml
pdi: XL
dsi: 1
qei: high
tti: external
# Enfoque: compliance, trazabilidad completa, V-Model
```

## 🎯 Beneficios clave

- ✅ **Trazabilidad completa** desde requisitos hasta valor entregado
- ✅ **Decisiones basadas en evidencia** mediante THI y métricas
- ✅ **Adaptable** a cualquier metodología (Agile, Waterfall, DevOps, V-Model)
- ✅ **Configurable** según contexto y madurez
- ✅ **Aprendizaje continuo** incorporado en el proceso
- ✅ **Interoperable** con PMBOK, PRINCE2, SAFe, ISO

## 🔧 Herramientas recomendadas

- **Documentación:** Markdown, PlantUML, YAML
- **CI/CD:** GitHub Actions, GitLab CI, Jenkins
- **Quality:** SonarQube, Snyk, ESLint
- **Testing:** Jest, Playwright, k6, TestContainers
- **Monitoring:** Prometheus, Grafana, ELK Stack
- **Project Management:** JIRA, Linear, GitHub Projects

## 📖 Recursos adicionales

- [Plan de adopción paso a paso](wiki/14-adoption-plan.md)
- [Unified Test Strategy completa](wiki/16-unified-test-strategy.md)
- [Ejemplos de V-Model en contextos regulados](wiki/05-roles-interactions.md#55-ejemplo-operativo-de-v-model-dentro-del-udf)
- [Calculadora de madurez organizacional](wiki/13-testing-risk-maturity.md#madurez-organizacional)

## 🤝 Contribución

El UDF es un **living framework** que evoluciona con feedback de la comunidad. Sugerencias y mejoras son bienvenidas.

## 📄 Licencia

Ver archivo [LICENSE](LICENSE) para detalles.

---

> "El UDF no te dice **qué** construir, te da **cómo** construir con evidencia, trazabilidad y aprendizaje continuo."
