from Logic.scraper import Scrapper
from Logic.visualizer import Visualizer
#from pprint import pprint as pp

#Etiquetas para la busqueda
carrers = [ "desarrollador web", 
            "desarrollador frontend", 
            "desarrollador backend", 
            "desarrollador de software", 
            "programador", 
            "desarrollador", 
            "programador junior",
            "python",
            "javascript",
            "sql",
            "java"
            ]

#Url de la empresa que vamos a utilizar
basic_url = "https://www.computrabajo.com.co/trabajo-de-"

#Creacion del Scrapper y llenado de datos
ws = Scrapper(basic_url)
ws.scan_url(carrers[0].replace(" ", "-"))
data = ws.get_companies()
#pp(data)

#Creacion de las graficas
vs = Visualizer()
vs.set_AxisData(data)
vs.get_BarChart()


    

