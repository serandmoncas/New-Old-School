---
id: matematicas.ecuaciones-lineales
titulo: Ecuaciones lineales
modulo: matematicas
alcance: nucleo
pais: null
nodo_base: null
nivel: 1
prerrequisitos: []
conecta_con: [dinero.ahorro-y-metas, dinero.interes-simple]
estado: en-progreso
responsable: serandmoncas
revisores: []
revision_experta: false
procedencia:
- {autor: claude, modelo: claude-opus-5-5, fecha: '2026-10-14', nota: 'borrador piloto para discutir el Formato Curioso en matemáticas; falta revisión humana'}
recursos:
- {titulo: Al-Juarismi, url: 'https://es.wikipedia.org/wiki/Al-Juarismi', licencia: CC BY-SA 4.0}
- {titulo: Ecuación de primer grado, url: 'https://es.wikipedia.org/wiki/Ecuaci%C3%B3n_de_primer_grado', licencia: CC BY-SA 4.0}
- {titulo: Plano cartesiano, url: 'https://es.wikipedia.org/wiki/Coordenadas_cartesianas', licencia: CC BY-SA 4.0}
actualizado: '2026-10-14'
---

# Ecuaciones lineales

<!--
BORRADOR PILOTO, fuera de curriculo/: no hay módulo de matemáticas todavía. Sirve para discutir
cómo se ve el Formato Curioso en un nodo académico (Discussions, Propuestas).
Llega desde Dinero: ahorro-y-metas lo nombra en conecta_con. Retoma a Kevin y a Doña Marta con
las cifras de ese nodo. Moneda genérica ("pesos") y cifras redondas: es contenido del núcleo.
En matemáticas, "La evidencia" cambia de función: no es "¿qué estudio lo prueba?", sino
"¿cómo sabemos que está bien?" (comprobar) y "¿de dónde salió?" (historia).
-->

## El gancho (≈ 30 s)

Kevin quiere una bicicleta de 360.000 pesos. Ya tiene 60.000 guardados y ahorra 30.000 cada mes. ¿En cuántos meses la compra?

Puedes contar mes a mes: 90.000, 120.000, 150.000… y en algún momento llegas. Funciona, pero es lento. Y si la cifra fuera de millones, te cansarías antes de terminar.

Hay otra forma: hacer la pregunta al revés. Hace unos mil doscientos años, un sabio en Bagdad escribió un libro entero sobre cómo hacerla. Del título de ese libro viene una palabra que quizás te asusta: **álgebra**.

## La idea (≈ 90 s)

Muchas cosas crecen **lo mismo cada vez**: el ahorro de Kevin sube 30.000 cada mes. Eso se puede escribir así:

> **lo que tengo = lo que tenía al empezar + lo que sumo cada vez × las veces**

Con los números de Kevin, y llamando *m* a los meses: **60.000 + 30.000 × m = 360.000**.

Eso es una **ecuación**: una igualdad con un número escondido, la **incógnita**. Se llama **lineal** porque la incógnita solo se multiplica por un número, nunca por sí misma. Más adelante verás que, si la dibujas, sale una línea recta.

Para encontrar el número escondido, piensa en una **balanza en equilibrio**. Lo que hagas de un lado, lo haces del otro, y sigue en equilibrio. Se trata de deshacer, paso a paso:

1. Quita los 60.000 de los dos lados: **30.000 × m = 300.000**.
2. Reparte los dos lados entre 30.000: **m = 10**.

Kevin compra la bicicleta en **10 meses**. No contaste mes a mes: deshiciste las operaciones en el orden contrario.

## La evidencia (≈ 60 s)

¿Cómo sabemos que 10 está bien? En matemáticas no hace falta creerle a nadie: **lo compruebas tú**. Pones 10 en lugar de *m*: 60.000 + 30.000 × 10 = 360.000. La balanza cuadra. Si no cuadrara, habría un error. Esa es la diferencia con otras materias: aquí cualquiera puede verificar la respuesta.

**Lo comprobado**: el sabio de Bagdad se llamaba **al-Juarismi**. Hacia el año 820 escribió un libro para resolver problemas de comercio, de medir terrenos y de repartir herencias. Uno de sus métodos se llamaba *al-yabr*, que quiere decir "restaurar": pasar algo al otro lado de la igualdad. De *al-yabr* viene "álgebra". Y de su nombre viene otra palabra que usas sin saberlo: **algoritmo**. <!-- VERIFICAR: fecha aproximada (≈ 820) y los usos del libro (comercio, terrenos, herencias); fuente: recurso de Wikipedia y, si es posible, una historia de las matemáticas de acceso abierto -->

**Lo que se dice, pero no es tan seguro**: que Descartes inventó la cuadrícula para dibujar ecuaciones mirando una mosca que caminaba por el techo. Es una historia bonita, pero no hay pruebas de que pasara así. Lo que sí está escrito es su libro, de 1637, donde une ecuaciones y dibujos. <!-- VERIFICAR: que la anécdota de la mosca se considera leyenda, y el año de La Géométrie (1637) -->

## ¿Y a mí qué? (≈ 60 s)

En el pueblo, un mototaxi cobra 2.000 pesos por subirte y 1.000 por cada kilómetro. Tienes 8.000. ¿Hasta dónde llegas? **2.000 + 1.000 × k = 8.000**. Quitas 2.000: 1.000 × k = 6.000. Repartes: **k = 6 kilómetros**. Si tu destino está a 7, ya sabes antes de subirte que no te alcanza.

En el campo, Doña Marta quiere diez gallinas que cuestan 250.000 pesos y guarda 5.000 a la semana. Si ya tuviera 50.000 ahorrados, ¿cuántas semanas le faltarían? **50.000 + 5.000 × s = 250.000**, así que 5.000 × s = 200.000, y **s = 40 semanas**. Con la ecuación puede comparar planes antes de decidir: ¿empiezo con algo guardado, o ahorro más cada semana?

Una ecuación lineal convierte "¿cuánto me falta?" en una cuenta que puedes resolver y comprobar.

## La puerta abierta (≈ 30 s)

Para conversar: **¿qué cosas de tu vida crecen lo mismo cada vez, y cuáles no?** Piensa en tu estatura, en una deuda o en los seguidores de una cuenta.

El siguiente nodo es **Funciones lineales**: qué pasa cuando, en vez de buscar un solo número escondido, dibujas todos los posibles. Ahí aparece la línea recta.

---

## Puente académico

<!-- En un nodo de matemáticas el puente va al revés: de lo académico a los nodos prácticos que lo usan. -->

Esta misma ecuación aparece en otros nodos de Dinero:

- **Ahorro y metas**: *Ahorro = I + a × m*. Despejar *m* responde "¿cuántos meses me faltan?".
- **Interés simple**: *M = C + C × r × t*. El dinero crece lo mismo en cada periodo. Despejar *t* responde "¿en cuánto tiempo se duplica mi deuda?".

Las dos tienen la forma **y = b + a × x**: *b* es de dónde arrancas y *a* es cuánto sumas cada vez. Aprender a despejar una sola vez sirve para todas.

## Ejercicios

1. **(Resuelto)** Resuelve 60.000 + 30.000 × m = 360.000 y comprueba.
    - Quita 60.000 de los dos lados: 30.000 × m = 300.000.
    - Reparte entre 30.000: **m = 10**.
    - Comprobación: 60.000 + 30.000 × 10 = 60.000 + 300.000 = 360.000. ✓
2. **(Guiado)** Un plan de celular cobra 10.000 pesos fijos al mes y 500 por cada megabyte extra. Este mes pagaste 14.000. ¿Cuántos megabytes extra usaste?
    - Escribe la ecuación: 10.000 + 500 × x = 14.000.
    - Quita lo fijo de los dos lados. Luego reparte.
3. Resuelve y comprueba: 3 × x + 7 = 31.
4. Resuelve y comprueba: 5 × x − 4 = 21.
5. Laura tiene 20.000 pesos y gasta 2.500 cada día en transporte. ¿Después de cuántos días le quedan 5.000? Escribe la ecuación antes de resolverla.
6. Inventa un problema de tu vida que se resuelva con una ecuación de la forma *b + a × x = total*. Resuélvelo y comprueba.

<details>
<summary>Soluciones</summary>

2. 10.000 + 500 × x = 14.000 → 500 × x = 4.000 → **x = 8 megabytes**. Comprobación: 10.000 + 500 × 8 = 14.000. ✓
3. 3 × x = 24 → **x = 8**. Comprobación: 3 × 8 + 7 = 31. ✓
4. 5 × x = 25 → **x = 5**. Comprobación: 5 × 5 − 4 = 21. ✓
5. 20.000 − 2.500 × d = 5.000 → 2.500 × d = 15.000 → **d = 6 días**. Comprobación: 20.000 − 2.500 × 6 = 5.000. ✓ Aquí el número que se repite *resta*: la ecuación sigue siendo lineal.
6. Respuesta abierta. Se evalúa que la situación crezca o baje lo mismo cada vez, que la ecuación la describa, que el despeje sea correcto y que haya comprobación.

</details>

## Caso práctico (evidencia de dominio)

**La ecuación de mi meta.**

1. Toma tu meta de ahorro de *Ahorro y metas* (o inventa una): cuánto cuesta, cuánto tienes y cuánto puedes guardar cada semana o cada mes.
2. Escribe la ecuación y despeja el tiempo que te falta.
3. Compruébala reemplazando tu respuesta.
4. Cambia **una sola** cosa (empezar con más, o guardar más cada vez) y resuelve de nuevo. ¿Cuál de los dos cambios te acerca más rápido?

**Entrega:** las dos ecuaciones, los despejes, las comprobaciones y dos o tres frases sobre qué cambio conviene y por qué.

**Se evalúa así:**

- La ecuación describe bien la situación (inicio, lo que se suma cada vez y total).
- El despeje es correcto y está comprobado.
- La comparación entre los dos planes es correcta y está explicada con palabras.

## Errores comunes

- **Hacer algo solo de un lado.** Si quitas 60.000 a la izquierda y no a la derecha, la balanza se rompe.
- **Deshacer en el orden equivocado.** Primero se quita lo que se suma y después se reparte lo que multiplica. Al revés, el resultado sale mal.
- **No comprobar.** Reemplazar la respuesta toma diez segundos y atrapa casi todos los errores.
- **Confundir el inicio con lo que se repite.** En "2.000 por subirte y 1.000 por kilómetro", el 2.000 se paga una vez y el 1.000 se multiplica.
- **Creer que el álgebra es otro idioma.** Es la misma cuenta que harías mes a mes, escrita de forma corta.

## Para el docente ancla

- **Tiempo:** una sesión de 45 a 60 minutos.
- **Cómo abrir:** pide que resuelvan el problema de Kevin contando mes a mes. Después muestra el despeje. Que comparen cuál fue más rápido y cuál se equivoca menos.
- **Material:** una balanza real, o dibujada, con fichas o tapas. Quitar lo mismo de los dos platos hace visible la regla.
- **Para conversar:** ¿por qué crees que un libro sobre herencias y comercio terminó dándole nombre a una materia entera?
- **Cuidado:** muchos estudiantes llegan creyendo que "no son buenos para matemáticas". Empieza por la comprobación: saber verificar da confianza antes que la técnica.
- **Siguiente nodo:** Funciones lineales.
