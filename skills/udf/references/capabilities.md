# Selección de capacidades e interfaces

## Estado contextual

Clasificá cada capacidad como `required`, `recommended`, `optional`, `not_applicable` o `discouraged`. Incluí siempre una razón ligada al assessment.

## Familias

- identidad y mínimo privilegio;
- aislamiento y ejecución segura;
- conocimiento, RAG y memoria;
- gestión de trabajo, staffing y coordinación;
- testing tradicional, agentico y web;
- seguridad y supply chain;
- observabilidad, costos y auditoría;
- documentación y contratos;
- operación, continuidad y rollback.

## Dimensiones independientes

Separá:

1. capacidad de dominio;
2. interfaz: CLI, API, MCP, ACP, skill, GUI, TUI, evento;
3. transporte: stdio, HTTP, socket, cola;
4. despliegue: proceso, local, LAN, nube privada/pública, edge;
5. límite de confianza.

MCP puede ser local o remoto. Una API y un adaptador MCP pueden coexistir. Encapsulá la lógica de dominio detrás de adaptadores cuando el costo sea proporcional.

ACP puede referirse a un protocolo cliente–agente o agente–agente. Nombrá la especificación y versión; no deduzcas topología o confianza solo del acrónimo.

## Ejemplos no normativos

- clientes/harnesses: Codex, Claude Code, OpenCode, Gemini CLI;
- código semántico: LSP, Serena;
- trabajo: OpenProject, Taskwarrior, Kanban, Jira, Linear, GitHub Projects;
- web: Playwright y navegadores headless;
- revisión: Plannotator;
- conocimiento: Obsidian y pipelines RAG;
- infraestructura: CLI/API de AWS, Azure o GCP, Kubernetes y OpenTofu/Terraform.

Evaluá capacidades, no popularidad de marca.
