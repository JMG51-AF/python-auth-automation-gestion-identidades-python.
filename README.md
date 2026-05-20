# python-auth-automation-gestion-identidades-python.
Algoritmo en Python para la actualización automatizada de listas de acceso (allow_list) mediante la eliminación de IPs no autorizadas

Automatización de Control de Accesos mediante Python

Descripción del Proyecto

En el ámbito de la ciberseguridad, la gestión de identidades y accesos (IAM) es fundamental para proteger la infraestructura. Este proyecto consiste en un algoritmo desarrollado en Python diseñado para mantener actualizada la lista de direcciones IP permitidas (allow_list.txt) para el acceso a contenidos protegidos.

El script automatiza la identificación y remoción de direcciones IP que han perdido sus privilegios de acceso, basándose en una lista de eliminación predefinida, garantizando así que solo el personal autorizado mantenga conectividad activa.

🛠️ Tecnologías y Conceptos Aplicados

Lenguaje: Python (Desarrollado en entorno Jupyter Notebook).

Conceptos de Seguridad: Principio de Mínimo Privilegio (PoLP), Gestión de Accesos, Automatización de Seguridad (SecOps).

Manejo de Datos: Manipulación de archivos (.txt), estructuras de listas, bucles iterativos y lógica condicional.

🚀 Análisis del Algoritmo

El proceso se divide en las siguientes etapas técnicas:

Acceso al Repositorio de Datos: Se utiliza la instrucción with junto con open() en modo lectura ("r") para acceder al archivo allow_list.txt. Este enfoque garantiza una gestión eficiente de los recursos del sistema al cerrar el archivo automáticamente.

Procesamiento de Información:
Se emplea el método .read() para convertir el contenido del archivo en una cadena de texto, la cual es posteriormente transformada en una lista mediante .split(). Esta conversión es crítica para permitir la manipulación individual de cada dirección IP.

Lógica de Eliminación (Iteración y Condicionales):
Se implementa un bucle for para recorrer la lista de eliminación (remove_list). Dentro de cada iteración, una sentencia if verifica la existencia de la IP antes de aplicar el método .remove(), evitando errores de ejecución y asegurando la integridad del proceso.

Actualización del Sistema:
Finalmente, la lista revisada se convierte nuevamente en una cadena de texto utilizando .join() con el separador de nueva línea (\n). Los datos actualizados se escriben en el archivo original mediante el modo escritura ("w"), reemplazando la información obsoleta con el nuevo estado de seguridad.

📁 Estructura del Repositorio

control_acceso.py: Script principal con el algoritmo de automatización.

allow_list.txt: Archivo de texto que actúa como base de datos de IPs autorizadas.

README.md: Documentación técnica del proyecto.

📈 Relevancia para el Perfil GRC

Este proyecto demuestra la capacidad de traducir políticas de seguridad (quién debe tener acceso) en controles técnicos automatizados. Es una prueba tangible de habilidades en la optimización de procesos administrativos orientados al cumplimiento normativo y la reducción de la superficie de ataque institucional.
