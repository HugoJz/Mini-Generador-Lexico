#Jiménez Estrada Hugo Armando
#22 / Enero / 2023 

import re

identificador = re.compile('[a-zA-Z]+([a-zA-Z]+[\d])*')

real = re.compile('[\d]+\.[\d]+')

entero = re.compile('[\d]')

linea = []

while (linea != '0'):
        linea = input("Cadena a analizar: ")
        tokens=linea.split(' ')
        print("Los tokens son ", tokens)
        
        for token in tokens:     
            if identificador.match(linea):
                print (token, "<< es un identificador del tipo: 0")
            elif real.match(linea):
                print (token, "<< es un real del tipo: 2")
            elif entero.match(linea):
                print(token, "<< es un identificador del tipo: 1") 
                
            
        print("----------------------------------------------------------")