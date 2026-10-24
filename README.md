# 🔐 Cifrado César en Python

Pequeña aplicación de escritorio desarrollada en **Python** con **PyQt6** que permite **encriptar y desencriptar mensajes** utilizando el clásico **cifrado César**.

> ⚠️ **Estado del proyecto:** Versión inicial (v0.1). Actualmente el cifrado funciona con un desplazamiento numérico fijo. Próximamente se añadirá soporte para **claves personalizadas**.

---

## ✨ Características actuales

- Interfaz gráfica intuitiva con PyQt6.
- Encriptación y desencriptación de texto mediante el cifrado César.
- Código modular y fácil de extender.

---

## 🧠 ¿Qué es el cifrado César?

Es una técnica de cifrado por sustitución en la que cada letra del texto original se reemplaza por otra que se encuentra un número fijo de posiciones más adelante en el alfabeto. Por ejemplo, con un desplazamiento de 3:

- `A` → `D`
- `B` → `E`
- `C` → `F`

> El texto `HOLA` se convertiría en `KROD`.

---

## 🛠️ Requisitos

- Python 3.9 o superior
- PyQt6

---

## 🚀 Instalación y uso

1. **Clona este repositorio:**
   ```bash
   git clone https://github.com/TU_USUARIO/Criptografia_Cesar.git
   cd Criptografia_Cesar
   ```

2. **(Recomendado) Crea y activa un entorno virtual:**
   ```bash
   python -m venv venv
   
   # Windows:
   venv\Scripts\activate
   
   # Linux / macOS:
   source venv/bin/activate
   ```

3. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecuta la aplicación:**
   ```bash
   python main.py
   ```

---

## 📁 Estructura del proyecto

```text
Criptografia_Cesar/
├── assets/                 # Recursos (íconos, imágenes)
├── src/
│   └── cifradoCesar.py     # Lógica del cifrado
├── ui/
│   ├── __init__.py
│   ├── main.ui             # Diseño de la interfaz (Qt Designer)
│   └── mainWindows.py      # Controlador de la ventana
├── utils/
│   └── rutas.py            # Utilidades de rutas
├── main.py                 # Punto de entrada
├── requirements.txt
└── README.md
```

---

## 🤝 Contribuciones

Este es un proyecto personal en desarrollo. Si tienes sugerencias o ideas, ¡eres bienvenido a abrir un issue o dejar un comentario!

---

## 👤 Autor

**Tu Nombre**
- GitHub: [@MartinSoftware](https://github.com/MartinSoftware)

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.