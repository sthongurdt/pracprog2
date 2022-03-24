# PIP es un manejador de paquetes y modulos para python, para checkear si esta instalado y su version escriba en la terminaL:
#   pip --version

# descargar paquetes es simple, identifique el paquete que desea descargar, navege al directorio script de python (en windows), en linux desde la terminal escriba:
#   pip install <paquete>
#   pip install camelcase

# para usar el paquete solo importelo
import camelcase

c = camelcase.CamelCase()

t = 'hola mundo'
print(c.hump(t))

# si desea desinstalar un paquete use:
#   pip uninstall <paquete>
#   pip uninstall camelcase

# si desea saber que paquetes tiene instalados use:
#   pip list