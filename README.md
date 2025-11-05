# LoginSentinel – Detección y análisis de intentos de autenticación en servicios críticos


## Descripción general del proyecto

LoginSentinel es un proyecto enfocado en la detección de intentos de autenticación y el monitoreo de servicios esenciales en una red (SSH, HTTP y HTTPS).
Su objetivo es identificar accesos potencialmente no autorizados, analizar comportamientos sospechosos y generar reportes automatizados que apoyen la toma de decisiones en entornos de ciberseguridad.



---

## Etapas principales del proyecto

--El proyecto se desarrolla en tres etapas principales:

-Descubrimiento de hosts y detección de puertos abiertos (Tarea 1):
Escanea una lista de direcciones IP para determinar qué equipos están activos y si tienen habilitados los puertos 22, 80 y 443, que corresponden a servicios de autenticación y web comunes.

-Análisis de intentos de autenticación (Tarea 2):
Examina registros simulados de accesos exitosos y fallidos, detectando patrones anómalos como múltiples intentos fallidos desde la misma IP o comportamientos que puedan indicar ataques de fuerza bru[...]

-Generación de reportes y resumen inteligente (Tarea 3):
Compila los resultados de los análisis y crea un reporte automatizado, que incluye un resumen ejecutivo generado por IA, con observaciones y recomendaciones para fortalecer la seguridad de acceso.



---

## Asignación de roles del equipo

| Integrante | Rol o responsabilidad |
|------------|-----------------------|
| Cintia Lizeth Salazar Alcocer | Descubrimiento y escaneo de hosts + documentación del procedimiento.|
| Abigail Loredo Torres | Análisis de intentos de autenticación + genera findings.csv/json. |
| Juan Andrés Villarreal Cortez | Generación de reportes y resumen con IA + crea executive_summary.md y logs. |



---

## Declaración ética y legal

*Declaración ética y legal

Todo el trabajo se realiza en un entorno controlado y con datos sintéticos, asegurando el cumplimiento de principios éticos y legales en el manejo de información.
El proyecto busca fomentar buenas prácticas de ciberseguridad, especialmente en la detección temprana de intrusiones y la protección de sistemas de autenticación.ción temprana de intrusiones y la protección de sistemas de autenticación.
