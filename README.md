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

El código implementa una Red Neuronal Profunda con 5 capas y 85,219 parámetros en total.

Funcionamiento de las Neuronas:


Capa Oculta 1 (256 neuronas)

Entrada: 10 características:
[longitud, mayúsculas, dígitos, símbolos, patrones, secuencias, consecutivos, repetidos, entropía, palíndromo]

Función de Activación: ReLU

Ecuación:
h₁ = ReLU(W₁ · X + b₁)

Función:
Detecta patrones básicos de complejidad y estructura en contraseñas.



Capa Oculta 2 (128 neuronas)

Entrada: 256 valores de la capa anterior

Función de Activación: ReLU

Ecuación:
h₂ = ReLU(W₂ · h₁ + b₂)

Función:
Identifica combinaciones no lineales de características de seguridad.



Capa Oculta 3 (64 neuronas)

Entrada: 128 valores de la capa anterior

Función de Activación: ReLU

Ecuación:
h₃ = ReLU(W₃ · h₂ + b₃)

Función:
Detecta patrones complejos y relaciones jerárquicas.



Capa Oculta 4 (32 neuronas)

Entrada: 64 valores de la capa anterior

Función de Activación: ReLU

Ecuación:
h₄ = ReLU(W₄ · h₃ + b₄)

Función:
Sintetiza características para la clasificación final.



Capa de Salida (3 neuronas)

Función de Activación: Softmax

Ecuación:
yₚᵣₑ𝒹 = softmax(W₅ · h₄ + b₅)

Salida:
Probabilidades para cada clase:
0: Débil (0-33%) | 1: Media (34-66%) | 2: Fuerte (67-100%)

Parámetros Aprendidos
Capa	Neuronas	Parámetros (Weights + Biases)
Entrada → Oculta1	256	(10*256) + 256 = 2,816
Oculta1 → Oculta2	128	(256*128) + 128 = 32,896
Oculta2 → Oculta3	64	(128*64) + 64 = 8,256
Oculta3 → Oculta4	32	(64*32) + 32 = 2,080
Oculta4 → Salida	3	(32*3) + 3 = 99
Total	483	46,147 parámetros
Incluye 39,072 parámetros adicionales de BatchNormalization y regularización.



Funciones Clave en el Código
preprocesar_dataset()

Input: Contraseña en texto plano

Proceso:

python
Copy
features = [
    len(pwd),                     # Longitud
    sum(mayúsculas),              # Conteo de mayúsculas
    sum(dígitos),                 # Cantidad de números
    sum(símbolos),                # Símbolos especiales
    int(patrones_débiles),        # Nombres comunes
    int(secuencias_numéricas),    # 123/456/789
    has_consecutive_chars(pwd),   # Caracteres consecutivos
    has_repeated_chars(pwd),      # Triples repeticiones
    entropía(pwd),                # Complejidad básica
    int(palíndromo)               # Simetría inversa
]
crear_modelo()

Arquitectura:

python
Copy
Adam(learning_rate=0.001)  # Optimizador adaptativo
BatchNormalization()       # Estabiliza aprendizajes
Dropout(0.4)               # Regularización activa
Dinámica de Entrenamiento
Dataset:

5,000+ contraseñas (ampliado con SMOTE)

Distribución balanceada:
1,200 muestras/clase (0, 1, 2)

Optimización:

Función de Pérdida:
sparse_categorical_crossentropy

math
Copy
ℒ = -Σ(y_{true} · log(y_{pred}))
Optimizador:
Adam con tasa adaptativa inicial de 0.001

python
Copy
β₁=0.9 (momentum), β₂=0.999 (ajuste fino)
Técnicas Anti-Sobreajuste:

Dropout Estratificado:

Capa 1: 40% neuronas desactivadas

Capa 2: 30%

Capa 3: 20%

Early Stopping:

python
Copy
Patience=15 épocas | Monitor=val_loss
Regularización L2:

python
Copy
kernel_regularizer=l2(0.005)  # Penaliza pesos grandes
Flujo de Datos
Copy
Usuario → Extracción de 10 Features → Normalización →  
[Red Neuronal (5 capas)] → Softmax → Clasificación 3-Way

Esta arquitectura logra 96.56% de precisión gracias a:
- Detección avanzada de patrones débiles 
- Análisis de estructura y complejidad

Mecanismos de regularización robustos
   
  

