import string

ABECEDARIO_EN = list(string.ascii_uppercase)
ABECEDARIO_ES = list(string.ascii_uppercase)
ABECEDARIO_ES.insert(14, 'Ñ')

class CifradoCesar():
    
    def __init__(self):
        super().__init__()
    
    def encriptar(self, mensajeIngresado, numDesplazamiento, alfabeto):
        if alfabeto == 0:
            abecedario_actual = ABECEDARIO_ES
            maximo = 27
        elif alfabeto == 1:
            abecedario_actual = ABECEDARIO_EN
            maximo = 26
        
        mensajesSeparados = self._separarMensaje(mensajeIngresado)
        resultadoPre = [None] * len(mensajesSeparados)
        posicion = 0
        
        for i in range(len(mensajesSeparados)):
            posicion = self._busqueda(mensajesSeparados[i], abecedario_actual)
            nueva_posicion = posicion + numDesplazamiento
            
            if nueva_posicion >= maximo:
                nueva_posicion = nueva_posicion - maximo
            
            resultadoPre[i] = abecedario_actual[nueva_posicion]
        
        return self._formatear_encriptado(mensajesSeparados, resultadoPre)
        
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
