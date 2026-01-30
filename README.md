Meta PAES ejercicio

Meta PAES ejercicio es un sistema de gestión de postulaciones desarrollado en Python. Permite la administración de carreras académicas y el registro de postulantes, asegurando que los datos ingresados cumplan con formatos específicos mediante un módulo de validaciones robusto.

🚀 Características

Gestión de Carreras: Permite definir y organizar las diferentes ofertas académicas.


Registro de Postulantes: Almacenamiento y manejo de información de los estudiantes interesados.


Validaciones en Tiempo Real: Módulo especializado para verificar RUT, correos electrónicos y formatos de datos.


Interfaz de Consola Interactiva: Menú integrado para facilitar la navegación del usuario.


Control de Versiones: Proyecto configurado con Git para un seguimiento detallado de cambios.
+2

🛠️ Estructura del Proyecto
El proyecto se organiza de la siguiente manera:


Menu_App.py: El punto de entrada principal que maneja la lógica del menú y la interacción con el usuario.


Carrera.py: Define la clase y lógica relativa a las carreras ofrecidas.


Postulante.py: Define la clase y atributos de los postulantes.


Validaciones.py: Contiene funciones utilitarias para asegurar la integridad de los datos ingresados.


.idea/ & .git/: Archivos de configuración del entorno de desarrollo (PyCharm) y control de versiones.
+2

📋 Requisitos

Python 3.10 o superior (según las referencias a archivos compilados .pyc para versiones recientes).
+2

💻 Instalación y Uso
Clonar el repositorio:

Bash
git clone https://github.com/tu-usuario/meta-paes-ejercicio.git
cd "Meta PAES ejercicio"
Ejecutar la aplicación:

Bash
python Menu_App.py
⚙️ Detalles Técnicos
El sistema utiliza un enfoque de Programación Orientada a Objetos (POO) para separar las entidades (Carrera y Postulante) de la lógica de presentación (Menu) y los servicios de soporte (Validaciones).
