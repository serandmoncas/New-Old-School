---
id: dinero.historial-crediticio
titulo: Historial crediticio (CO)
modulo: dinero
alcance: local
pais: co
nodo_base: dinero.historial-crediticio
nivel: 2
prerrequisitos: []
conecta_con: []
estado: en-revision
responsable: serandmoncas
revisores: []
revision_experta: true
procedencia:
- {autor: claude, modelo: claude-opus-5-5, fecha: '2026-10-13', nota: primera versión; reglas de la Ley 2157 de 2021 consultadas en el texto oficial el 2026-10-13}
recursos:
- {titulo: 'Ley 1266 de 2008 (hábeas data financiero), texto oficial, consultado 2026-10-13', url: 'http://www.secretariasenado.gov.co/senado/basedoc/ley_1266_2008.html', licencia: dominio público}
- {titulo: 'Ley 2157 de 2021 ("borrón y cuenta nueva"), texto oficial, consultado 2026-10-13', url: 'http://www.secretariasenado.gov.co/senado/basedoc/ley_2157_2021.html', licencia: dominio público}
- {titulo: 'Superintendencia de Industria y Comercio — protección de datos personales', url: 'https://www.sic.gov.co', licencia: dominio público}
- {titulo: 'Superintendencia Financiera de Colombia — Defensor del Consumidor Financiero y quejas', url: 'https://www.superfinanciera.gov.co', licencia: dominio público}
actualizado: '2026-10-13'
---

# Historial crediticio (CO)

> Adaptación local. Complementa el nodo del núcleo: [../../nucleo/historial-crediticio.md](../../nucleo/historial-crediticio.md). No repitas su explicación.
> Reglas consultadas el 13 de octubre de 2026 en el texto oficial de las leyes.

## Cómo funciona aquí

En Colombia, las **centrales de riesgo** más conocidas son **DataCrédito Experian** y **TransUnion** (antes CIFIN). No son del Estado ni deciden si te prestan: guardan la información que les reportan bancos, cooperativas, almacenes que venden a crédito y empresas de telefonía celular, y la entregan a quien tú autorices.

Las reglas están en la **Ley 1266 de 2008**, llamada de **hábeas data financiero**. La **Ley 2157 de 2021**, conocida como de "borrón y cuenta nueva", la modificó. Lo esencial:

- **Te tienen que avisar antes.** Antes de reportarte en mora, la entidad debe comunicártelo, y entre ese aviso y el reporte deben pasar al menos **20 días calendario**.
- **Deudas pequeñas.** Si la deuda es de hasta el **15 % de un salario mínimo** (unos $262.636 en 2026), solo te pueden reportar después de **dos avisos en días diferentes**.
- **El reporte negativo no es eterno.** Cuando pagas, el dato negativo dura **el doble del tiempo que estuviste en mora, y máximo cuatro años**. Si te atrasaste tres meses, el reporte desaparece seis meses después de pagar.
- **Si nunca pagas,** el dato negativo caduca ocho años después de que la deuda entró en mora. Eso no significa que la deuda desaparezca: te la pueden seguir cobrando según las reglas de prescripción. <!-- VERIFICAR: interacción entre la caducidad del dato (8 años) y la prescripción de la obligación; fuente: SIC o abogado -->
- **Consultar es gratis y no te baja el puntaje.** Puedes revisar tu reporte sin costo cuando quieras, y la ley prohíbe que esas consultas bajen tu calificación.
- **Puedes reclamar.** Si hay un error, presentas una petición o reclamo a la entidad que te reportó o a la central de riesgo. Si no te responden, puedes acudir a la **Superintendencia de Industria y Comercio** (SIC) o, si es una entidad financiera, a la **Superintendencia Financiera** (SFC).

**Ojo con las estafas:** nadie te puede cobrar por "sacarte de DataCrédito". Si pagas tu deuda, el dato se actualiza solo con los plazos de la ley. Quien ofrece "limpiar tu historial" por plata te está engañando.

## Ejemplo con datos locales

Andrés compró un celular a crédito en un almacén de cadena con cuotas de $120.000. Perdió el trabajo y dejó de pagar durante **cinco meses**. Recibió un mensaje del almacén avisándole que lo iban a reportar, y veinte días después apareció en mora en las centrales de riesgo.

Cuando consiguió empleo nuevo, se puso al día. Ese día empezó a correr el plazo: su reporte negativo durará **diez meses** (el doble de cinco) y luego desaparecerá. Mientras tanto, un banco le negó una tarjeta de crédito.

Su hermana Sofía también tuvo un atraso, pero de solo un mes, por olvido. Pagó en cuanto se dio cuenta. Su reporte negativo duró **dos meses**. Después programó el pago automático de sus cuotas.

## Entidades y recursos oficiales

- **DataCrédito Experian**: consulta gratuita de tu historial en su portal para personas. [datacredito.com.co](https://www.datacredito.com.co).
- **TransUnion Colombia**: consulta gratuita para personas. [transunion.co](https://www.transunion.co).
- **Superintendencia de Industria y Comercio (SIC)**: reclamos por manejo de tus datos. [sic.gov.co](https://www.sic.gov.co).
- **Superintendencia Financiera de Colombia (SFC)**: quejas contra bancos y entidades vigiladas. Cada entidad tiene además un **Defensor del Consumidor Financiero**. [superfinanciera.gov.co](https://www.superfinanciera.gov.co).
- **Texto oficial de las leyes 1266 de 2008 y 2157 de 2021**: Secretaría del Senado (ver `recursos`).

<!-- VERIFICAR: URLs vigentes de los portales de consulta gratuita para personas de DataCrédito Experian y TransUnion -->

## Ejercicios con contexto local

1. Pedro estuvo **siete meses** en mora con una cuota y pagó todo el 1 de marzo. ¿Hasta cuándo puede aparecer el dato negativo? ¿Y si la mora hubiera sido de tres años?
2. Laura debe $200.000 a una tienda que le vendió a crédito. ¿Esa deuda está por debajo del 15 % del salario mínimo de 2026? ¿Qué tiene que hacer la tienda antes de reportarla?
3. Un aviso en redes dice: "Te sacamos de DataCrédito en 48 horas por solo $150.000". Explica, con lo que dice la ley, por qué es una estafa.
4. Con permiso de un adulto de tu casa, revisen juntos su reporte en el portal gratuito de una central de riesgo. ¿Qué información aparece? ¿Hay algún dato que les parezca un error? (No compartan los datos con nadie más.)

<details>
<summary>Soluciones</summary>

1. El dato dura el doble de la mora: 7 × 2 = **14 meses**, contados desde el pago. Aparece hasta comienzos de mayo del año siguiente. Con tres años de mora, el doble serían seis años, pero la ley pone un **máximo de cuatro**, contados desde el pago.
2. El 15 % de $1.750.905 es **$262.636**, así que $200.000 sí está por debajo. La tienda debe enviarle **al menos dos avisos, en días diferentes**, y esperar **20 días calendario** después del último antes de reportarla.
3. Nadie puede borrar un reporte a cambio de dinero. Si el dato es cierto, solo desaparece con los plazos de la ley (el doble de la mora, máximo cuatro años, contados desde el pago). Si es un error, el reclamo es **gratuito** ante la entidad, la central de riesgo o la SIC.
4. Respuesta abierta. Se valora que identifiquen las obligaciones, su estado (al día o en mora) y que sepan dónde reclamar un error.

</details>
