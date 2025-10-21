# Wiki Content Directory

This directory contains the source documentation files for the UDF framework.

## ⚠️ Important Notice

**The official UDF documentation is published on the [GitHub Wiki](https://github.com/akasha-code/UDF/wiki)**

This directory serves as a source repository for the wiki content. The files here should be published to the GitHub Wiki to make them accessible to users.

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

## Publishing to GitHub Wiki

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
3. Publish updated content to the GitHub Wiki
4. Ensure links in README.md point to the wiki

## Why Separate Repository and Wiki?

Following the issue guidance:
- **Repository (https://github.com/akasha-code/UDF)**: Examples and framework structure
- **Wiki (https://github.com/akasha-code/UDF/wiki)**: Complete manual and documentation

This separation keeps the repository clean and focused on practical implementation while providing comprehensive documentation through the wiki.

## Contributing

To contribute to the documentation:

1. Edit files in this directory
2. Submit a pull request to the main repository
3. Once merged, the maintainers will publish to the wiki

For more details, see [CONTRIBUTING.md](../CONTRIBUTING.md) and [WIKI_GUIDE.md](../WIKI_GUIDE.md).
