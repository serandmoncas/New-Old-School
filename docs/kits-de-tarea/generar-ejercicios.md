# Kit · Generar ejercicios

**Produce**: las secciones *Ejercicios* (con soluciones), *Caso práctico* y *Errores comunes* de un nodo.
**Rúbricas**: "Ejercicios" y "Caso práctico" en `docs/rubricas.md`.

## Prompt

```text
Actúas como docente de secundaria para New Old School.
Ya leíste AGENTS.md y el archivo del nodo que te pasé, incluida su explicación.

Escribe SOLO estas secciones, en Markdown y en español neutro:
## Ejercicios
## Caso práctico (evidencia de dominio)
## Errores comunes

Condiciones para Ejercicios:
- 8 ejercicios, de fácil a difícil.
- El 1 y el 2 resueltos paso a paso; del 3 en adelante, solo el enunciado.
- Mezcla tres tipos: cálculo, interpretación ("¿qué significa este resultado?")
  y decisión ("¿qué harías y por qué?").
- Situaciones creíbles para un joven de 12 a 15 años.
- Coloca todas las soluciones al final dentro de
  <details><summary>Soluciones</summary> ... </details>,
  explicando el razonamiento, no solo el resultado.

Condiciones para Caso práctico:
- Una actividad real que el estudiante pueda hacer con celular básico,
  sin gastar dinero y sin compartir datos personales sensibles.
- Indica qué debe entregar como evidencia y 3 a 4 criterios de evaluación.

Condiciones para Errores comunes:
- 3 a 5 errores frecuentes y cómo detectarlos.

Verifica tú mismo cada cálculo antes de responder. Si el nodo es de alcance
"nucleo", usa una moneda genérica ("pesos" o "unidades") sin cifras de un país.
```

## Antes de entregar

- [ ] Rehice yo mismo cada cálculo (calculadora u hoja de cálculo).
- [ ] Las soluciones explican el razonamiento.
- [ ] El caso práctico es seguro y factible.
- [ ] Agregué mi entrada en `procedencia`.
