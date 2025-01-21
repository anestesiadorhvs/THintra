El protocolo es un protocolo de solicitud/respuesta basado en mensajes.
Los datos disponibles a través del protocolo de exportación de datos se modelan como valores de atributo de objetos de información. Estos incluyen:
• Numéricos: Representan el estado y el valor de las mediciones numéricas, como la frecuencia cardíaca.
• Datos de alarma: Incluye alarmas técnicas y de pacientes, con tasas de actualización en tiempo real de hasta 1024 ms.
• Datos de onda: Se pueden acceder a los datos de onda, pero es importante tener en cuenta las limitaciones de tamaño de los mensajes y la necesidad de realizar un seguimiento de las marcas de tiempo para detectar muestras de onda faltantes.
• Datos del sistema del monitor: Incluye información sobre el estado operativo del monitor.
• Datos demográficos del paciente: Datos introducidos por el usuario en el monitor.

El esquema de comunicación entre el cliente (ordenador) y el servidor (monitor IntelliVue) se basa en un diálogo de solicitud/respuesta.
1.Conexión:
El cliente envía una solicitud de asociación al servidor para establecer una conexión.
El servidor responde con un resultado de asociación, que puede ser una aceptación o un rechazo.
2.Inicio:
Si la asociación es aceptada, el servidor envía un mensaje de informe de evento de creación de MDS (Sistema de Dispositivo Médico) que contiene información sobre la configuración del sistema.
El cliente confirma la recepción del informe de evento con un mensaje de resultado de evento de creación de MDS.
3.Acceso a datos:
El cliente envía solicitudes de datos para acceder a los datos del monitor.
Existen dos tipos de solicitudes de datos de sondeo:
▪ Solicitud de datos única: Solicita datos específicos en un solo mensaje de respuesta.
▪ Solicitud de datos extendida: Solicita datos de forma continua durante un período definido por el cliente.

El servidor responde a las solicitudes de datos c
4. Liberación de la conexión:
cuando el cliente desea terminar la conexión, envía una solicitud de liberación.
El servidor responde con un resultado de liberación para confirmar que la asociación ha finalizado.

Diagrama de flujo del diálogo del protocolo:
Cliente                        Servidor
|                                |
|---- Solicitud de Asociación -->|
|<- Resultado de Asociación -----|
|                                |
|                                |
|---- Informe de Evento MDS ---->|
|<- Resultado de Evento MDS -----|
|                                |
|---- Solicitud de Datos ------->|
|<-  Resultado de Datos   -------|
|                                |
|       ...                      |
|                                |
|---- Solicitud de Liberación -->|
|<- Resultado de Liberación  ----|
|                                |

La estructura de los mensajes es la siguinte:
Encabezado de sesión/presentación: Define el tipo de mensaje y contiene información sobre la sesión y la presentación.

Encabezado de operación remota: Permite distinguir entre diferentes tipos de mensajes, como comandos, respuestas y errores.

Encabezado de comando: Contiene la parte común de la estructura de datos del comando identificada en el encabezado de operación remota.
Parámetros específicos del comando: Se añaden a la estructura del mensaje genérico y varían según el comando.

Encabezado de Sesión/Presentación:
Longitud: Define el número de bytes restantes en el mensaje.

Encabezado de Operación Remota:
Existen cuatro tipos de mensajes de operación remota:
• Invocación de operación remota: Se utiliza para enviar un comando al receptor, que debe responder con un mensaje de resultado o error. Contiene:
◦ ID de invocación: Identifica la transacción y debe ser único mientras la operación está en proceso.
◦ Tipo de comando: Define el tipo de comando que se envía.
◦ Longitud: Define el número de bytes restantes en el mensaje.

•Resultado de operación remota simple: Es la respuesta a una invocación de operación remota que requiere confirmación. Contiene:
◦ ID de invocación: Refleja el ID de invocación del mensaje de invocación original.
◦ Tipo de comando: Define el tipo de comando que se devuelve.
◦ Longitud: Define el número de bytes restantes en el mensaje.

• Resultado de operación remota enlazada: Se utiliza para enviar resultados grandes que exceden el tamaño máximo del mensaje, dividiéndolos en múltiples mensajes. Contiene:
◦ ID enlazada: Identifica cada mensaje en una secuencia de mensajes enlazados.
◦ ID de invocación: Refleja el ID de invocación del mensaje de invocación original.
◦ Tipo de comando: Define el tipo de comando que se devuelve.
◦ Longitud: Define el número de bytes restantes en el mensaje.

Error de operación remota: Se devuelve si se detecta un error a nivel de operación remota. Contiene:
◦
ID de invocación: Refleja el ID de invocación del mensaje de invocación original.
◦
Valor de error: Indica el tipo de error que se ha producido.
◦
Longitud: Define el número de bytes restantes en el mensaje.
Encabezado de Comando:
El encabezado de comando varía según el tipo de comando. Algunos ejemplos de comandos son:
•
Informe de evento: Se utiliza para enviar información no solicitada desde el monitor al cliente.
•
Acción: Se utiliza para invocar una actividad en el lado del receptor.
•
Get: Se utiliza para solicitar valores de atributo de objetos administrados.
•
Set: Se utiliza para establecer valores de atributo de objetos administrados.
