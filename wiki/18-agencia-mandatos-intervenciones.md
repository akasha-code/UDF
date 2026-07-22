# 18) Agencia, mandatos e intervenciones

> **Carácter editorial:** perspectiva opcional. Estas definiciones amplían UDF cuando intervienen actores con autonomía delegada; no reemplazan el modelo general de roles y equipos.

El UDF amplía su unidad de análisis: no presupone que todo trabajo lo realiza una persona ni que toda automatización es un agente. Modela **quién o qué interviene**, bajo qué autoridad, con qué límites y qué evidencia deja.

## 18.1 Conceptos

| Concepto | Definición operativa |
| --- | --- |
| **Principal** | Persona u organización que conserva la responsabilidad y delega autoridad. |
| **Actor** | Entidad identificable que participa: persona, equipo, servicio, modelo o sistema agentico. |
| **Agente** | Actor al que se le delega un objetivo y cierto margen para observar, decidir y actuar. Puede ser humano, técnico o híbrido. |
| **Equipo** | Composición coordinada de actores. No desaparece: expresa capacidades colectivas, coordinación y responsabilidad compartida. |
| **Mandato** | Delegación acotada: objetivo, alcance, permisos, prohibiciones, presupuesto, tolerancias, duración, supervisión y criterios de terminación. |
| **Intervención** | Unidad auditable de actuación de un actor: propuesta, decisión, modificación, ejecución o comunicación. |
| **Harness** | Entorno que conecta al agente con contexto, herramientas, memoria, políticas, evaluación y observabilidad. |
| **Guardrail** | Control preventivo, detectivo o correctivo que limita o verifica una intervención. |

La palabra **agente** describe autonomía delegada, no una tecnología específica. Una persona puede operar como agente dentro de un mandato. Un servicio determinista puede ser actor sin ser agente.

## 18.2 Modelo directo, asistente y agente

| Forma de uso | Rasgos | Tratamiento UDF |
| --- | --- | --- |
| Llamada directa a un LLM | Entrada y salida; sin objetivo persistente ni ciclo propio | Herramienta o modelo utilizado por un actor |
| Asistente | Mantiene conversación o contexto y propone trabajo | Actor asistivo; normalmente sin autoridad para producir efectos externos |
| Agente | Objetivo, ciclo de control, estado, herramientas y autoridad delegada | Actor sujeto a mandato, controles, evidencia y supervisión |
| Sistema multiagente | Varios agentes coordinados con roles y protocolos | Equipo técnico o híbrido con reglas de composición y escalamiento |

Usar un LLM no convierte automáticamente una solución en agentica. La distinción importante es si existe **autonomía para seleccionar o ejecutar intervenciones**.

## 18.3 Lo que se produce

Los artefactos siguen siendo válidos, pero no cubren por sí solos todo el trabajo:

- **work product:** resultado persistente, como código, documento, modelo o configuración;
- **state change:** cambio verificable en un sistema, repositorio, entorno o proceso;
- **decision:** elección con fundamento, autoridad y consecuencias;
- **evidence:** registro que permite verificar una afirmación, control o resultado;
- **outcome:** cambio de valor o comportamiento observado;
- **intervention record:** vínculo entre actor, mandato, acción, herramientas, resultados y evidencia.

Una intervención puede producir varios de estos resultados o ninguno. Por ejemplo, una evaluación puede generar evidencia y una recomendación sin modificar estado.

## 18.4 Responsabilidad y atribución

La autonomía puede delegarse; la responsabilidad organizacional no se transfiere a un modelo. Cada intervención con efectos relevantes debe poder responder:

1. ¿Qué principal autorizó el mandato?
2. ¿Qué actor ejecutó o propuso la intervención?
3. ¿Qué versión de modelo, herramienta, política y contexto se usó?
4. ¿Qué límites, tolerancias y guardrails aplicaban?
5. ¿Qué cambió, qué evidencia quedó y cómo se revierte?
6. ¿Quién acepta el riesgo residual y el resultado?

La aprobación humana no debe ser ceremonial. Debe ubicarse antes del efecto cuando la criticidad, irreversibilidad, sensibilidad o regulación lo exijan.

## 18.5 Mandato mínimo

Un mandato debería incluir:

```yaml
mandate:
  objective: "Reducir defectos sin cambiar interfaces públicas"
  principal: "engineering-lead"
  actor: "maintenance-agent"
  scope:
    can_read: ["src/", "tests/"]
    can_write: ["src/", "tests/"]
    must_not_touch: ["production/", "secrets/"]
  tolerances:
    cost: "20 EUR"
    duration: "2h"
    risk: "low"
  approval:
    required_before: ["dependency-change", "deployment", "data-deletion"]
  stop_conditions: ["tests-regress", "scope-uncertain", "credential-required"]
```

El contrato ejecutable está en [`schemas/mandate.schema.json`](../schemas/mandate.schema.json).

## 18.6 Equipos humanos, técnicos e híbridos

El concepto de equipo sigue siendo útil porque coordinación y composición no se reducen a identidades individuales. UDF recomienda describir:

- miembros o tipos de actor;
- capacidades complementarias;
- protocolo de coordinación y resolución de conflictos;
- límites de autoridad individuales y colectivos;
- mecanismo de escalamiento;
- responsable organizacional del resultado.

Así se evita tanto antropomorfizar servicios como reducir a las personas a componentes intercambiables.

---

## Navegación

- [Interoperabilidad y automatización](17-interoperabilidad-y-automatizacion.md)
- [Contexto, assurance y capacidades](19-contexto-assurance-capacidades.md)
- [Arquitectura agentica e integraciones](20-arquitectura-agentic-e-integraciones.md)
