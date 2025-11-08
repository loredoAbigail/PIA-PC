import csv
import re
import json
from collections import defaultdict

def opcion_2():
    # Ruta del archivo exportado desde PowerShell con el registro de ips, fallos, éxitos y fechas
    CSV_PATH = r"C:\\Users\\usuario\\Desktop\\pia08\\registro_eventos.csv"

    # Expresión regular para extraer la IP desde el texto del evento
    ip_re = re.compile(r'\d{1,3}(?:\.\d{1,3}){3}')

    # Contadores para intentos por IP
    failed_attempts = defaultdict(int) # intentos fallidos
    successful_attempts = defaultdict(int) # intentos exitosos

    # Abrir el archivo CSV y leer fila por fila
    with open(CSV_PATH, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            event_id = int(row["Id"])
            message = row["Message"]
            ip_match = ip_re.search(message)
            ip = ip_match.group(0) if ip_match else "unknown"

            # Contar según el tipo de evento
            if event_id == 4625:  # fallo
                failed_attempts[ip] += 1
            elif event_id == 4624:  # éxito
                successful_attempts[ip] += 1

    # Detectar posibles ataques de fuerza bruta
    alerts = []
    for ip, fails in failed_attempts.items():
        if fails >= 3:
            alerts.append({
                "Ip": ip,
                "Intentos fallidos": fails,
                "Alerta": "Posible fuerza bruta detectada"
            })

    # Crear resumen
    report = {
        "total de ips": len(set(failed_attempts.keys()) | set(successful_attempts.keys())),
        "fallos_totales": sum(failed_attempts.values()),
        "exitos totales": sum(successful_attempts.values()),
        "alertas": alerts
    }
    #Ruta del archivo JSON con el resumen
    with open("c:\\Users\\usuario\\Desktop\\pia08\\_analisis.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4)

    print("Análisis completado. Resultado guardado en carpeta.")
