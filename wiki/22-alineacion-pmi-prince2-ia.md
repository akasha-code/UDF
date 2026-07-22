# 22) Alineación con PMI, PRINCE2 e IA

UDF toma principios útiles de PMI y PRINCE2 sin intentar reemplazarlos ni declararse certificado por esas organizaciones. El mapeo permite que proyectos con IA usen vocabulario y controles reconocibles manteniendo el carácter modular del framework.

## 22.1 Aportes de PMI

La orientación reciente de PMI sobre IA en project management enfatiza valor, responsabilidad humana, confiabilidad, transparencia, ética, sostenibilidad y adaptabilidad, junto con gobierno, datos, ciclo de vida y capacidad organizacional.

UDF los operacionaliza así:

| Tema | Tratamiento UDF |
| --- | --- |
| Valor | Outcomes y beneficios trazables, no adopción de IA como fin |
| Responsabilidad humana | Principal, mandato, aprobación efectiva y aceptación de riesgo |
| Transparencia | Provenance, registros de intervención y documentación de límites |
| Confiabilidad | Testing, evaluación, monitoreo y gestión de cambios de modelo/datos |
| Datos | Sensibilidad, calidad, procedencia, acceso, retención y soberanía |
| Ciclo de vida | Revaluación en Stage Reviews, operación y retiro |
| Capacidad organizacional | Madurez como entrada para decidir autonomía y controles |

Un registro de riesgos clásico sigue siendo válido, pero debe contemplar riesgos propios de IA: deriva, alucinación, sesgo, prompt injection, exfiltración, dependencia de proveedor, cambios de modelo y uso imprevisto de herramientas.

## 22.2 Aportes de PRINCE2

PRINCE2 aporta especialmente:

- **justificación de negocio continua:** la IA debe seguir resolviendo un problema con valor y riesgo aceptables;
- **gestión por excepción:** el mandato expresa tolerancias y condiciones de escalamiento;
- **gestión por etapas:** cada Stage Review reevalúa contexto, evidencia y autorización;
- **productos definidos:** work products y evidencia tienen criterios de calidad explícitos;
- **roles claros:** principal, actor, owner de riesgo y aprobador no se confunden;
- **tailoring:** documentación y controles se adaptan al contexto, sin perder invariantes.

El **work package** puede representarse como un mandato ejecutable. Cuando un agente excede tolerancias de costo, tiempo, alcance, calidad, riesgo o beneficio, debe detenerse o elevar una excepción; no improvisar autoridad adicional.

## 22.3 Gobierno por autonomía y efecto

| Nivel | Ejemplo | Control orientativo |
| --- | --- | --- |
| Asistivo | Resume o propone | Revisión del usuario y trazabilidad de fuentes |
| Preparativo | Genera un cambio sin aplicarlo | Tests y aprobación antes de integrar |
| Acotado | Ejecuta cambios reversibles dentro de un mandato | Sandbox, límites, evidencia y monitoreo |
| Supervisado | Opera continuamente con escalamiento | Tolerancias, observabilidad y revisión periódica |
| Alto impacto | Produce efectos sensibles o difíciles de revertir | Separación de funciones, aprobación previa y assurance independiente |

La clasificación no depende de si el actor es humano o LLM: depende del mandato, el efecto y el contexto.

## 22.4 Gates actualizados

Además de los criterios UDF existentes, un gate para sistemas con IA puede preguntar:

- ¿La justificación para usar IA sigue vigente frente a una solución más simple?
- ¿El mandato y las tolerancias son explícitos?
- ¿Los datos y fuentes están autorizados, actualizados y trazables?
- ¿Las evaluaciones representan escenarios reales y abuso razonable?
- ¿Permisos, credenciales y guardrails corresponden al efecto posible?
- ¿Existe intervención humana efectiva donde el riesgo lo requiere?
- ¿Se puede observar, detener, revertir y retirar el sistema?
- ¿Se conocen costos, dependencias y plan de salida?

## 22.5 Referencias externas

- [PMI: Global Standard for AI in Project Management](https://www.pmi.org/about/press-media/2026/pmi-publishes-worlds-first-global-standard-for-ai-in-project-work)
- [PMI: AI Standard for Project Management](https://www.pmi.org/blog/pmi-ai-standard-project-management)
- [PRINCE2: The changing role of the project manager in an AI-enabled environment](https://www.prince2.com/uk/blog/the-changing-role-of-the-project-manager-in-an-ai-enabled-environment)
- [PRINCE2: How to effectively manage an AI project](https://www.prince2.com/eur/blog/how-to-effectively-manage-an-ai-project)

---

## Navegación

- [Gobierno y Project Management](04-governance.md)
- [Contexto, assurance y capacidades](19-contexto-assurance-capacidades.md)
- [Documentación agent-ready](21-documentacion-agent-ready.md)
