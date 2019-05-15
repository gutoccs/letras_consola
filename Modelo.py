import sqlite3
import datetime
from os import path, makedirs
import io
import pickle


class Modelo:
    """
    Clase que gestiona la conexión de la Base de Datos 
    """

    def __init__(self):
        """
        Constructor de la clase, crea la estructura de la BD, es decir, la tabla frase_impresa
        """
        cursor, conexion = self.abrir_conexion()
        cursor.execute("""CREATE TABLE IF NOT EXISTS frase_impresa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            frase VARCHAR(30),
            caracter VARCHAR(1),
            fecha_completa DATETIME)""")
        self.cerrar_conexion(conexion)


    def abrir_conexion(self):
        """
        Método que abre la conexión con la Base de Datos
        """
        #Si la carpeta BD no existe la crea
        if not path.exists("./BD"):
            makedirs("./BD")

        #Si la BD no existe la crea
        conexion = sqlite3.connect("./BD/letras_consola.db")    
        cursor = conexion.cursor()

        return cursor, conexion


    def cerrar_conexion(self, conexion):
        """
        Método que cierra la conexión con la Base de Datos
        """
        conexion.commit()
        conexion.close()


    def guardar_frase(self, frase, caracter):
        """
        Método que guarda la frase y el caracter en la BD
        """
        cursor, conexion = self.abrir_conexion()
        fecha_completa = datetime.datetime.now()
        cursor.execute("INSERT INTO frase_impresa VALUES (null, '{}', '{}', '{}')".format(frase, caracter, fecha_completa))
        self.cerrar_conexion(conexion)


    def __obtener_frases_guardadas(self):
        """
        Devuelve una lista con las frases impresas, el caracter que se usó y la fecha de la misma
        """
        cursor, conexion = self.abrir_conexion()

        frases = cursor.execute("SELECT * FROM frase_impresa").fetchall()
        
        self.cerrar_conexion(conexion)

        return frases


    def imprimir_frases_guardadas(self):
        """
        Imprime la lista de las frases impresas, el caracter que se usó y la fecha de la misma
        """
        frases = self.__obtener_frases_guardadas()

        if len(frases) > 0:
            print("")
            for frase in frases:
                formato_datetime = "%Y-%m-%d %H:%M:%S.%f"
                aux_fecha = datetime.datetime.strptime(frase[3], formato_datetime)
                formato_fecha = "%H:%M %d-%m-%Y"
                print("ID: {id} \t- Frase: {frase}\t- -\t Caracter: {caracter}\t- Fecha: {aux_fecha}\n".format(id = frase[0], frase = frase[1], caracter = frase[2], aux_fecha = aux_fecha.strftime(formato_fecha)))
        else:
            print("\nNo hay frases que mostrar\n")

        input("\nSe ha impreso lo solicitado, presione Enter para continuar ")


    def guardar_frases_archivo_plano(self):
        """
        Genera un archivo plano .txt de salida que contiene todas las frases impresas, el caracter que se usó y la fecha de la misma
        """
        #Creo la carpeta que contendrá el archivo de salida
        if not path.exists("./archivos_salida"):
            makedirs("./archivos_salida")

        texto_salida = ""
        frases = self.__obtener_frases_guardadas()        

        if len(frases) > 0:
            for frase in frases:
                formato_datetime = "%Y-%m-%d %H:%M:%S.%f"
                aux_fecha = datetime.datetime.strptime(frase[3], formato_datetime)
                formato_fecha = "%H:%M %d-%m-%Y"
                texto_salida += "ID: {id} \t- Frase: {frase}\t- -\t Caracter: {caracter}\t- Fecha: {aux_fecha}\n".format(id = frase[0], frase = frase[1], caracter = frase[2], aux_fecha = aux_fecha.strftime(formato_fecha))
        else:
            texto_salida = "No hay frases que mostrar"

        #Utilizo el modo 'w', para que cuando se abra el archivo borre todo su contenido
        archivo = open('./archivos_salida/frases.txt','w')
        archivo.write(texto_salida)
        archivo.close()

        input("\nSe han guardado las frases impresas en archivos_salida/frases.txt\nPresione Enter para continuar ")


    def guardar_frases_archivo_binario(self):
        """
        Genera un archivo binario .pckl de salida que contiene todas las frases impresas, el caracter que se usó y la fecha de la misma
        """
        #Creo la carpeta que contendrá el archivo de salida
        if not path.exists("./archivos_salida"):
            makedirs("./archivos_salida")

        texto_salida = []
        frases = self.__obtener_frases_guardadas()        

        if len(frases) > 0:
            for frase in frases:
                formato_datetime = "%Y-%m-%d %H:%M:%S.%f"
                aux_fecha = datetime.datetime.strptime(frase[3], formato_datetime)
                formato_fecha = "%H:%M %d-%m-%Y"
                texto_salida.append("ID: {id} \t- Frase: {frase}\t- -\t Caracter: {caracter}\t- Fecha: {aux_fecha}\n".format(id = frase[0], frase = frase[1], caracter = frase[2], aux_fecha = aux_fecha.strftime(formato_fecha)))
        else:
            texto_salida.append("No hay frases que mostrar")

        archivo = open('./archivos_salida/frases.pckl','wb')
        pickle.dump(texto_salida, archivo)
        archivo.close()

        input("\nSe han guardado las frases impresas en archivos_salida/frases.pckl\nPresione Enter para continuar ")
