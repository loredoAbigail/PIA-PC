from scapy.all import Ether, ARP, srp, IP, ICMP, TCP, sr
import csv, os

def opcion_1():
    # Define el rango de IPs de tu red local
    rango_red = "192.168.0.0/24"

    print(f"Escaneando red local: {rango_red}")

    hosts = []           # lista de (ip, mac) o (ip, None) si no hay MAC
    used_layer2 = False  # indica si pudimos usar srp (capa 2)

    # Intentamos hacer un ARP sweep por capa 2 (Ether / ARP).
    try:
        paquete = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=rango_red)
        respuestas, _ = srp(paquete, timeout=3, verbose=0)

        # Recopilamos respuestas y filtramos duplicados manteniendo el primer visto
        seen = set()
        for _, respuesta in respuestas:
            ip = respuesta.psrc
            mac = respuesta.hwsrc
            if ip not in seen:
                seen.add(ip)
                hosts.append((ip, mac))
                print(f"Host encontrado → IP: {ip} | MAC: {mac}")

        used_layer2 = True

    except Exception as e:
        print("No fue posible usar ARP en capa 2 (srp). Usando fallback por ICMP (ping sweep).")
        # Fallback: ping sweep en rango (no devuelve MACs)
        paquete_ping = IP(dst=rango_red) / ICMP()
        respuestas, _ = sr(paquete_ping, timeout=2, verbose=0)

        seen = set()
        for enviado, recibido in respuestas:
            ip = recibido.src
            if ip not in seen:
                seen.add(ip)
                hosts.append((ip, None))
                print(f"Host activo → IP: {ip}")

    if not hosts:
        print("No se encontraron hosts activos. Comprueba la red o aumenta los timeouts.")
        return

     # Asegurarse de que exista carpeta results/
    out_dir = "results"
    os.makedirs(out_dir, exist_ok=True)

    # Rutas de salida (archivo ARP y CSV dentro de results/)
    arp_file = os.path.join(out_dir, "arp_hosts.txt")
    csv_file = os.path.join(out_dir, "syn_scan.csv")



    # Guarda los resultados en un archivo (si hay MACs, las incluye; si no, guarda solo la IP)
    with open("arp_hosts.txt", "w") as archivo:
        for ip, mac in hosts:
            if mac:
                archivo.write(f"{ip},{mac}\n")
            else:
                archivo.write(f"{ip}\n")

    print("Resultados guardados en arp_hosts.txt")

    # Lee las IPs desde el archivo generado (maneja líneas con o sin MAC)
    with open("arp_hosts.txt") as archivo:
        hosts_ips = []
        for line in archivo:
            line = line.strip()
            if not line:
                continue
            ip = line.split(",")[0].strip()
            if ip:
                hosts_ips.append(ip)

    # Define los puertos a escanear
    puertos = [22, 80, 443]
    resultados = []

    print("Iniciando escaneo SYN de puertos… (esto puede requerir permisos de administrador)")
    
    for ip in hosts_ips:
        abiertos = []
        for puerto in puertos:
            paquete = IP(dst=ip) / TCP(dport=puerto, flags="S")
            respuesta, _ = sr(paquete, timeout=1, verbose=0)
            if respuesta:
                abiertos.append(puerto)

        print(f"{ip} → Puertos abiertos: {abiertos}")
        resultados.append((ip, abiertos))

    # Guarda los resultados en un archivo CSV
    with open("syn_scan.csv", "w", newline="") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["IP"] + [str(p) for p in puertos])



        for ip, abiertos in resultados:
            fila = [ip] + [("Sí" if p in abiertos else "No") for p in puertos]
            writer.writerow(fila)

    print("Resultados guardados en syn_scan.csv")


