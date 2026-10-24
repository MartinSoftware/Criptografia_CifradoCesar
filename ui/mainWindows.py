from PyQt6 import uic
from PyQt6.QtWidgets import QButtonGroup, QMainWindow
from utils.rutas import ruta
from src.cifradoCesar import CifradoCesar

class ventanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(ruta("ui/main.ui"), self)
        self.setWindowTitle("Cifrado de César")
        self._conectar_botones()
        self.cifrador = CifradoCesar()

    def _conectar_botones(self):
        ventana = self.window()
        
        self._inputTEXT =ventana.findChild(object,"inputTEXT")
        self._cbox_tipoAlfabeto =ventana.findChild(object,"cbox_tipoAlfabeto")
        self._spinNumDesplazamiento =ventana.findChild(object,"spinNumDesplazamiento")
        self._radioDesencriptar = ventana.findChild(object, "radioDesencriptar")
        self._radioEncriptar = ventana.findChild(object, "radioEncriptar")
        self._resultText = ventana.findChild(object, "resultText")
        self._btnComenzar = ventana.findChild(object, "btnComenzar")
        self._btnBorrarTodo = ventana.findChild(object, "btnBorrarTodo")
        
        self._tipoCifrado = QButtonGroup(self)
        self._tipoCifrado.addButton(self._radioEncriptar,   1)
        self._tipoCifrado.addButton(self._radioDesencriptar, 2)
        #self._tipoCifrado.buttonClicked.connect(lambda: self._log("Boton Cambiado"))
        
        #print("botones sincronizados")
        
        self._btnComenzar.clicked.connect(self._procesarMensaje)
        self._btnBorrarTodo.clicked.connect(self._limpiarTodo)
        
        #self._inputTEXT.textChanged.connect(lambda: self._log(self._inputTEXT.toPlainText()))
    
    def _log(self, valor):
        print(f"{valor}")
        
    
    def _procesarMensaje(self):
        id_seleccionado = self._tipoCifrado.checkedId()
        modos = {1: "Encriptar", 2: "Desencriptar"}
        modo_actual = modos.get(id_seleccionado, "Ninguno")
        getNumDesplazamiento = self._spinNumDesplazamiento.value()
        getMensajeEntrada = self._inputTEXT.toPlainText()
        getTipoAlfabeto = self._cbox_tipoAlfabeto.currentIndex()
    
        """ print(modo_actual)
        print(str(getNumDesplazamiento))
        print(getMensajeEntrada)
        print(getTipoAlfabeto) """
        
        if modo_actual == "Encriptar":
            resultado_final = self.cifrador.encriptar(
                getMensajeEntrada,
                getNumDesplazamiento,
                getTipoAlfabeto
            )

        elif modo_actual == "Desencriptar":
            desplazamiento_final = -getNumDesplazamiento
            
            resultado_final = self.cifrador.encriptar(
                getMensajeEntrada,
                desplazamiento_final,
                getTipoAlfabeto
            )
        return self._resultText.setPlainText(resultado_final)
        
    def _limpiarTodo(self):
        self._inputTEXT.setPlainText("")
        self._resultText.setPlainText("")
        self._cbox_tipoAlfabeto.setCurrentIndex(0)
        self._spinNumDesplazamiento.setValue(0)
        
        
        
        
