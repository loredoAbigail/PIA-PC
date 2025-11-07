from scapy.all import Ether, ARP, srp, IP, TCP, sr
import csv

def opcion_1():
    # Define el rango de IPs de tu red local
    rango_red = "192.168.0.0/24"

    # Construye el paquete ARP dentro de un paquete Ethernet
    paquete = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=rango_red)

    print(f"Escaneando red local: {rango_red}")
    respuestas, _ = srp(paquete, timeout=3, verbose=0)

    # Procesa las respuestas
    hosts = []
    for _, respuesta in respuestas:
        ip = respuesta.psrc
        mac = respuesta.hwsrc
        hosts.append((ip, mac))
        print(f"Host encontrado → IP: {ip} | MAC: {mac}")

    # Guarda los resultados en un archivo
    with open("arp_hosts.txt", "w") as archivo:
        for ip, mac in hosts:
            archivo.write(f"{ip},{mac}\n")

    print("Resultados guardados en arp_hosts.txt")

    # Lee las IPs desde el archivo generado por el escaneo ARP
    with open("arp_hosts.txt") as archivo:
        hosts = [line.split(",")[0] for line in archivo]

    # Define los puertos a escanear
    puertos = [22, 80, 443]
    resultados = []

    print("Iniciando escaneo SYN de puertos…")
    
    for ip in hosts:
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

