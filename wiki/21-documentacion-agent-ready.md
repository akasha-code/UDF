# 21) Documentación agent-ready

> **Carácter editorial:** perspectiva opcional. Complementa la documentación para personas; no obliga a mantener dos fuentes ni a adoptar protocolos agenticos.

La documentación UDF debe servir a personas y a sistemas agenticos sin crear dos verdades paralelas. El objetivo no es escribir para una marca de IA, sino mejorar descubrimiento, comprensión, recuperación, acción, verificación y gobierno.

## 21.1 Seis propiedades

| Propiedad | Práctica |
| --- | --- |
| Descubrible | Índices claros, `README`, `llms.txt`, sitemap o catálogo y nombres previsibles |
| Comprensible | Lenguaje directo, términos definidos, alcance y ejemplos |
| Recuperable | Secciones autocontenidas, encabezados descriptivos, metadatos y enlaces estables |
| Accionable | Procedimientos, entradas, salidas, precondiciones y criterios de terminación |
| Verificable | Esquemas, tests, fuentes, versiones, evidencia y resultados esperados |
| Gobernable | Owners, estado, fecha, sensibilidad, política de cambio y deprecación |

Esto puede favorecer la visibilidad en buscadores y asistentes —a veces llamada GEO, AEO o SEO para IA—, pero el objetivo primario es una documentación confiable y reutilizable.

## 21.2 Escritura para personas y agentes

Cada guía operacional debería declarar:

1. propósito y cuándo usarla;
2. alcance y no-alcance;
3. entradas y supuestos;
4. permisos y riesgos;
5. procedimiento o decisiones;
6. salidas y evidencia;
7. validación y criterios de finalización;
8. escalamiento y rollback;
9. versión y fuentes relevantes.

Preferir Markdown semántico, enlaces relativos dentro del repositorio, ejemplos pequeños y formatos estructurados solo donde agreguen verificabilidad. Evitar esconder reglas críticas exclusivamente en diagramas, imágenes o conversaciones.

## 21.3 Capas documentales

- **orientación:** `README.md`, mapa del framework y quick start;
- **instrucción local:** `AGENTS.md` u otras reglas cercanas al trabajo;
- **método:** wiki y guías conceptuales;
- **contratos:** JSON Schema, OpenAPI, manifiestos y políticas;
- **operación:** runbooks, comandos, observabilidad y recuperación;
- **evidencia:** resultados de tests, decisiones, intervenciones y aprobaciones;
- **descubrimiento agentico:** `llms.txt`, skills y recursos MCP cuando aporten valor.

`llms.txt` es un índice ligero y emergente, no reemplaza navegación, permisos ni documentación canónica.

## 21.4 Skills para aplicar UDF

Un skill es apropiado cuando se necesita un procedimiento repetible que un agente pueda aplicar en distintos repositorios. El skill UDF incluido define modos explícitos:

- `analyze`: entender sin modificar;
- `assess`: caracterizar el contexto y sus incertidumbres;
- `plan`: proponer perfil, artefactos, controles y validación;
- `apply`: realizar cambios autorizados;
- `validate`: comprobar artefactos o implementación;
- `review-gate`: preparar o revisar un Stage Review;
- `audit`: reconstruir mandatos, intervenciones, evidencia y desviaciones.

El modo predeterminado frente a pedidos de análisis es de solo lectura. Un agente no debe convertir una conversación exploratoria en cambios del proyecto.

## 21.5 MCP para UDF

Un servidor MCP podría exponer evaluadores, plantillas, schemas, perfiles o checks de gate. Vale la pena cuando varios clientes necesitan acceso dinámico y gobernado a esas capacidades. No es necesario para distribuir documentación y un skill versionado.

Si se implementa, debe mantener la lógica de dominio separada del adaptador MCP y ofrecer contratos que también puedan utilizarse desde CLI o API. En este repositorio, los esquemas y el evaluador son esa base portable; no se incorpora un servidor obligatorio.

## 21.6 Calidad documental automatizable

Puede validarse automáticamente:

- enlaces internos y archivos referenciados;
- ejemplos contra sus esquemas;
- frontmatter y metadatos obligatorios;
- coherencia entre índice, navegación y archivos;
- comandos o ejemplos ejecutables en entornos seguros;
- antigüedad y owner de documentación sensible;
- cobertura de términos del glosario.

La IA puede detectar ambigüedad, contradicciones o secciones pobres, pero los checks deterministas deben conservarse para invariantes verificables.

---

## Navegación

- [Arquitectura agentica e integraciones](20-arquitectura-agentic-e-integraciones.md)
- [Alineación con PMI y PRINCE2](22-alineacion-pmi-prince2-ia.md)
- [Skill UDF](../skills/udf/SKILL.md)
