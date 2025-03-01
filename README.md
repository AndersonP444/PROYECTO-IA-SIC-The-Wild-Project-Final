**# PROYECTO-IA-SIC-The-Wild-Project**
**Este grupo esta conformado por: **
Anderson Perdomo, Diego Alviarez, Jeremy Vicent, Kevin Rodriguez y Greymel Moreno. 
Nosotros desarrollaremos y le daremos una estructura solida y estable a una pagina web.

**Este proyeto lleva como nombre: **
**WildPassPro: Generador y Validador de Contraseñas Seguras con IA.**
Este proyecto no solo generará y validará contraseñas seguras, sino que también utilizará un modelo de red neuronal entrenado con TensorFlow para predecir la fortaleza de una contraseña basándose en patrones de contraseñas comunes y vulnerabilidades conocidas. El modelo aprenderá a identificar contraseñas débiles, predecibles o comprometidas, y proporcionará recomendaciones inteligentes para mejorarlas.
Cuenta con un inicio de sesion, generador de contraseñas, portafolio y muchas funciones utiles. 

**Este proyecto cuenta con las librerias:**
streamlit
Pandas
numpy
re
requests
openai
joblib
tensorflow
secrets
string
os
io
time
json
sklearn.model_selection import train_test_split
sklearn.preprocessing import LabelEncoder
cryptography.fernet import Fernet
tensorflow.keras.models import Sequential
tensorflow.keras.layers import Dense

El código implementa una Red Neuronal Artificial Prealimentada con 3 capas y 133 neuronas en total. 
Funcionamiento de las Neuronas
1. Capa Oculta 1 (64 neuronas)
  * Entrada: 4 características (length, has_upper, has_digit, has_symbol)
  * Función de Activación: ReLU (Rectified Linear Unit)
  * Función:
    h_1 = \text{ReLU}(W_1 \cdot X + b_1)
    * Detecta patrones básicos de seguridad en contraseñas
    * Aprende relaciones no lineales entre las características de entrada
      
2. Capa Oculta 2 (64 neuronas)
  * Entrada: Salida de la capa anterior (64 valores)
  * Función de Activación: ReLU
  * Función:
    h_2 = \text{ReLU}(W_2 \cdot h_1 + b_2)
    * Combina patrones detectados en la capa anterior
    * Genera representaciones más complejas de seguridad
   
3. Capa de Salida (3 neuronas)
  * Función de Activación: Softmax
  * Función:
    y_{\text{pred}} = \text{softmax}(W_3 \cdot h_2 + b_3)
    * Calcula probabilidades para cada clase:
      * 0: Débil
      * 1: Media
      * 2: Fuerte

Parámetros Aprendidos
Capa	Neuronas	Parámetros (Weights + Biases)
Entrada → Oculta1	64	(4*64) + 64 = 320
Oculta1 → Oculta2	64	(64*64) + 64 = 4,160
Oculta2 → Salida	3	(64*3) + 3 = 195
Total	131	4,675 parámetros

**Funciones Clave en el Código**
1. predecir_fortaleza()
  * Input: Contraseña del usuario
  * Proceso:
    features = [longitud, mayúsculas, dígitos, símbolos]  # Vector de 4 elementos
    prediction = model.predict(features)                   # Propagación hacia adelante
  * Output: Índice de la clase predicha (0-2)

2. Flujo de Datos
  Usuario → Extracción de Features → Normalización → Red Neuronal → Probabilidades → Clase Final

**Dinámica de Entrenamiento**
  1. Dataset: 500 contraseñas generadas por Groq/LLama3
  2. Optimización:
     * Función de Pérdida: sparse_categorical_crossentropy
     * Optimizador: Adam (tasa de aprendizaje adaptativa)
  3. Regularización:
     * Dropout: No aplicado (podría añadirse entre capas)
     * Early Stopping: No implementado (se entrenan 10 épocas fijas)

   
  

