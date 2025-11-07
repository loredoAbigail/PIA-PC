
# MENÚ
print("-------BIENVENIDO A LOGINSENTINEL-------.\nEste es un proyecto enfocado en la detección de intentos de autenticación \
y el monitoreo de servicios esenciales en una red (SSH, HTTP y HTTPS).\nSu objetivo es identificar accesos potencialmente no autorizados, \
analizar comportamientos sospechosos y generar reportes automatizados \nque apoyen la toma de decisiones en entornos de ciberseguridad.\n\
\n\t1- Descubrimiento de hosts y detección de puertos abiertos\n\t2- Análisis de intentos de autenticación\n\t3- Generación de reportes y resumen inteligente\n")


while True:
    try:
        tipo = int(input("Introduce el número correspondiente según tu opción:"))

        if 1 <= tipo <= 3:

            if tipo == 1:
                opcion_1()

            elif tipo == 2:
                print("opción 2")

            elif tipo == 3:
                print("opción 3")
            
            break

        else:
            print("Por favor ingresa un número del 1-3.")
    except ValueError:
        print("\nTiene que ingresar un número del 1-3.")