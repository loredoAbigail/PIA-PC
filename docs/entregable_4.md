
#  Entregable 4 – Proyecto casi completo (90%)
 
> Este entregable forma parte del repositorio único del proyecto PIA. La propuesta técnica se encuentra en [`/proposals/propuesta.md`](../proposals/propuesta.md).
 
---
 
##  Flujo técnico consolidado
 
> Descripción del flujo completo entre tareas:  
> ¿Qué módulos están conectados? ¿Cómo fluye la información entre ellos? ¿Qué salidas se generan?

Los tres módulos del proyecto están conectados de forma secuencial, como si uno alimentara al siguiente.
Primero, la tarea 1 obtiene las IPs activas y revisa si tienen abiertos los puertos 22, 80 y 443.
Luego, la tarea 2 analiza registros simulados de intentos de conexión, detectando posibles ataques de fuerza bruta y generando un archivo con alertas.
Finalmente, la tarea 3 toma esas alertas (desde el archivo JSON de la tarea 2) y consulta una API pública para obtener más información sobre las IPs, como país, región u organización. 
---
 
##  IA integrada funcionalmente
 
- **Modelo/API utilizado**: [Ej. GPT-4, Azure OpenAI, simulación]
 Usamos simulación, una IA pública.
- **Punto de integración**:  
> ¿Dónde se invoca la IA dentro del flujo técnico?
La IA pública se invoca en la tarea 3 que nos ayuda a analizar los datos de la salida de la tarea 2, y también a enriquecer éstos datos para una mejor presentación.
 
- **Ejemplo de entrada/salida**:  
En este proyecto la IA se usa de forma complementaria para ayudar a analizar y enriquecer la información.
Por ejemplo, se aprovecha una API externa con capacidades de análisis automático, que interpreta las IPs sospechosas y devuelve datos relevantes como país, región u organización sin que el usuario tenga que hacerlo manualmente.
 
---
 
##  Evidencia reproducible
 
- **Archivos de salida**: [`/examples`](../examples)
- **Logs estructurados**: [`/examples/logs.jsonl`](../examples/logs.jsonl)
- **Script principal o de orquestación**: [`/scripts/run_pipeline.sh`] o [`/scripts/run_pipeline.ps1`]
 
---
 
##  Documentación técnica
 
> Instrucciones de ejecución:
-Abre la carpeta del proyecto en Visual Studio Code.
-Asegúrate de tener instalado Python 3.10 o superior.
-Instala las dependencias necesarias.
-Ejecuta el menú principal.
-Desde el menú selecciona:
--1: Escaneo de IPs y puertos abiertos.
--2: Análisis de intentos de autenticación.
--3: Enriquecimiento de IPs con datos de una API pública.


> Dependencias:requests, csv, json, re, collections, ipaddress, pathlib.


> Observaciones relevantes sobre el comportamiento del sistema:
Las tareas están conectadas entre sí:
-La salida de la tarea 2 (_analisis.json) se usa como entrada en la tarea 3.
-El proyecto no usa datos reales ni accede a sistemas externos sin autorización; los ejemplos son simulados y éticos.
-Si se desea probar con datos reales (por ejemplo, logs de Windows), debe hacerse en un entorno controlado y con permisos administrativos.
-El archivo final de la tarea 3 (reporte_tarea2.json) muestra los resultados de cada IP con información adicional del país, región u organización.
 
---
 
##  Colaboración
 
> ¿Quién trabajó en esta etapa? ¿Qué evidencia hay en GitHub (commits, issues, PRs)? ¿Cómo se distribuyeron los ajustes finales?
 
Todo el equipo contribuyo con la creación del script, haciendo de este al mismo tiempo estando todos al pendiente del mismo.
 
##  Observaciones
 
> ¿Qué falta por pulir antes de la entrega final? ¿Qué decisiones técnicas se tomaron? ¿Qué se aprendió en esta etapa?

Sólo nos faltaría pulir el GitHub, agregar datos finales y acomodar ciertas cosas. Tomamos la decisión de cambiar de IA, a una IA pública, una simulación. Aprendimos a usar una API pública para darle más contexto a los datos, por ejemplo, saber de dónde proviene una IP o a qué organización pertenece.
