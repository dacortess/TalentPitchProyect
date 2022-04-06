from bs4 import BeautifulSoup
from urllib.request import urlopen

class Scrapper:
    def __init__(self, main_url: str):
        self.main_url = main_url
        self.soup = None
        self.companies = dict()

    def scan_url(self, tag:str) -> None:
        """
        Recibe el nombre de un empleo y busca las empresas que aparecen
        en las primeras 10 paginas con vacantes disponibles.

            Parametros:
                tag : Nombre del empleo a buscar.
            
            Returns:
                None
        """
        for i in range(10):
            page = urlopen(self.main_url + tag + "?p=" + str(i+1))
            html = page.read().decode("utf-8") #HTML page as a string
            soup = BeautifulSoup(html, "html.parser") # bs4 object
            self.soup = soup
            self.upload_companies()
        
    def upload_companies(self) -> None:
        """
        Usa el objeto BeautufulSoup creado en base a un HTML para extraer
        los nombres de la compañias y almacenarlos en un diccionario
        segun la frecuencia con la que aparecen. 

            Parametros:
                None.
            
            Returns:
                None
        """
        jobs = self.soup.find_all('article', 
                                {'class':'box_border hover dFlex vm_fx mbB cp bClick mB_neg_m mb0_m'})

        for job in jobs:
            to_clean = str(job.find('a', {'class': 'fc_base hover it-blank'}))
            if to_clean != "None":
                company = to_clean.split(">")[1].split("<")[0].lower()
                company = self.clean_name(company)
                if not company in self.companies:
                    self.companies[company] = 1
                else:
                    self.companies[company] += 1
    
    def get_companies(self) -> dict:
        """
        Retorna el diccionario con la informacion de las compañias

            Parametros:
                None
            
            Returns:
                None
        """
        return self.companies
    
    def clean_name(self, name:str):
        """
        Toma el nombre de una empresa y elimina su tipo de sociedad.

            Parametros:
                name : nombre de la empresa a limpiar
            
            Returns:
                name : nombre de la empresa limpio
        """
        if name[-2:] == "sa":
            name = name[:-2]
        elif name[-3:] == "sas" or name[-3:] == "s.a":
            name = name[:-3]
        elif name[-4:] == "s.a.":
            name = name[:-4]
        elif name[-5:] == "s.a.s":
            name = name[:-5]
        elif name[-6:] == "s.a.s.":
            name = name[:-6]
        return name
        
        

    


