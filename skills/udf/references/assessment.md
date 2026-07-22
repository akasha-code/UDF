# Assessment de contexto y assurance

## Entradas

Evaluá, con evidencia cuando sea posible:

- criticidad e impacto;
- reversibilidad de efectos;
- regulación y obligaciones contractuales;
- sensibilidad, residencia y jurisdicción de datos;
- autonomía real del actor;
- topología de ejecución y límites de confianza;
- cadencia de cambio;
- madurez operativa;
- volumen y distribución del conocimiento;
- necesidad explícita de RAG o staffing.

Usá `schemas/context-assessment.schema.json` como contrato. No rellenes incertidumbres con falsa precisión: registralas en `unknowns`.

## Derivación

Elevá assurance, documentación y supervisión ante alta criticidad, difícil reversibilidad, regulación, datos restringidos o autonomía alta. Si la madurez es baja, reducí autonomía antes de agregar complejidad de control.

El perfil automático es una recomendación reproducible, no una aprobación. Una persona confirma los hechos, acepta riesgos y decide excepciones.

## Gate

Revisá si continúa la justificación de negocio, si el mandato está vigente, si las evaluaciones representan uso y abuso, si permisos y datos son adecuados, y si el sistema puede observarse, detenerse, revertirse y retirarse.
