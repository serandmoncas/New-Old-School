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

<!--
Parte 1 · La historia (formato Curioso): se puede contar en máximo 5 minutos.
Una sola idea. Concreto antes que completo. Entra directo al gancho.
Parte 2 · La práctica: puente académico, ejercicios, caso y guía para el docente.
-->

## El gancho (≈ 30 s)

La pregunta que responde este nodo, en palabras de un estudiante, y qué tiene de sorprendente. Empieza sin contexto: una situación, un dato inesperado, una persona real.
Ej.: "¿Por qué una deuda de 100.000 pesos puede terminar costando el triple?"

## La idea (≈ 90 s)

La explicación para alguien que no sabe nada del tema: una sola idea, frases cortas, un ejemplo que se pueda imaginar o tocar.

## La evidencia (≈ 60 s)

¿Cómo lo sabemos? ¿Quién lo dice y qué tan seguro es? Separa lo comprobado de lo que solo "se dice". Obligatorio en temas polémicos.

## ¿Y a mí qué? (≈ 60 s)

Por qué importa en la vida del estudiante: un ejemplo cotidiano y creíble, que funcione también fuera de una gran ciudad, y qué decisión cambia con esto.

## La puerta abierta (≈ 30 s)

La pregunta que queda para conversar en grupo, dónde profundizar y qué nodo sigue.

---

## Puente académico

Qué concepto académico hay detrás y cómo se conecta (ver `conecta_con`). Si se puede, su historia: quién lo descubrió, cuándo y qué problema resolvía.

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
