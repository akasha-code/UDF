# 1) Fases del ciclo de vida

**Fases UDF ↔ Resultado ↔ Stage Review (SR)**

El UDF define un ciclo de vida estructurado en seis fases principales, cada una con sus entregables específicos y su respectiva revisión de fase (Stage Review). Este enfoque garantiza la trazabilidad completa desde la concepción hasta el cierre del proyecto.

---

## Fases principales

### **Initiation (SR-I)**
**Objetivo:** Establecer la visión, alcance y viabilidad del proyecto.

**Entregables:**
* Charter del proyecto
* Modelo de dominio
* Casos de uso o historias de uso
* Prototipo de interfaz de usuario (UI)

**Criterios de salida:**
* Aprobación del charter por stakeholders
* Validación del modelo de dominio
* Prototipos validados con usuarios

---

### **Concept & Planning (SR-C)**
**Objetivo:** Detallar la solución y planificar la ejecución.

**Entregables:**
* Descripciones detalladas de requisitos
* Diagramas de robustez o story maps
* Diseño de clases
* Plan de proyecto detallado
* Matriz de trazabilidad

**Criterios de salida:**
* Plan de proyecto aprobado
* Arquitectura de solución validada
* Recursos asignados y comprometidos

---

### **Build (SR-E)**
**Objetivo:** Construcción e implementación de la solución.

**Entregables:**
* Diagramas de secuencia
* Diseño técnico detallado
* Pruebas automatizadas
* Architecture Decision Records (ADRs)
* Reportes de salud técnica

**Criterios de salida:**
* Código implementado y testeado
* Cobertura de pruebas según QEI
* ADRs documentados y aprobados
* Technical Health Index (THI) dentro de umbrales

---

### **Business Validation (SR-B)**
**Objetivo:** Validar que la solución cumple con las necesidades de negocio.

**Entregables:**
* Plan de cut-over
* Resultados de User Acceptance Testing (UAT)
* Evidencias de QA
* Validación de negocio formal

**Criterios de salida:**
* UAT completado exitosamente
* Sign-off de stakeholders
* Plan de despliegue aprobado

---

### **Operation (SR-O)**
**Objetivo:** Poner en producción y establecer operación estable.

**Entregables:**
* Despliegue completado
* Sistema de monitoreo configurado
* Runbook operativo
* Transferencia de ownership

**Criterios de salida:**
* Sistema en producción estable
* SLOs cumplidos
* Equipo operativo capacitado

---

### **Closure (SR-X)**
**Objetivo:** Formalizar el cierre y capturar aprendizajes.

**Entregables:**
* Lecciones aprendidas
* Métricas de beneficio realizado
* Conocimiento reintegrado al repositorio corporativo

**Criterios de salida:**
* Documentación completa y archivada
* Aprendizajes incorporados al proceso
* Cierre administrativo y financiero

---

## Flujo de progresión

```
Initiation → Concept & Planning → Build → Business Validation → Operation → Closure
   (SR-I)         (SR-C)          (SR-E)        (SR-B)           (SR-O)      (SR-X)
```

Cada Stage Review actúa como gate de calidad y decisión Go/No-Go para avanzar a la siguiente fase.

---

## Adaptabilidad

El nivel de detalle y formalidad de cada fase se ajusta según las variables del proyecto:
* **PDI** (Project Depth Index): profundidad documental
* **DSI** (Delivery Structure Index): ritmo y estructura
* **QEI** (Quality Emphasis Index): énfasis en calidad
* **TTI** (Team Topology Index): configuración del equipo

Ver [Delivery Cube](11-delivery-cube.md) para más detalles sobre la configuración.

---

[← Volver al Overview](00-overview.md) | [Siguiente: Artefactos →](02-artifacts.md)
