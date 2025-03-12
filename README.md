# WildPassPro - Suite de Seguridad y Gestión de Contraseñas 🔐

---

## 📑 **Tabla de Contenidos**
1. [Nombre del Proyecto](#-nombre-del-proyecto)
2. [Descripción del Proyecto](#-descripción-del-proyecto)
3. [Arquitectura del Proyecto](#-arquitectura-del-proyecto)
4. [Proceso de Desarrollo](#-proceso-de-desarrollo)
   - Fuente del Dataset
   - Limpieza de Datos
   - Manejo de Excepciones y Control de Errores
   - Estadísticos y Gráficos
5. [Funcionalidades](#-funcionalidades)
6. [Estado del Proyecto](#-estado-del-proyecto)
7. [Tecnologías y Herramientas Usadas](#-tecnologías-y-herramientas-usadas)
8. [Conclusiones del Proyecto](#-conclusiones-del-proyecto)

---

## 🏷️ **Nombre del Proyecto**
**WildPassPro** - Suite de Seguridad y Gestión de Contraseñas.

---

## 📝 **Descripción del Proyecto**
WildPassPro es una aplicación innovadora diseñada para mejorar la seguridad de tus contraseñas, proteger tus datos y brindarte herramientas avanzadas para gestionar tus credenciales de manera inteligente. Con un enfoque en la usabilidad, la seguridad y la inteligencia artificial, WildPassPro es tu compañero ideal para navegar en el mundo digital de forma segura.

![WildPassPro Demo](https://github.com/AndersonP444/PROYECTO-IA-SIC-The-Wild-Project-Final/blob/main/wildpasspro.png)

---

## 🏗️ **Arquitectura del Proyecto**

### Diagrama de Arquitectura
![Arquitectura de WildPassPro](https://raw.githubusercontent.com/AndersonP444/PROYECTO-IA-SIC-The-Wild-Project/main/arquitectura_wildpasspro.png)

### Componentes Principales:
1. **Frontend**:
   - Interfaz de usuario construida con **Streamlit**.
   - Diseño moderno con **CSS personalizado**.

2. **Backend**:
   - Lógica de negocio en **Python**.
   - **Redes Neuronales** para evaluación de contraseñas.
   - **Groq API** para análisis avanzado con IA.

3. **Base de Datos**:
   - Almacenamiento seguro de contraseñas cifradas con **AES-256**.

4. **APIs Externas**:
   - **GitHub OAuth** para autenticación.
   - **Have I Been Pwned API** para verificación de fugas de datos.

---

## 🛠️ **Proceso de Desarrollo**

### 1. **Fuente del Dataset**
   - Utilizamos un dataset público de contraseñas para entrenar nuestros modelos.
   - Fuente: [Kaggle - Password Strength Dataset](https://www.kaggle.com/datasets/bhavikbb/password-strength-classifier-dataset).

### 2. **Limpieza de Datos**
   - Eliminación de contraseñas duplicadas.
   - Normalización de caracteres y formato.
   - División del dataset en entrenamiento y prueba.


### 3. **Manejo de Excepciones y Control de Errores**
   - Implementación de try-except para capturar errores en tiempo real.
   - Validación de entradas del usuario para evitar inyecciones de código.

### 4. **Estadísticos y Gráficos**
   - Gráficos de barras para mostrar la fortaleza de las contraseñas.
   - Métricas de precisión y recall para los modelos de IA.

![image](https://github.com/user-attachments/assets/724f57d2-8b8e-40ad-b26f-fc1a571f562e)
![image](https://github.com/user-attachments/assets/e399d5a4-1449-4b43-8455-218c67e67961)
![image](https://github.com/user-attachments/assets/cdcfc2cb-a989-49da-afa6-20a3bde1ad37)
![image](https://github.com/user-attachments/assets/361edd0c-3865-490b-8405-04b0b3cccb0c)
![image](https://github.com/user-attachments/assets/1af7fc57-e302-4b54-9b0c-7f74debf763d)
![image](https://github.com/user-attachments/assets/d7736a4c-c143-4e06-bc37-c71720c505bb)
![image](https://github.com/user-attachments/assets/be1c3ed6-435a-4ec8-9227-400585e51513)
![image](https://github.com/user-attachments/assets/14659804-3b39-48f5-b64c-b09205ae1885)


---

## 🎯 **Funcionalidades**

### 1. **Generador de Contraseñas Seguras**
   - Crea contraseñas robustas y únicas con un solo clic.

### 2. **Bóveda de Contraseñas Cifradas**
   - Almacena tus contraseñas de forma segura con cifrado AES-256.

### 3. **Analizador de Fortaleza de Contraseñas**
   - Evalúa la fortaleza de tus contraseñas en tiempo real.

### 4. **Asistente de Seguridad con IA (Groq API)**
   - Explicaciones detalladas generadas por IA.

### 5. **Redes Neuronales para Evaluación de Contraseñas**
   - Utiliza modelos de redes neuronales entrenados para predecir la fortaleza de las contraseñas.

### 6. **Escáner de Vulnerabilidades Web**
   - Analiza sitios web en busca de vulnerabilidades comunes.

### 7. **Verificador de Fugas de Datos**
   - Verifica si tus contraseñas han sido expuestas en fugas de datos conocidas.

---

## 📊 **Estado del Proyecto**
- **Versión Actual**: 1.0.0
- **Estado**: En desarrollo activo.
- **Próximas Funcionalidades**:
  - Integración con WhatsApp y Telegram.
  - Interfaz gráfica de usuario más avanzada.

---

## 🛠️ **Tecnologías y Herramientas Usadas**

### Frontend:
- **Streamlit**
- **CSS**

### Backend:
- **Python**
- **TensorFlow/Keras**
- **Scikit-learn**
- **Groq API**
- **Cryptography**

### APIs Externas:
- **GitHub OAuth**
- **Have I Been Pwned API**

### Otras Herramientas:
- **Git** para control de versiones.
- **Docker** para contenerización.

---

## 🎓 **Conclusiones del Proyecto**

WildPassPro es un proyecto ambicioso que combina seguridad, inteligencia artificial y usabilidad para ofrecer una solución completa de gestión de contraseñas. A lo largo del desarrollo, hemos aprendido la importancia de:

1. **Seguridad**: Implementar medidas robustas para proteger los datos de los usuarios.
2. **IA**: Utilizar modelos avanzados para mejorar la experiencia del usuario.
3. **Usabilidad**: Diseñar interfaces intuitivas y fáciles de usar.

Este proyecto no solo mejora la seguridad de los usuarios, sino que también sirve como un ejemplo de cómo la tecnología puede ser utilizada para resolver problemas cotidianos de manera eficiente.

---

## 🌍 **Haz del Mundo un Lugar Más Seguro**

Con WildPassPro, no solo proteges tus datos, sino que también contribuyes a un mundo digital más seguro. ¡Únete a nosotros y sé parte de la revolución de la seguridad!

---

**WildPassPro** - Porque tu seguridad es nuestra prioridad. 🔐

---

¡Esperamos que disfrutes usando WildPassPro tanto como nosotros disfrutamos creándolo! 🚀
