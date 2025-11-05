#  Propuesta técnica del proyecto PIA
 
##  Título del proyecto
LoginSentinel
 
##  Descripción general del proyecto
LoginSentinel es un proyecto enfocado en la detección de intentos de autenticación y el monitoreo de servicios esenciales en una red (SSH, HTTP y HTTPS).
Su objetivo es identificar accesos potencialmente no autorizados, analizar comportamientos sospechosos y generar reportes automatizados que apoyen la toma de decisiones en entornos de ciberseguridad.
 
---
 
##  Tareas propuestas
 
###  Tarea 1
- **Título**: Descubrimiento de hosts y detección de puertos abiertos.
- **Propósito**: Identificar equipos activos en la red y verificar si exponen servicios críticos como SSH (22), HTTP (80) y HTTPS (443). Esto permite conocer la superficie de ataque y detectar posibles puntos vulnerables.
- **Rol o área relacionada**: SOC (Security Operations Center) / Blue Team
- **Entradas esperadas**: Lista de IPs en formato CSV o JSON
Ejemplo:

ip
192.168.1.10
192.168.1.11

- **Salidas esperadas**: Archivo findings.csv con las IPs y los puertos abiertos detectados.
Ejemplo:

ip,port,status
192.168.1.10,22,open
192.168.1.10,443,closed

- **Descripción del procedimiento**: El script toma una lista de IPs y ejecuta un escaneo controlado usando herramientas o módulos de red.
Los resultados se procesan en Python para generar un resumen con los puertos activos y se almacenan en formato CSV para ser utilizados en las siguientes tareas.
- **Complejidad técnica**: Parsing de salidas, automatización básica, uso de librerías de red (scapy, subprocess, csv).
- **Controles éticos**: Solo se usan direcciones IP simuladas o de laboratorio. No se realiza ningún escaneo sobre redes reales.
- **Dependencias**: Python 3.x, librerías Scapy, módulos TCP, sr, csv, subprocess.
 
###  Tarea 2
- **Título**: Análisis de patrones de autenticación y detección de accesos sospechosos.
- **Propósito**: Analizar los registros de inicio de sesión para detectar patrones de intentos fallidos o repetitivos que indiquen posibles ataques de fuerza bruta o accesos indebidos.
- **Rol o área relacionada**: Blue Team / SOC (Monitoreo de eventos de seguridad).
- **Entradas esperadas**: Archivo auth_logs.json con eventos de autenticación simulados.
Ejemplo:
[
  {"timestamp": "2025-11-04T12:00:00Z", "ip": "192.168.1.10", "user": "admin", "status": "fail"},
  {"timestamp": "2025-11-04T12:01:00Z", "ip": "192.168.1.10", "user": "admin", "status": "fail"},
  {"timestamp": "2025-11-04T12:02:00Z", "ip": "192.168.1.10", "user": "admin", "status": "success"}
]

- **Salidas esperadas**: Archivo alerts.json con IPs o usuarios sospechosos y el tipo de alerta.
Ejemplo:
[
  {"ip": "192.168.1.10", "user": "admin", "alerts": ["Múltiples fallos consecutivos"], "risk_level": "high"}

]

- **Descripción del procedimiento**: El script procesa los registros en formato JSON, agrupa los intentos por IP y usuario, y calcula métricas básicas.
Si se detectan múltiples fallos seguidos o intentos desde IPs distintas para un mismo usuario, se genera una alerta. Los resultados se exportan a un archivo json.
- **Complejidad técnica**: Parsing de JSON, correlación de eventos, uso de librerías (json, collections, datetime), automatización de análisis.
- **Controles éticos**: Los logs son totalmente simulados, sin datos reales de usuarios. El análisis se realiza en un entorno académico.
- **Dependencias**: Python 3.x, librerías json, collections, datetime.
 
###  Tarea 3 (opcional)
- **Título**: Creación de reporte ejecutivo automatizado y enriquecido con IA.
- **Propósito**: Transformar los resultados técnicos de las tareas previas en un reporte comprensible para analistas o responsables de seguridad, con resúmenes generados mediante una API de inteligencia artificial.
- **Rol o área relacionada**: Threat Intelligence / SOC Reporting.
- **Entradas esperadas**: Archivos csv y json generados por las tareas anteriores.
- **Salidas esperadas**: Genera un archivo json con toda la información organizada y envía ese resumen a una API de IA (por ejemplo, usando la librería requests y una clave API guardada en variable de entorno).
- **Descripción del procedimiento**: Integra la información de los archivos previos y crea un reporte estructurado en JSON, luego envía un resumen de los hallazgos a una API de IA para obtener un texto descriptivo y recomendaciones automatizadas.
- **Complejidad técnica**: Parsing y consolidación de datos, integración con API externa, manejo de errores (retries, backoff), uso de librerías (requests, pandas, os).
- **Controles éticos**: No se envían datos reales a la API; los prompts y respuestas se registran en /prompts para trazabilidad. Se usan variables de entorno para las claves API.
- **Dependencias**: Python 3.x, librerías requests, pandas, os, API key definida como variable de entorno (AI_API_KEY).
---
 
##  Estructura inicial del repositorio (ejemplo)
/src 
/docs 
/examples 
/proposals 
/tests 
/prompts 
README.md 
.gitignore
 

 
##  Evidencia de colaboración inicial (elegir uno o más)
 
- [ ] Commits realizados por más de un integrante
- [ ] Issues creados para organizar tareas
- [ ] Pull requests abiertos o revisados
- [ ] Actividad visible en GitHub desde el inicio del proyecto
 
---
 
##  Ubicación de entregables posteriores
 
Todos los avances y entregables estarán documentados en la carpeta `/docs` dentro de este mismo repositorio.
