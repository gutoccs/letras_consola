from Letra import Letra
from Modelo import Modelo

class Menu:
    """
    Clase que gestiona el menú de la aplicación
    """

    letra = Letra()
    modelo = Modelo()

    def menu(self):
        """
        Muestra el menú de la aplicación
        """
        
        while True:
            
            try:
                opcion = int(input("""
            Menú de Letras Cónsola

            1. Ingresar frase a Imprimir
            2. Imprimir todo el abecedario
            3. Mostrar las frases impresas
            4. Exportar las frases impresas en un archivo plano
            5. Exportar las frases impresas en un archivo binario
            6. Salir
            
            Opción: """))
                if opcion == 1:
                    self.opcion_1()
                elif opcion == 2:
                    self.opcion_2()
                elif opcion == 3:
                    self.opcion_3()
                elif opcion == 4:
                    self.opcion_4()
                elif opcion == 5:
                    self.opcion_5()
                elif opcion == 6:
                    print("\n¡Hasta luego!")
                    break
                else:
                    print("\nOpción Inválida\n")
            except ValueError:
                print("\nLa opción no es un número\nIntente nuevamente\n")


    def opcion_1(self):
        """
        Opción que recoge los datos para imprimir en pantalla
        """

        frase = input("\nIngrese la frase a imprimir: ")
        caracter = input("Ingrese el caracter que desea que se muestre: ")
        print("")
        
        self.letra.impresion_frase(frase, caracter)


    def opcion_2(self):
        """
        Opción que manda a imprimir todo el abecedario
        """
        self.letra.impresion_abecedario()

    
    def opcion_3(self):
        """
        Opción que muestra por pantalla las frases impresas en el sistema
        """
        self.modelo.imprimir_frases_guardadas()


    def opcion_4(self):
        """
        Opción que permite exportar las frases impresas en el proyecto en un archivo plano (.txt)
        """
        self.modelo.guardar_frases_archivo_plano()


    def opcion_5(self):
        """
        Opción que permite exportar las frases impresas en el proyecto en un archivo binario (.pckl)
        """        
        self.modelo.guardar_frases_archivo_binario()
