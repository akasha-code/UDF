# 19) Contexto, assurance y capacidades

UDF no define una lista universal de tecnologías necesarias. Primero caracteriza el contexto y luego deriva un **perfil de entrega y assurance**: documentación, controles, evidencia y capacidades proporcionales al riesgo.

## 19.1 Del Delivery Cube al Context & Assurance Model

El [Delivery Cube](11-delivery-cube.md) continúa siendo una forma compacta y compatible de expresar profundidad, estructura, calidad y topología. Para sistemas humanos y agenticos se amplía con variables que influyen directamente en autonomía y control:

| Variable | Pregunta |
| --- | --- |
| Criticidad | ¿Cuál es el impacto de un error o abuso? |
| Reversibilidad | ¿El efecto se puede deshacer de manera segura y económica? |
| Regulación | ¿Existen obligaciones legales, contractuales o de auditoría? |
| Sensibilidad de datos | ¿Qué daño produciría exposición, alteración o pérdida? |
| Soberanía | ¿Dónde pueden residir y procesarse datos, modelos y evidencia? |
| Autonomía | ¿El actor recomienda, prepara o ejecuta efectos? |
| Topología de ejecución | ¿Opera localmente, en LAN, nube privada, nube pública, edge o de forma híbrida? |
| Cadencia de cambio | ¿Los cambios son puntuales, iterativos o continuos? |
| Madurez | ¿Qué capacidad real existe para operar, observar y auditar los controles? |

Estas variables no sustituyen PDI, DSI, QEI y TTI; permiten explicar mejor **por qué** se elige una configuración.

## 19.2 Clasificación contextual de capacidades

Cada capacidad se clasifica por proyecto, flujo o mandato:

| Estado | Significado |
| --- | --- |
| `required` | Sin ella el riesgo o una obligación no queda aceptablemente cubierto. |
| `recommended` | Aporta valor claro y su costo es proporcional. |
| `optional` | Puede mejorar el sistema, pero no es parte de la base mínima. |
| `not_applicable` | No responde al contexto actual. |
| `discouraged` | Añade riesgo, complejidad o dependencia injustificada. |

Todo estado debe incluir una razón. Esto evita transformar preferencias tecnológicas en obligaciones del framework.

## 19.3 Familias de capacidades

- **identidad y acceso:** autenticación, autorización, mínimo privilegio y separación de funciones;
- **ejecución segura:** aislamiento, sandbox, límites de recursos, allowlists y confirmación de efectos;
- **conocimiento y contexto:** búsqueda, RAG, memoria, versionado y control de procedencia;
- **coordinación:** gestión de trabajo, staffing, handoffs y escalamiento;
- **calidad:** pruebas unitarias, integración, contratos, navegadores reales o headless y evaluación de comportamiento agentico;
- **seguridad:** análisis de dependencias, secretos, amenazas, prompt injection y exfiltración;
- **observabilidad y auditoría:** trazas, costos, decisiones, intervenciones, logs y evidencia;
- **documentación:** formatos abiertos, referencias estables, esquemas y ejemplos ejecutables;
- **operación:** despliegue, rollback, continuidad, SLO y respuesta a incidentes.

RAG, staffing, MCP o nube **no son obligatorios**. Se activan cuando resuelven una necesidad demostrable.

## 19.4 Reglas de derivación

Algunas reglas fuertes pueden automatizarse:

- regulación o datos restringidos elevan trazabilidad, controles y documentación;
- efectos irreversibles requieren aprobación previa y plan de recuperación;
- mayor autonomía exige mejor observabilidad, límites y evaluación continua;
- ejecución fuera del perímetro esperado eleva requisitos de identidad, cifrado y soberanía;
- alta criticidad con baja madurez debe reducir autonomía, no compensarse solo con más documentación;
- RAG requiere fuentes autorizadas, procedencia, evaluación de recuperación y política de actualización;
- staffing agentico requiere reglas para selección, conflicto de intereses, presupuesto y terminación.

El evaluador incluido en [`skills/udf/scripts/derive_profile.py`](../skills/udf/scripts/derive_profile.py) aplica una base determinista. Un sistema de IA puede preparar el assessment a partir de evidencia, pero una persona confirma los datos y acepta el perfil resultante.

## 19.5 Soberanía digital

La soberanía no equivale automáticamente a operar sin nube. UDF separa dimensiones:

- residencia y jurisdicción de datos;
- ubicación del cómputo y de los modelos;
- control de identidades, claves y políticas;
- portabilidad de datos, prompts, evaluaciones y artefactos;
- dependencia y capacidad de salida del proveedor;
- auditabilidad y continuidad operacional.

Un diseño local-first puede ser apropiado, pero también debe contemplar parches, disponibilidad, backup y capacidad operativa. La decisión se registra como trade-off, no como dogma.

## 19.6 Perfil evaluable

UDF incluye esquemas separados para:

- [`context-assessment.schema.json`](../schemas/context-assessment.schema.json): hechos y supuestos de entrada;
- [`delivery-profile.schema.json`](../schemas/delivery-profile.schema.json): configuración derivada, capacidades y razones.

Separar entrada y resultado permite revaluar el perfil cuando cambia el contexto y comparar la recomendación automática con la decisión humana.

---

## Navegación

- [Delivery Cube](11-delivery-cube.md)
- [Agencia, mandatos e intervenciones](18-agencia-mandatos-intervenciones.md)
- [Arquitectura agentica e integraciones](20-arquitectura-agentic-e-integraciones.md)
