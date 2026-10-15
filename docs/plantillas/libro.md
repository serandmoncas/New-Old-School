---
id: slug-del-libro              # igual al nombre del archivo: biblioteca/<slug>.md
titulo: Título en español
titulo_original: null           # solo si el libro se escribió en otro idioma
autor: Nombre del autor
publicado: '1850'               # texto: un año, "hacia 1597" o "s. VIII a. C."
tipo: novela                    # novela | cuento | fabula | poema | teatro | ensayo | tratado | divulgacion | historia | monografia
acceso: dominio-publico         # dominio-publico | con-derechos
texto_libre: null               # URL de una edición libre y legal; solo si es dominio público
temas: []                       # solo temas de biblioteca/_temas.yaml
cruza_con: []                   # - {libro: otro-slug, por: "una frase: qué tienen en común"}
nodos: []                       # ids del currículo, ej. dinero.presupuesto
estado: propuesta               # propuesta | aceptado | retirado
procedencia: []                 # - {autor: usuario, modelo: nombre-del-modelo-o-ninguno, fecha: AAAA-MM-DD}
actualizado: AAAA-MM-DD
---

# Título en español

## De qué trata

Dos o tres frases, sin destripar el final si no hace falta.

## Resumen

Recomendado; obligatorio en divulgación, ensayo, tratado y monografía. La estructura del libro (partes o capítulos, comprobados con el índice de una edición real, no de memoria) y, al final, su tesis en una frase en negrita. Si una obra de ficción no lo necesita, basta con "De qué trata".

## Por qué está en la biblioteca

Qué idea del currículo ilumina y por qué un estudiante de 12 a 16 años la va a entender mejor con este libro.

## Análisis

Recomendado; obligatorio en divulgación, ensayo, tratado y monografía. Tres partes:

**Lo que hace bien.** Sus aportes, con la evidencia que los respalda.

**Sus límites.** Lo que exagera, lo que no se sostiene y lo que la investigación posterior encontró, aunque el libro sea famoso. Separa lo comprobado de lo que solo "se dice".

**Para el colegio.** Cómo usarlo en New Old School y con qué otros libros o nodos conviene leerlo.

Cada estudio citado lleva enlace a su DOI, comprobado en Crossref (`https://api.crossref.org/works/<DOI>`), y su resultado se resume a partir del resumen del estudio, no de un comentario de terceros. Lo que no se pueda confirmar se quita; si es importante, se deja con `<!-- VERIFICAR: ... -->`.

## Para leer en clase

El fragmento concreto (capítulo, canto, acto) que vale la pena leer, y una pregunta para conversar.

## Con cuidado

Opcional: temas sensibles o ideas de su época que el docente debe poner en contexto.
