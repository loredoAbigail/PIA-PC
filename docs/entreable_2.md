#  Entregable 2 – MVP funcional parcial - Borrador
 
> Este entregable forma parte del repositorio único del proyecto PIA. La propuesta técnica se encuentra en [`/proposals/propuesta.md`](../proposals/propuesta.md).
 
---
 
##  Tarea implementada
 
- **Nombre de la tarea**: Descubrimiento de hosts y detección de puertos abiertos.
- **Descripción funcional**:  
> Identifica los equipos activos en la red y verifica si exponen servicios críticos. Permitiendo así conocer la superficie de ataque y detectar posibles puntos vulnerables.
 
---
 
##  Entradas utilizadas
 
> Iterativa (selección del menú), COnfiguración (rango de red, puertos a escanear, tiempo deespera) y arp_host.txt que es para el host a escanear.
 
---
 
##  Salidas generadas
 
> arp_hosts.txt, syn_scan.csv
 
---
 
##  Evidencia reproducible
 
- **Ruta a ejemplos de ejecución**: [`/examples`](../examples)
- **Ruta a logs estructurados**: [`/examples/logs.jsonl`](../examples/syn_scan.csv)
- **Script de ejecución**: [`/src/run_tarea1.sh`](../src/run_tarea1.sh)
 
---
 
##  Documentación técnica
 
## Ejecución
`python parte1.py` → Seleccionar opción 1 → Escaneo automático ARP + SYN.

## Dependencias
`pip install scapy`

## Observaciones
- Escaneo funcional ARP + SYN
- Solo opción 1 implementada  
- Rango hardcodeado (192.168.0.0/24)
- Sin manejo de errores
- Archivos de salida incorrectos (usa arp_hosts.txt, syn_scan.csv)
- Faltan: findings.csv, alerts.jsonl, executive_summary.md

## Salidas Actuales
arp_hosts.txt (IPs/MACs), syn_scan.csv (puertos por host)

---
 
##  Colaboración
 
> Todo el equipo contribuyo con la creación del script, haciendo de este al mismo tiempo estando todos al pendiente del mismo.
 
---
 
##  Observaciones
 
> Lo que quedaría pendiente es implementar opciones 2-3, corregir archivos de salida, agregar análisis de autenticación.
> Los errores en scripts se iran editando con forme el proyecto vaya tomando forma, la organización es primordial y tenemos que corregir nuestros errores.
> La Tarea 1 se ejecuta con facilidad, lo aprendido fue que tenemos que separar el main script de las funciones de nuestras tareas.
