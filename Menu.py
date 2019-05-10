from Letra import Letra

class Menu:
    """
    Clase que gestiona el menú de la aplicación
    """

    letra = Letra()

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
            3. Salir
            
            Opción: """))
                if opcion == 1:
                    self.opcion_1()
                elif opcion == 2:
                    self.opcion_2()
                elif opcion == 3:
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
