# Wiki Content Directory

This directory contains the source documentation files for the UDF framework.

## Rol dentro de UDF

Esta carpeta conserva la referencia numerada y canónica del framework público. El contenido puede publicarse también en la [GitHub Wiki](https://github.com/akasha-code/UDF/wiki), pero el repositorio versionado es la fuente de verdad.

## Content Structure

The documentation follows a logical progression:

0. **00-overview.md** - Resumen ejecutivo y navegación
1. **01-lifecycle-phases.md** - Fases del ciclo de vida
2. **02-artifacts.md** - Artefactos principales
3. **03-technical-management.md** - Gestión técnica y CI/CD
4. **04-governance.md** - Gobierno y Project Management
5. **05-roles-interactions.md** - Roles, Interacciones y Responsabilidades
6. **06-quality-testing.md** - Calidad y pruebas
7. **07-architecture.md** - Arquitectura y observabilidad
8. **08-product-value.md** - Producto y valor
9. **09-portfolio.md** - Portfolio y planificación
10. **10-learning-loop.md** - Learning Loop activo
11. **11-delivery-cube.md** - Delivery Cube (PDI–DSI–QEI–TTI)
12. **12-governance-learning.md** - Gobierno y aprendizaje
13. **13-testing-risk-maturity.md** - Testing, riesgo y madurez
14. **14-adoption-plan.md** - Plan de adopción
15. **15-synthesis.md** - Síntesis
16. **16-unified-test-strategy.md** - Unified Test Strategy (UTS)
17. **17-interoperabilidad-y-automatizacion.md** - Núcleo vs extensiones; perfil agent-ready (handoff, estados, capacidades, gates)
18. **18-agencia-mandatos-intervenciones.md** - Actores, agentes, equipos, mandatos e intervenciones
19. **19-contexto-assurance-capacidades.md** - Context & Assurance Model y capacidades proporcionales
20. **20-arquitectura-agentic-e-integraciones.md** - Harnesses, guardrails, interfaces, RAG, staffing y testing
21. **21-documentacion-agent-ready.md** - Documentación para personas y sistemas agenticos
22. **22-alineacion-pmi-prince2-ia.md** - Alineación de gobierno y delivery con IA

## Publicación opcional en GitHub Wiki

To publish these files to the GitHub Wiki:

### Method 1: Manual Publishing (Web Interface)

1. Go to https://github.com/akasha-code/UDF/wiki
2. For each file, create or edit a wiki page
3. Copy the content from the corresponding markdown file
4. Save the page

### Method 2: Git Publishing (Command Line)

```bash
# Clone the wiki repository
git clone https://github.com/akasha-code/UDF.wiki.git

# Copy the documentation files
cp wiki/*.md UDF.wiki/

# Commit and push
cd UDF.wiki
git add .
git commit -m "Update wiki documentation"
git push origin master
```

## Maintenance

When updating documentation:

1. Edit the files in this `wiki/` directory
2. Commit changes to the main repository
3. Update public documentation, examples, schemas, or skills affected by a conceptual change
4. Run `python scripts/validate_repository.py`
5. Optionally publish updated content to the GitHub Wiki

## Repository and published wiki

The repository preserves review history, validation, branches, and references across the public UDF framework. The GitHub Wiki is an optional publication channel for the numbered framework reference, not a separate source of truth.

## Contributing

To contribute to the documentation:

1. Edit files in this directory
2. Submit a pull request to the main repository
3. Once merged, maintainers may publish the numbered reference to the GitHub Wiki

For more details, see [CONTRIBUTING.md](../CONTRIBUTING.md) and [WIKI_GUIDE.md](../WIKI_GUIDE.md).
