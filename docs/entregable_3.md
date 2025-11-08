#  Entregable 3 – Integración parcial y plan de IA
 
> Este entregable forma parte del repositorio único del proyecto PIA. La propuesta técnica se encuentra en [`/proposals/propuesta.md`](../proposals/propuesta.md).
 
---
 
##  Tareas integradas
 
- **Tarea 1**: Descubrimiento de hosts y detección de puertos abiertos.
- **Tarea 2**: Análisis de patrones de autenticación y detección de accesos sospechosos.
- **Descripción de la integración**:  
> El flujo ejecuta un proceso secuencial donde cada tarea se alimenta de la salida de la anterior
> Entradas:
  - Archivo CSV generado desde PowerShell (`registro_eventos.csv`)
  - Estructura: 
    - `Id` (Event ID): 4624 (éxito) / 4625 (fallo)
    - `Message`: Texto completo del evento de autenticación
>Procesamiento:
  - Extracción de IPs: Expresión regular `\d{1,3}(?:\.\d{1,3}){3}`
  - Clasificación: 
    - Event ID 4625 → Contador de fallos por IP
    - Event ID 4624 → Contador de éxitos por IP
  - Estructura: Diccionarios `defaultdict` para acumulación eficiente
>Análisis:
  - Detección de patrones: ≥ 3 intentos fallidos desde misma IP
  - Criterio de riesgo: Frecuencia de intentos fallidos
>Salidas generadas:
  Archivo Principal: `_analisis.json`
  ```json
  {
    "métricas_totales": {
      "total de ips": "X",
      "fallos_totales": "Y",
      "exitos totales": "Z"
    },
    "alertas": [
      {
        "Ip": "192.168.1.100",
        "Intentos fallidos": 5,
        "Alerta": "Posible fuerza bruta detectada"
      }
    ]
  }
```
---
 
##  Uso de dos lenguajes de programación
 
- **Lenguajes utilizados**: Python + PowerShell
- **Forma de integración**:  
> El sistema actual implementa una arquitectura monolítica modularizada donde todas las funcionalidades de análisis de seguridad se encapsulan en un único script Python auto-contenido. Esta aproximación ofrece simplicidad operacional mientras mantiene una estructura interna organizada para el procesamiento de eventos de autenticación.
 
- **Archivo relevante**: [`/src/run_tarea2.py`]
 
---
 
##  Plan de uso de IA
 
- **Propósito del uso de IA**:  
> Detección en tiempo real de patrones sospechosos de autenticación
> Análisis predictivo de posibles ataques de fuerza bruta
> Clasificación inteligente de intentos legítimos vs. maliciosos
> Correlación automática de eventos de login across múltiples servicios críticos
> Generación automática de alertas contextualizadas para el equipo de seguridad
 
- **Punto de integración en el flujo**:  
> Post-captura de logs de AD, SSH, VPN, O365, AWS CloudTrail
> Pre-decisión de respuesta automática
> Post-detección de múltiples fallos para análisis contextual
 
- **Modelo/API previsto**: LLM para análisis contextual avanzado
 
- **Archivo del plan**: [`/docs/ai_plan.md`](ai_plan.md)
 
---
 
##  Prompt inicial
 
- **Archivo de plantilla**: [`/prompts/prompt_v1.json`](../prompts/prompt_v1.json)
- **Campos incluidos**:  
  - `version`
  - `tarea`
  - `template`
  - `instrucciones`
 
---
 
##  Evidencia reproducible
 
- **Logs estructurados**: [`/examples/_analisis.json`](../examples/_analisis.json)
- **Ejemplos de ejecución**: [`/examples`](../examples)
- **Script de orquestación o módulo funcional**: [`/srs`](../srs)
 
---
 
##  Colaboración
 
> Todo el equipo contribuyo con la creación del script, haciendo de este al mismo tiempo estando todos al pendiente del mismo.
 
---
 
##  Observaciones
 
> Integraciones: Webhook a N8N para orquestación automática, APIs de Firewall para bloqueo automático, Sistemas de Notificación (Slack/Email), Base de datos para historial y análisis temporal.
> Mejoras Técnicas: Umbrales dinámicos basados en comportamiento histórico, Contexto geográfico con API GeoIP, Detección de horarios no laborales, Dashboard visual para monitoreo.
> Estrategia Híbrida: IA para análisis contextual y correlación avanzada, Reglas para detección simple de fuerza bruta (ya implementado), Automation para respuesta inmediata vía N8N.
> Aprendizaje: IA mejorará precisión pero no reemplazará reglas base, nuestra prioridad es conectar con N8N antes de refinamientos complejos, el sistema debe evolucionar de detección a respuesta automática.
> Nuestros proximos pasos son la implementacion de la tarea #3, implementación IA contextual y APIs de bloqueo automático.
