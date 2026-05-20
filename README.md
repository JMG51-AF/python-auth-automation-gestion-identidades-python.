# 🔒 Automatización de Control de Accesos mediante Python

<p align="center">
  <img src="https://shields.io" alt="Python" />
  <img src="https://shields.io" alt="Jupyter" />
  <img src="https://shields.io🛡️-blue?style=for-the-badge" alt="SecOps" />
  <img src="https://shields.io🔑-green?style=for-the-badge" alt="IAM" />
</p>

Algoritmo en Python para la actualización automática de listas de acceso (`allow_list`) mediante la eliminación de IPs no autorizadas.

---

<h2 style="color: white; font-size: 26px;">📝 Descripción del Proyecto</h2>

En el ámbito de la ciberseguridad, la **Gestión de Identidades y Accesos (IAM)** es fundamental para proteger la infraestructura. Este proyecto consiste en un algoritmo desarrollado en Python diseñado para mantener actualizada la lista de direcciones IP permitidas (`allow_list.txt`) para el acceso a contenidos protegidos.

El script automatiza la identificación y remoción de direcciones IP que han perdido sus privilegios de acceso, basándose en una lista de eliminación predefinida, garantizando así que solo el personal autorizado mantenga la conectividad activa.

---

<h2 style="color: white; font-size: 26px;">🛠️ Tecnologías y Conceptos Aplicados</h2>

*   **Lenguaje:** Python (Desarrollado en entorno Jupyter Notebook).
*   **Conceptos de Seguridad:** Principio de Mínimo Privilegio (PoLP), Gestión de Accesos, Automatización de Seguridad (SecOps).
*   **Manejo de Datos:** Manipulación de archivos (`.txt`), estructuras de listas, bucles iterativos y lógica condicional.

---

<h2 style="color: white; font-size: 26px;">🚀 Análisis del Algoritmo</h2>

El proceso se divide en las siguientes etapas técnicas:

1. **Acceso al Repositorio de Datos**
   Se utiliza la instrucción `with` junto con `open()` en modo lectura (`"r"`) para acceder al archivo `allow_list.txt`. Este enfoque garantiza una gestión eficiente de los recursos del sistema al cerrar el archivo automáticamente.

2. **Procesamiento de Información**
   Se emplea el método `.read()` para convertir el contenido del archivo en una cadena de texto, la cual es posteriormente transformada en una lista mediante `.split()`. Esta conversión es crítica para permitir la manipulación individual de cada dirección IP.

3. **Lógica de Eliminación (Iteración y Condicionales)**
   Se implementa un bucle para recorrer la lista de eliminación (`remove_list`). Dentro de cada iteración, una sentencia `if` verifica la existencia de la IP antes de aplicar el método `.remove()`, evitando errores de ejecución y asegurando la integridad del proceso.

4. **Actualización del Sistema**
   Finalmente, la lista revisada se convierte nuevamente en una cadena de texto utilizando `.join()` con el separador de nueva línea (`\n`). Los datos actualizados se escriben en el archivo original mediante el modo escritura (`"w"`), reemplazando la información obsoleta con el nuevo estado de seguridad.

---

<h2 style="color: white; font-size: 26px;">📁 Estructura del Repositorio</h2>

```text
├── control_acceso.py    # Script principal con el algoritmo de automatización.
├── allow_list.txt      # Archivo de texto que actúa como base de datos de IP autorizadas.
└── README.md            # Documentación técnica del proyecto.
```

---

<h2 style="color: white; font-size: 26px;">📈 Relevancia para el Perfil GRC</h2>

Este proyecto demuestra la capacidad de **traducir políticas de seguridad** (quién debe tener acceso) en **controles técnicos automatizados**. Es una prueba tangible de habilidades en la optimización de procesos administrativos orientados al cumplimiento normativo y la reducción de la superficie de ataque institucional.

---

<h2 style="color: white; font-size: 26px;">📘 Contexto del Proyecto</h2>

Este proyecto se desarrolló en un entorno educativo y simulado, con el objetivo de aplicar conceptos de programación en Python a la gestión de listas de control de acceso (ACL). La solución implementada automatiza la actualización de direcciones IP autorizadas, contrastándolas con una lista de exclusión para revocar accesos no permitidos de forma inmediata.

Aunque se trata de un ejercicio académico, el enfoque está directamente relacionado con los principios de **Gestión de Identidad y Accesso (IAM)**, ya que aborda la administración de permisos, la revocación de accesos y la reducción del error humano mediante automatización. De esta manera, el proyecto no solo refuerza la seguridad sobre contenidos restringidos, sino que también ejemplifica cómo la programación puede integrarse en prácticas de gestión de identidades y control de accesos dentro de organizaciones modernas.

