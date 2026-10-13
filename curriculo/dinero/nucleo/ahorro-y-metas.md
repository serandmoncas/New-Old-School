---
id: dinero.ahorro-y-metas
titulo: Ahorro y metas
modulo: dinero
alcance: nucleo
pais: null
nodo_base: null
nivel: 1
prerrequisitos: [dinero.presupuesto]
conecta_con: [matematicas.ecuaciones-lineales]
estado: en-revision
responsable: serandmoncas
revisores: []
revision_experta: false
procedencia:
- {autor: claude, modelo: claude-opus-5-5, fecha: '2026-10-13', nota: primera versión}
recursos:
- {titulo: Experimento del malvavisco de Stanford, url: 'https://en.wikipedia.org/wiki/Stanford_marshmallow_experiment', licencia: CC BY-SA 4.0}
- {titulo: Historia de las alcancías, url: 'https://en.wikipedia.org/wiki/Piggy_bank', licencia: CC BY-SA 4.0}
actualizado: '2026-10-13'
---

# Ahorro y metas

<!--
Moneda genérica ("pesos") y cifras redondas, porque es contenido del núcleo.
El bloque de evidencia desmonta la lectura "esperar es cuestión de fuerza de voluntad".
-->

## El gancho (≈ 30 s)

Imagina que tienes cinco años. Un adulto te pone un malvavisco enfrente y te dice: "Puedes comértelo ya. Pero si esperas a que yo vuelva, te doy dos". Y se va.

Eso hicieron investigadores de la Universidad de Stanford con cientos de niños, a finales de los años sesenta. Algunos se lo comieron en segundos. Otros se tapaban los ojos, cantaban o se sentaban encima de las manos para aguantar.

Ahorrar es exactamente eso: no comerte el malvavisco hoy para tener más mañana. Pero la historia tiene un giro que casi nadie cuenta.

## La idea (≈ 90 s)

**Ahorrar** es guardar una parte de lo que tienes hoy para algo que quieres o necesitas después.

El problema es que ahorrar "porque sí" casi nunca funciona: el dinero sin destino termina gastado. Lo que funciona es ahorrar **para algo**. Una buena meta responde tres preguntas:

1. **¿Para qué?** Algo concreto: una bicicleta, no "ahorrar más".
2. **¿Cuánto cuesta?** Un número: 360.000 pesos.
3. **¿Para cuándo?** Una fecha: en 12 meses.

Con eso, la cuenta sale sola: **lo que cuesta ÷ los meses = lo que debes guardar cada mes**. 360.000 ÷ 12 = 30.000 pesos al mes.

Hay una meta especial que todos deberían tener: el **fondo de emergencias**. Es plata guardada para lo que no se puede planear: una enfermedad, algo que se daña, un mes sin trabajo. No es para gastar; es para no tener que endeudarse cuando llega el imprevisto.

## La evidencia (≈ 60 s)

Durante años se dijo que los niños que esperaban el segundo malvavisco tenían, de grandes, mejores resultados en el colegio y en la vida. La conclusión parecía clara: **ahorrar es cuestión de fuerza de voluntad**.

**El giro**: en 2018, un estudio con muchos más niños y de familias más diversas encontró que el efecto era mucho menor. Buena parte se explicaba por algo más: la **situación de cada familia**. Otro experimento mostró que los niños esperan mucho menos cuando el adulto antes les ha incumplido una promesa. Tiene sentido: si no confías en que el segundo malvavisco va a llegar, lo racional es comerte el primero.

**Lo que sí está comprobado**: las metas concretas y escritas funcionan mejor que las vagas. Y ponerse barreras ayuda. En un estudio en Filipinas, las personas que eligieron guardar su dinero en una cuenta que no podían tocar hasta cumplir su meta ahorraron bastante más que las demás.

La lección: ahorrar no depende solo de aguantarse. Depende de tener una meta clara y de **hacerse las cosas fáciles**.

## ¿Y a mí qué? (≈ 60 s)

En la ciudad, Kevin quiere una bicicleta de 360.000 pesos para ir al colegio. Antes decía "algún día". Ahora tiene meta, cifra y fecha: 30.000 pesos al mes durante un año. Separa esa plata apenas la recibe, en un frasco que no abre, y marca en una hoja cuánto lleva. Ver la línea subir lo ayuda a no rendirse.

En el campo, Doña Marta gana unos 11.000 pesos a la semana con sus huevos. Quiere comprar diez gallinas más, a 25.000 cada una: 250.000 pesos. Si guarda 10.000 a la semana, en 25 semanas las tiene, y con ellas su negocio crece. Su meta no es un gusto: es una inversión.

Una meta convierte "no gastar" en "estar construyendo algo".

## La puerta abierta (≈ 30 s)

Para conversar: **si supieras con certeza que lo vas a lograr, ¿para qué ahorrarías?** ¿Y qué te haría más fácil no tocar esa plata?

El siguiente nodo es **Dónde guardar el dinero**: el frasco, la cuenta de ahorros o la billetera digital, y qué gana o pierde tu plata en cada lugar.

---

## Puente académico

Una meta de ahorro es una **ecuación lineal**. Si empiezas con un ahorro inicial *I* y guardas *a* pesos cada mes, después de *m* meses tienes:

> **Ahorro = I + a × m**

Si quieres saber cuántos meses te faltan para llegar a una meta *M*, despejas: **m = (M − I) ÷ a**. Y si dibujas el ahorro mes a mes, obtienes una **línea recta**: la pendiente es lo que ahorras cada mes. Cuanto más empinada, más rápido llegas.

Un poco de historia: guardar monedas en un recipiente cerrado es muy antiguo. Se han encontrado alcancías de barro de la Antigua Grecia, de hace más de 2.000 años, algunas con forma de templo. <!-- VERIFICAR: alcancía de Priene (siglo II a. C.); confirmar fecha y fuente antes de aprobar. -->

## Ejercicios

1. **(Resuelto)** Kevin quiere una bicicleta de 360.000 pesos en 12 meses. ¿Cuánto debe ahorrar al mes?
    - 360.000 ÷ 12 = **30.000 pesos al mes**.
2. **(Resuelto)** Laura ya tiene 60.000 pesos ahorrados y guarda 25.000 al mes. Quiere llegar a 210.000. ¿Cuántos meses le faltan?
    - Le faltan 210.000 − 60.000 = 150.000.
    - 150.000 ÷ 25.000 = **6 meses**.
3. Quieres reunir 150.000 pesos en 5 meses. ¿Cuánto debes ahorrar cada mes?
4. Una familia gasta 400.000 pesos al mes y quiere un fondo de emergencias equivalente a 3 meses de gastos. ¿De cuánto es el fondo? Si ahorran 100.000 al mes, ¿cuánto tardan en completarlo?
5. Martín empieza con 20.000 pesos y ahorra 15.000 al mes. Haz una tabla de su ahorro del mes 0 al mes 6 y dibuja la gráfica. ¿Qué forma tiene?
6. Sara tiene dos metas para dentro de 6 meses: un celular de 300.000 y un paseo de 120.000. Puede ahorrar 50.000 al mes. ¿Le alcanza para las dos? Si no, propón dos soluciones distintas.
7. Convierte esta meta vaga en una meta concreta con para qué, cuánto y para cuándo: *"Quiero ahorrar más este año"*.
8. Doña Marta quiere comprar 10 gallinas a 25.000 pesos cada una. ¿Cuánto necesita? ¿Cuántas semanas tarda si ahorra 6.000 a la semana? ¿Y si ahorra 10.000?

<details>
<summary>Soluciones</summary>

3. 150.000 ÷ 5 = **30.000 pesos al mes**.
4. Fondo: 400.000 × 3 = **1.200.000 pesos**. Tiempo: 1.200.000 ÷ 100.000 = **12 meses**.
5. Ahorro = 20.000 + 15.000 × m. Mes 0: 20.000; mes 1: 35.000; mes 2: 50.000; mes 3: 65.000; mes 4: 80.000; mes 5: 95.000; mes 6: **110.000**. La gráfica es una **línea recta** que sube 15.000 cada mes y empieza en 20.000.
6. Necesita 300.000 + 120.000 = 420.000, es decir, 420.000 ÷ 6 = 70.000 al mes. Con 50.000 al mes reúne 50.000 × 6 = **300.000**: **no alcanza** para las dos. Soluciones posibles: priorizar una meta y aplazar la otra; extender el plazo (420.000 ÷ 50.000 = 8,4 → 9 meses); aumentar el ahorro mensual reduciendo gustos o con un ingreso extra; buscar una versión más barata de alguna de las dos. Cualquier propuesta es válida si cuadra.
7. Ejemplo: *"Voy a ahorrar 240.000 pesos para un curso de inglés, guardando 20.000 al mes desde enero hasta diciembre."* Se evalúa que tenga para qué, cuánto y para cuándo, y que la cuenta cuadre.
8. Necesita 10 × 25.000 = **250.000 pesos**. Con 6.000 a la semana: 250.000 ÷ 6.000 = 41,7 → **42 semanas**. Con 10.000 a la semana: 250.000 ÷ 10.000 = **25 semanas**.

</details>

## Caso práctico (evidencia de dominio)

**Mi meta en serio.**

1. Elige una meta real o imaginaria y escríbela con **para qué, cuánto y para cuándo**.
2. Calcula cuánto debes ahorrar cada semana o cada mes.
3. Diseña una forma de **hacértelo fácil**: dónde vas a guardar la plata, cuándo vas a separarla y cómo vas a ver tu avance (una tabla, una gráfica, un frasco transparente).
4. Durante **4 semanas**, registra cuánto llevas y dibuja tu línea de ahorro. Si te desvías, escribe qué pasó y cómo ajustas el plan.

**Entrega:** la meta escrita, la cuenta, la gráfica de 4 semanas y un párrafo corto sobre lo que aprendiste. Si no manejas dinero, puedes ahorrar otra cosa medible (minutos de lectura, por ejemplo) o simular el plan de Kevin.

**Se evalúa así:**

- La meta tiene para qué, cuánto y para cuándo.
- La cuenta del ahorro periódico es correcta.
- Hay al menos una estrategia concreta para hacerlo fácil.
- El registro y la gráfica muestran 4 semanas, con ajustes explicados si hubo desvíos.

## Errores comunes

- **Ahorrar "lo que sobre".** Casi nunca sobra; se separa primero (ver Presupuesto).
- **Metas vagas.** "Ahorrar más" no es una meta: no se puede medir ni saber cuándo se cumple.
- **Guardar la plata donde es fácil gastarla.** Si está a la mano, se usa. Separarla ayuda.
- **Usar el fondo de emergencias para gustos.** Ese dinero existe para que un imprevisto no se vuelva deuda.
- **Rendirse al primer desvío.** Un mes malo no arruina la meta: se ajusta el plan y se sigue.
- **Creer que es solo fuerza de voluntad.** Las condiciones importan; por eso conviene diseñar el ahorro para que sea fácil.

## Para el docente ancla

- **Tiempo:** una sesión de 45 a 60 minutos y cuatro semanas de seguimiento ligero del caso práctico.
- **Cómo abrir:** cuenta la historia del malvavisco y pregunta antes del giro: "¿qué creen que les pasó, de grandes, a los niños que esperaron?". Luego revela el resultado de 2018.
- **Para conversar:** ¿esperar es fuerza de voluntad o confianza? ¿Qué hace más fácil o más difícil ahorrar en tu casa o en tu barrio?
- **Cuidado:** el giro del experimento es importante. No uses la historia para decir que quien no ahorra es "débil": las condiciones de cada familia pesan mucho.
- **Siguiente nodo:** Dónde guardar el dinero.
