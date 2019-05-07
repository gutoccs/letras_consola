class Letra:
    """
    Clase que contiene el formato de cada letra de tamaño 5*5
    """

    #[[, , , , ], [, , , , ], [, , , , ], [, , , , ], [, , , , ]]
    abecedario = {} #Declarando el diccionario
    

    def __init__(self):
        #Inicializando el tipo de línea
        lineas = {}
        lineas["tipo_1"] = [1, 1, 1, 1, 1]
        lineas["tipo_2"] = [1, 1, 1, 1, 0]
        lineas["tipo_3"] = [1, 0, 0, 0, 1]
        lineas["tipo_4"] = [1, 0, 0, 0, 0]
        lineas["tipo_5"] = [0, 0, 1, 0, 0]
        lineas["tipo_6"] = [0, 0, 0, 1, 0]
        lineas["tipo_7"] = [1, 0, 0, 1, 0]
        lineas["tipo_8"] = [0, 1, 1, 1, 0]
        lineas["tipo_9"] = [0, 0]
        lineas["tipo_10"] = [1, 1, 0, 0, 0]
        lineas["tipo_11"] = [1, 1, 0, 1, 1]
        lineas["tipo_12"] = [1, 0, 1, 0, 1]
        lineas["tipo_13"] = [1, 1, 0, 0, 1]
        lineas["tipo_14"] = [1, 0, 0, 1, 1]
        lineas["tipo_15"] = [0, 0, 1, 1, 1]
        lineas["tipo_16"] = [1, 0, 1, 0, 0]
        lineas["tipo_17"] = [0, 0, 0, 0, 1]
        lineas["tipo_18"] = [0, 1, 0, 1, 0]
        lineas["tipo_19"] = [0, 1,  0, 1, 0]
        lineas["tipo_20"] = [0, 1,  0, 0, 0]
        
        


        #Inicializando el diccionario con el abecedario
        self.abecedario["A"] = [lineas["tipo_1"], lineas["tipo_3"], lineas["tipo_1"], lineas["tipo_3"], lineas["tipo_3"]]
        self.abecedario["B"] = [lineas["tipo_2"], lineas["tipo_3"], lineas["tipo_1"], lineas["tipo_3"], lineas["tipo_2"]]
        self.abecedario["C"] = [lineas["tipo_1"], lineas["tipo_4"], lineas["tipo_4"], lineas["tipo_4"], lineas["tipo_1"]]
        self.abecedario["D"] = [lineas["tipo_2"], lineas["tipo_3"], lineas["tipo_3"], lineas["tipo_3"], lineas["tipo_2"]]
        self.abecedario["E"] = [lineas["tipo_1"], lineas["tipo_4"], lineas["tipo_1"], lineas["tipo_4"], lineas["tipo_1"]]
        self.abecedario["F"] = [lineas["tipo_1"], lineas["tipo_4"], lineas["tipo_1"], lineas["tipo_4"], lineas["tipo_4"]]
        self.abecedario["G"] = [lineas["tipo_1"], lineas["tipo_4"], lineas["tipo_1"], lineas["tipo_3"], lineas["tipo_1"]]
        self.abecedario["H"] = [lineas["tipo_3"], lineas["tipo_3"], lineas["tipo_1"], lineas["tipo_3"], lineas["tipo_3"]]
        self.abecedario["I"] = [lineas["tipo_1"], lineas["tipo_5"], lineas["tipo_5"], lineas["tipo_5"], lineas["tipo_1"]]
        self.abecedario["J"] = [lineas["tipo_1"], lineas["tipo_6"], lineas["tipo_7"], lineas["tipo_7"], lineas["tipo_8"]]
        self.abecedario["K"] = [lineas["tipo_3"], lineas["tipo_7"], lineas["tipo_10"], lineas["tipo_7"], lineas["tipo_3"]]
        self.abecedario["L"] = [lineas["tipo_4"], lineas["tipo_4"], lineas["tipo_4"], lineas["tipo_4"], lineas["tipo_1"]]
        self.abecedario["M"] = [lineas["tipo_3"], lineas["tipo_11"], lineas["tipo_12"], lineas["tipo_3"], lineas["tipo_3"]]
        self.abecedario["N"] = [lineas["tipo_3"], lineas["tipo_13"], lineas["tipo_12"], lineas["tipo_14"], lineas["tipo_3"]]
        self.abecedario["Ñ"] = [lineas["tipo_1"], lineas["tipo_13"], lineas["tipo_12"], lineas["tipo_14"], lineas["tipo_3"]]
        self.abecedario["O"] = [lineas["tipo_8"], lineas["tipo_3"], lineas["tipo_3"], lineas["tipo_3"], lineas["tipo_8"]]
        self.abecedario["P"] = [lineas["tipo_2"], lineas["tipo_3"], lineas["tipo_1"], lineas["tipo_4"], lineas["tipo_4"]]
        self.abecedario["Q"] = [lineas["tipo_8"], lineas["tipo_3"], lineas["tipo_3"], lineas["tipo_8"], lineas["tipo_15"]]
        self.abecedario["R"] = [lineas["tipo_2"], lineas["tipo_3"], lineas["tipo_1"], lineas["tipo_16"], lineas["tipo_3"]]
        self.abecedario["S"] = [lineas["tipo_1"], lineas["tipo_4"], lineas["tipo_1"], lineas["tipo_17"], lineas["tipo_1"]]
        self.abecedario["T"] = [lineas["tipo_1"], lineas["tipo_5"], lineas["tipo_5"], lineas["tipo_5"], lineas["tipo_5"]]
        self.abecedario["U"] = [lineas["tipo_3"], lineas["tipo_3"], lineas["tipo_3"], lineas["tipo_3"], lineas["tipo_8"]]
        self.abecedario["V"] = [lineas["tipo_3"], lineas["tipo_3"], lineas["tipo_3"], lineas["tipo_18"], lineas["tipo_5"]]
        self.abecedario["W"] = [lineas["tipo_3"], lineas["tipo_3"], lineas["tipo_12"], lineas["tipo_11"], lineas["tipo_3"]]
        self.abecedario["X"] = [lineas["tipo_3"], lineas["tipo_19"], lineas["tipo_5"], lineas["tipo_19"], lineas["tipo_3"]]
        self.abecedario["Y"] = [lineas["tipo_3"], lineas["tipo_19"], lineas["tipo_5"], lineas["tipo_5"], lineas["tipo_5"]]
        self.abecedario["Z"] = [lineas["tipo_1"], lineas["tipo_6"], lineas["tipo_5"], lineas["tipo_20"], lineas["tipo_1"]]
        self.abecedario[" "] = [lineas["tipo_9"], lineas["tipo_9"], lineas["tipo_9"], lineas["tipo_9"], lineas["tipo_9"]]

    def impresion_frase(self, frase, caracter):
        """
        Imprime por cónsola la frase y/o palabra que haya recibido.
        """
        
        retorno, frase, mensaje = self.__validar_frase(frase)
        
        if retorno == False:
            print("\n{}\n".format(mensaje))
            return

        frase = frase
             
        impresion = []
        for letra in frase:
            impresion.append(self.abecedario[letra])
        
        for linea in range(5):
            for letra in range(len(impresion)):
                for iter in range(len(impresion[letra][linea])):
                    if impresion[letra][linea][iter] == True:
                        print(caracter, end="")
                    else:
                        print(" ", end="")
                print("  ", end="")
            print("")
        
        self.mensaje_final()


    def __validar_frase(self, frase):
        """
        Valida la frase antes de la impresión
        """

        frase = str(frase)

        if not frase.replace(" ", "").isalpha():
            return False, frase, "La frase contiene algún caracter no alfabético"

        if len(frase) > 24:
            return False, frase, "La frase excede los 24 caracteres"

        frase = frase.upper()

        return True, frase, ""

                          
    def impresion_abecedario(self):
        """
        Imprime todas las letras del abecedario
        """

        print("\nImpresión del Abecedario, caracter por defecto *")

        for letra, matriz in self.abecedario.items():
            if letra == "A":
                print("")
            else:
                print("\n")

            print("Letra {}:\n".format(letra))

            for arr in matriz:
                for aux in arr:
                    if aux == True:
                        print("*", end="") 
                    else:
                        print(" ", end="")
                print("")

        self.mensaje_final()

    def mensaje_final(self):
        """
        Imprime el mensaje y solicita un enter para continuar
        """
        input("\nSe ha impreso lo solicitado, presione Enter para continuar ")

