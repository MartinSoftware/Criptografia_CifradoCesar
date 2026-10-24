# utils/rutas.py
import os
import sys

def ruta_base() -> str:
    """Retorna la ruta base correcta tanto en desarrollo como en el .exe"""
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def ruta(relativa: str) -> str:
    """Construye una ruta absoluta desde la raíz del proyecto."""
    return os.path.normpath(os.path.join(ruta_base(), relativa))