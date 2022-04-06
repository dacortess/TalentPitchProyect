import matplotlib.pyplot as plt

class Visualizer:
    def __init__(self):
        self.x_axis = None
        self.y_axis = None
    
    def set_AxisData(self, info: dict) -> None:
        """
        Toma un diccionario con datos y lo separa en dos listas
        organizadas para no perder la relacion clave-valor. Solo 
        cuenta empresas con 2 o mas vacantes.

            Parametros:
                info : Diccionario con la información.
            
            Returns:
                None
        """
        x_axis, y_axis = list(), list()
        for key in info:
            if info[key]>1:
                x_axis.append(key)
                y_axis.append(info[key])
        self.x_axis = x_axis
        self.y_axis = y_axis

    def get_BarChart(self, a:int, b:int) -> None:
        """
        Crea una grafica de barras horizontal de la informacion
        guardada actualmente en un intervalo dado

            Parametros:
                a : Inicio del intervalo
                b : Fin del intervalo
            
            Returns:
                None
        """
        plt.barh(self.x_axis, self.y_axis, color="red")
        plt.xlabel('Cantidad de vacantes')
        plt.ylabel('Compañias')
        plt.xlim(a,b)
        plt.title('Compañias con mas vacantes')
        plt.show()
