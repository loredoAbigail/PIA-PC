import json
import requests
import ipaddress
from pathlib import Path

def opcion_3():

    # Rutas relativas dentro del proyecto
    input_path = Path("C://-------//_analisis.json")
    output_path = Path("outputs/reporte_tarea2.json")

    # Verificación del archivo JSON
    if not input_path.exists():
        print("\nNo se encontró el archivo de la tarea 2 (_analisis.json).")
        return

    # Carga de datos de la tarea 2
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Extraer IPs desde la sección de alertas
    ips = [alert["Ip"] for alert in data.get("alertas", [])]
    print(f"Se encontraron {len(ips)} IPs para analizar: {ips}")

    enriched = []

    for ip in ips:
        entry = {
            "ip": ip,
            "pais": "N/A",
            "region": "N/A",
            "organizacion": "N/A",
            "estatus": "fail",
            "reason": ""
        }

        # Para evitar consultar IPs privadas
        try:
            if ipaddress.ip_address(ip).is_private:
                entry["estatus"] = "skipped"
                entry["reason"] = "private_ip"
                enriched.append(entry)
                continue
        except ValueError:
            entry["reason"] = "invalid_ip"
            enriched.append(entry)
            continue

        # Consulta a API pública
        try:
            resp = requests.get(f"http://ip-api.com/json/{ip}", timeout=5).json()
            if resp.get("status") == "success":
                entry["pais"] = resp.get("country")
                entry["region"] = resp.get("regionName")
                entry["organizacion"] = resp.get("org")
                entry["estatus"] = "success"
            else:
                entry["reason"] = resp.get("message", "unknown_error")
        except requests.RequestException as e:
            entry["reason"] = f"request_error: {e}"

        enriched.append(entry)

    # Creación de carpeta de salida si no existe
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Guardar resultados
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(enriched, f, indent=4, ensure_ascii=False)

    print(f"Análisis completado. Resultado guardado en: {output_path}")
