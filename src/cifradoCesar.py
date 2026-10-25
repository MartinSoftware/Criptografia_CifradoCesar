import string

ABECEDARIO_EN = list(string.ascii_uppercase)
ABECEDARIO_ES = list(string.ascii_uppercase)
ABECEDARIO_ES.insert(14, 'Ñ')
class CifradoCesar():
    def __init__(self):
        super().__init__()
    
    def encriptar(self, mensajeIngresado, numDesplazamiento, alfabeto, clave = None):
        if alfabeto == 0:
            abecedario_actual = ABECEDARIO_ES
            maximo = 27
        elif alfabeto == 1:
            abecedario_actual = ABECEDARIO_EN
            maximo = 26
        
        mensajesSeparados = self._separarMensaje(mensajeIngresado)
        resultadoPre = [None] * len(mensajesSeparados)
        posicion = 0
        
        if clave is None or str(clave).strip() == "":
            for i in range(len(mensajesSeparados)):
                posicion = self._busqueda(mensajesSeparados[i], abecedario_actual)
                nueva_posicion = (posicion + numDesplazamiento)%maximo

                resultadoPre[i] = abecedario_actual[nueva_posicion]
        else:
            #desplazamiento = numDesplazamiento*-1
            lista = self._nuevaListaConClave(numDesplazamiento, abecedario_actual,clave)
            resultadoPre = self._encriptadoConClave(mensajesSeparados,abecedario_actual,lista)

            if(numDesplazamiento < 0):
                lista = self._nuevaListaConClave(numDesplazamiento*-1, abecedario_actual,clave)
                resultadoPre = self._encriptadoConClave(mensajesSeparados,abecedario_actual,lista)

                resultado = [None] * len(mensajesSeparados)
                resultado = self._desencriptadoConClave(lista,mensajesSeparados,abecedario_actual)
                resultadoPre = resultado
            else:
                pass
            
        return self._formatear_encriptado(mensajesSeparados, resultadoPre)
    
    def _nuevaListaConClave(self,numDesplazamiento, alfabeto, clave):
        claveFormateada = list(dict.fromkeys(self._separarMensaje(clave)))
        arregloInicial = list(dict.fromkeys([caracter for caracter in (claveFormateada + alfabeto) if caracter != " "]))
        
        arregloFinal = arregloInicial[-numDesplazamiento:] + arregloInicial[:-numDesplazamiento]
        
        return arregloFinal
    
    def _encriptadoConClave(self,mensaje,alfabeto,lista):
        #_resultadoPre = [None] * len(lista)
        _resultadoPre = [None] * len(mensaje)
        for i in range(len(mensaje)):
            posicionEncontrada = self._busqueda(mensaje[i],alfabeto)
            if(mensaje[i]== " "):
                _resultadoPre[i] = " "
            else:
                _resultadoPre[i]  = lista[posicionEncontrada]
        return _resultadoPre
        
    def _desencriptadoConClave(self,claveArray,mensajeArray,abecedario):
        resultadoPre = []
        resultadoPre = [None] * len(mensajeArray)
        for i in range(len(mensajeArray)):
            posicionEncontrada = self._busqueda(mensajeArray[i],claveArray)
            if(mensajeArray[i]== " "):
                resultadoPre[i] = " "
            else:
                resultadoPre[i]  = abecedario[posicionEncontrada]
        return resultadoPre
        
    def _separarMensaje(self, texto):
        return list(texto.upper())
    
    def _busqueda(self, letra, abecedario_actual):
        posicion = 0
        for i in range(len(abecedario_actual)):
            if letra == abecedario_actual[i]:
                posicion = i
        return posicion

    def _formatear_encriptado(self, texto_inicial, texto_encriptado):
        texto_final = []
        for letra_i, letra_e in zip(texto_inicial, texto_encriptado):
            if letra_i != " ":
                texto_final.append(letra_e)
            else:
                texto_final.append(" ")
                
        return "".join(texto_final)

