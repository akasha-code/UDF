# 20) Arquitectura agentica e integraciones

> **Carácter editorial:** perspectiva opcional y orientativa para iniciativas que incorporan IA, agentes o integraciones relacionadas.

UDF recomienda arquitecturas por **capacidades e interfaces**, no una lista normativa de marcas. Las herramientas concretas son ejemplos reemplazables y deben evaluarse por contexto.

## 20.1 Capacidad, interfaz, transporte y despliegue

Estas dimensiones son independientes:

| Dimensión | Ejemplos |
| --- | --- |
| Capacidad de dominio | consultar tareas, modificar código, desplegar, recuperar conocimiento |
| Interfaz | CLI, API, MCP, ACP, skill, GUI, TUI, evento o archivo |
| Transporte | stdio, HTTP, WebSocket, cola, socket local |
| Despliegue | mismo proceso, host local, LAN, nube privada, nube pública, edge |
| Límite de confianza | proceso, usuario, dispositivo, red, organización, proveedor |

Por eso un MCP puede operar por `stdio` en la misma máquina, como servicio local o dentro de una LAN. **MCP no significa internet ni cloud**. A su vez, una CLI puede invocar una API remota y cruzar varios límites de confianza.

## 20.2 CLI, API, MCP, ACP y skills

No forman una secuencia obligatoria:

- una **CLI** es buena para personas, scripts y automatización reproducible;
- una **API** ofrece un contrato de aplicación estable e independiente del cliente;
- un servidor **MCP** presenta herramientas, recursos o prompts a clientes compatibles;
- **ACP** puede nombrar, según la especificación, un protocolo cliente–agente o uno de comunicación entre agentes;
- un **skill** enseña a un agente cómo aplicar un método, usar herramientas y respetar políticas;
- GUI y TUI pueden ofrecer control humano y visibilidad operacional.

Un patrón sólido es implementar la capacidad de dominio sin depender del adaptador y exponer solo las interfaces que aporten valor. MCP puede envolver una API, una CLI o una biblioteca, pero no debería ser la única definición del dominio ni reemplazar automáticamente una API pública.

El acrónimo ACP no debe quedar solo en un contrato: registrá nombre completo, autoridad de la especificación, versión y propósito. Un protocolo cliente–agente gestiona sesiones, mensajes y control entre una interfaz y un agente; un protocolo agente–agente coordina descubrimiento, delegación y resultados entre agentes. Ninguno determina por sí mismo si la ejecución es local, LAN o cloud. Según la variante, ACP puede complementar a MCP en lugar de competir con él.

## 20.3 Harness y guardrails

Un harness agentico debería separar:

1. **objetivo y mandato**;
2. **contexto** recuperado y su procedencia;
3. **modelo o motor de decisión**;
4. **herramientas e interfaces**;
5. **memoria y estado**;
6. **políticas y guardrails**;
7. **evaluación, observabilidad y costos**;
8. **aprobación, escalamiento y terminación**.

Los guardrails no se reducen a filtros de texto. Incluyen permisos del sistema operativo, credenciales acotadas, sandboxes, límites de red, validación de argumentos, aprobación previa, políticas de datos, tests, monitoreo y rollback.

## 20.4 RAG y memoria

RAG es una capacidad opcional útil cuando el trabajo depende de conocimiento amplio, cambiante o privado. No hace falta para contextos pequeños que caben de forma controlada en la entrada.

Antes de incorporarlo, definir:

- fuentes autorizadas y derechos de uso;
- estrategia de segmentación, metadatos y filtros de acceso;
- actualización, borrado y versionado;
- procedencia visible de cada respuesta;
- evaluación de recuperación y de respuesta;
- defensa frente a contenido malicioso e instrucciones embebidas;
- residencia de índices, embeddings y consultas.

Una base de notas como Obsidian puede ser fuente documental o interfaz humana; no es por sí sola un RAG. Debe existir un pipeline explícito si se quiere recuperación semántica.

## 20.5 Staffing y coordinación

Los sistemas de staffing pueden seleccionar personas, agentes o combinaciones según capacidades, disponibilidad, costo y restricciones. Son opcionales. Un motor local como AgentMarket ilustra que staffing, CLI, MCP, TUI, embeddings y modelos pueden desacoplarse.

UDF exige que la selección conserve:

- criterios explicables y política de elegibilidad;
- mandato individual y colectivo;
- presupuesto y límites de concurrencia;
- manejo de conflictos y fallos parciales;
- evaluación de desempeño sin confundir volumen con valor;
- salida segura y reasignación.

## 20.6 Gestión de trabajo y revisión humana

UDF no presupone una plataforma corporativa. Puede integrarse con:

- servidores de gestión de proyectos como OpenProject;
- gestores locales y CLI como Taskwarrior;
- tableros Kanban físicos o digitales;
- issues y proyectos ligados al repositorio;
- planners y superficies de anotación como Plannotator;
- bases de conocimiento como Obsidian.

La herramienta debe preservar identificadores, estados, responsables, relaciones, evidencia y reglas de transición suficientes para el perfil elegido.

## 20.7 Testing de sistemas agenticos

Además de pruebas tradicionales, evaluar:

- calidad de decisiones sobre escenarios representativos;
- uso correcto de herramientas y argumentos;
- cumplimiento de mandato, permisos y `must_not_touch`;
- resistencia a prompt injection y contenido no confiable;
- idempotencia, reintentos, timeout y recuperación;
- costo, latencia y consumo de contexto;
- navegación real con herramientas como Playwright y navegadores headless cuando la interfaz web sea parte del sistema;
- regresiones de modelo, prompt, herramientas, fuentes RAG y políticas.

Las pruebas end-to-end en navegador son una capacidad contextual, no un requisito para proyectos sin superficie web.

## 20.8 Nube y operación local

AWS, Azure, GCP, nubes privadas, homelabs y ejecución local pueden participar. Sus CLI y API son interfaces potentes, pero un agente debe operar con identidad separada, mínimo privilegio, entornos acotados, dry-run cuando exista y aprobación para efectos sensibles.

La elección local/cloud/híbrida se toma con el modelo de contexto y assurance; no se deduce de usar MCP, RAG o un cliente agentico.

## 20.9 Taxonomía orientativa de herramientas

| Capacidad | Ejemplos no normativos |
| --- | --- |
| Clientes y harnesses | Codex, Claude Code, OpenCode, Gemini CLI |
| Comprensión semántica de código | LSP, Serena |
| Gestión de trabajo | OpenProject, Taskwarrior, Kanban, Jira, Linear, GitHub Projects |
| Pruebas web | Playwright, navegadores headless |
| Revisión de planes | Plannotator y flujos equivalentes |
| Documentación | Markdown, Mermaid, PlantUML, OpenAPI, JSON Schema, Obsidian |
| Infraestructura | CLI de AWS/Azure/GCP, Kubernetes, OpenTofu/Terraform |

Los ejemplos ayudan a descubrir opciones; no definen conformidad con UDF.

---

## Navegación

- [Contexto, assurance y capacidades](19-contexto-assurance-capacidades.md)
- [Documentación agent-ready](21-documentacion-agent-ready.md)
- [Unified Test Strategy](16-unified-test-strategy.md)
