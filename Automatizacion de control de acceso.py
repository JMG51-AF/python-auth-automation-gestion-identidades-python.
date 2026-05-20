# Configuración del repositorio de identidades (Lista de acceso autorizado)
import_file = "allow_list.txt"

# Lista de exclusión: IPs identificadas para revocación inmediata de accesos
remove_list = ["192.168.X.X", "10.0.X.X"]

# Apertura segura del archivo para lectura de credenciales activas
with open(import_file, "r") as file:
    # Extracción de la base de datos de IPs autorizadas
    ip_addresses = file.read()

# Tokenización del contenido para permitir la evaluación individual de cada IP
ip_addresses = ip_addresses.split()

# Proceso automatizado de depuración de privilegios
# Se evalúa cada IP de la lista de exclusión para aplicar el Principio de Mínimo Privilegio
for element in remove_list:

    # Control de validación: Se verifica la existencia de la IP antes de operar
    # Esto previene errores de ejecución (ValueErrors) y asegura la integridad del flujo
    if element in ip_addresses:

        # Revocación efectiva del acceso: Eliminación de la IP no autorizada
        ip_addresses.remove(element)

# Reestructuración del formato de datos para su almacenamiento persistente
ip_addresses = "\n".join(ip_addresses)

# Apertura del archivo en modo escritura para aplicar la nueva política de accesos
with open(import_file, "w") as file:
    # Actualización del control de acceso, guardando únicamente el estado seguro de la lista
    file.write(ip_addresses)

