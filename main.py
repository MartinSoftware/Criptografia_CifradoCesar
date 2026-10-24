import sys
from PyQt6.QtWidgets import QApplication
from ui.mainWindows import ventanaPrincipal


def main():
    app = QApplication(sys.argv)
    
    ventana = ventanaPrincipal()
    ventana.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()