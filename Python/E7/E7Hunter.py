from pyhunter import PyHunter as pyhunter
from openpyxl import Workbook as workbook
import getpass


def busqueda(organizacion):
    resultado = hunter.domain_search(
        company=organizacion, limit=1, emails_type='personal')
    return resultado


def guardar_informacion(datos_encontrados, organizacion):
    libro = workbook()
    hoja = libro.create_sheet(organizacion)
    libro.save("Hunter" + organizacion + ".xlsx")
    celda = hoja["A1"]
    hoja["A1"] = "Email"
    hoja["A2"] = info
    print ("Contenido de A1:", celda.value)
    hoja["B1"] = "Nombre"
    hoja["B2"] = nombre
    hoja["C1"] = "Pais"
    hoja["C2"] = country
    # agrega el codigo necesario para guardar en formato tabla
    # dentro del libro de Excel, información que consideres relevante
    # de lo obtenido en la búsqueda.
    libro.save("Hunter" + organizacion + ".xlsx")


print("Script para buscar información")
apikey = getpass.getpass("Ingresa tu API key: ")
hunter = pyhunter(apikey)
orga = input("Dominio a investigar: ")
datos_encontrados = busqueda(orga)
if datos_encontrados is None:
    exit()
else:
    print(datos_encontrados)
    info = (datos_encontrados['emails'][0]['value'])
    nombre = (datos_encontrados['emails'][0]['first_name'])
    country = (datos_encontrados["country"])
    guardar_informacion(datos_encontrados, orga)


# Integrantes:
# ANDREA PAOLA ARZATE RODRIGUEZ
# ANGELA MONTOYA ALDAPE
# ESTEBAN OSORIO RODRIGUEZ
# LUIS JULIAN RAMOS CASTAÑEDA
