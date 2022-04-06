from Logic.scraper import Scrapper
from Logic.visualizer import Visualizer
#from pprint import pprint as pp

#Etiquetas para la busqueda
carrers = [ "Desarrollador web", 
            "Desarrollador frontend", 
            "Desarrollador backend", 
            "Desarrollador de software"
            ]

#Url de la empresa que vamos a utilizar
basic_url = "https://www.computrabajo.com.co/trabajo-de-"

#Creacion del Scrapper y llenado de datos
ws = Scrapper(basic_url)
for tag in carrers:
    ws.scan_url(tag.replace(" ", "-"))

data = ws.get_companies()
#pp(data)
ids = ws.get_ids()
#pp(ids)

#Creacion de las graficas
vs = Visualizer()
vs.set_AxisData(data)
vs.get_BarChart()


    

