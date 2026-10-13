---
# ── Identidad (no cambiar después de creado) ──────────────────────────
id: modulo.slug                 # ej. dinero.interes-compuesto  (minúsculas, guiones)
titulo: Título del nodo
modulo: modulo                  # ej. dinero
alcance: nucleo                 # nucleo | local
pais: null                      # solo si alcance: local → código ISO en minúscula, ej. co
nodo_base: null                 # solo si alcance: local → id del nodo del núcleo que adapta

# ── Lugar en el grafo ──────────────────────────────────────────────────
nivel: 1                        # 1 básico · 2 intermedio · 3 avanzado
prerrequisitos: []              # ids de nodos que hay que dominar antes
conecta_con: []                 # puentes académicos, ej. matematicas.porcentajes

# ── Quién lo tiene y en qué va ─────────────────────────────────────────
estado: pendiente               # pendiente | en-progreso | en-revision | aprobado | retirado
responsable: null               # usuario de GitHub de quien lo tiene ahora
revisores: []                   # usuarios que aprobaron
revision_experta: false         # true en salud, electricidad, legal, tributario

# ── Trazabilidad ───────────────────────────────────────────────────────
procedencia: []                 # - {autor: usuario, modelo: nombre-del-modelo-o-ninguno, fecha: AAAA-MM-DD}
recursos: []                    # - {titulo: ..., url: ..., licencia: ...}
actualizado: AAAA-MM-DD
---

# Título del nodo

## Pregunta que responde

Una sola pregunta, en palabras de un estudiante. Ej.: "¿Por qué una deuda pequeña puede volverse enorme?"

## Explicación

Explicación breve (menos de 10 minutos de lectura), clara para un estudiante de 12 años.

## Ejemplo cotidiano

Una situación real y creíble, que funcione también fuera de una gran ciudad.

## Puente académico

Qué concepto académico hay detrás y cómo se conecta (ver `conecta_con`).

## Ejercicios

1. Ejercicio resuelto paso a paso.
2. Ejercicio guiado.
3. Ejercicio independiente.

<details>
<summary>Soluciones</summary>

1. …
2. …
3. …

</details>

## Caso práctico (evidencia de dominio)

Algo real que el estudiante hace y puede mostrar. Con criterios claros de cómo se evalúa.

## Errores comunes

- Error frecuente y cómo detectarlo.

## Para el docente ancla

Preguntas para conversar, tiempo estimado, cómo conectar con el nodo siguiente.
