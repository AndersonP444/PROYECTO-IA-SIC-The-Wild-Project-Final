# -*- coding: utf-8 -*-
"""redneuronal.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Yo9OS8HeSiKFad5iNj6O2zNJUUNOONSE
"""

# Importar librerías necesarias
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, BatchNormalization
from tensorflow.keras.callbacks import EarlyStopping
import tensorflow as tf

# Cargar el dataset desde GitHub
dataset_url = "https://github.com/AndersonP444/PROYECTO-IA-SIC-The-Wild-Project/raw/main/password_dataset_final.csv"
df = pd.read_csv(dataset_url)

# Añadir contraseñas débiles adicionales
weak_passwords = [
    {"password": "Pepito123", "strength": 0},
    {"password": "Juan456", "strength": 0},
    {"password": "Maria789", "strength": 0},
    {"password": "Pedro123", "strength": 0},
    {"password": "Ana456", "strength": 0},
    {"password": "Luis789", "strength": 0},
    {"password": "Carlos123", "strength": 0},
    {"password": "Laura456", "strength": 0},
    {"password": "Sofia789", "strength": 0},
    {"password": "Diego123", "strength": 0},
]
weak_df = pd.DataFrame(weak_passwords)
df = pd.concat([df, weak_df], ignore_index=True)

# Función para preprocesar el dataset
def preprocesar_dataset(df):
    X = np.array([[
        len(row["password"]),                        # Longitud de la contraseña
        sum(1 for c in row["password"] if c.islower()),  # Conteo de minúsculas
        sum(1 for c in row["password"] if c.isupper()),  # Conteo de mayúsculas
        sum(1 for c in row["password"] if c.isdigit()),  # Conteo de dígitos
        sum(1 for c in row["password"] if c in "!@#$%^&*()"),  # Conteo de símbolos
        int(row["password"].lower() in ["maria", "juan", "pedro", "diego", "media"]),  # Nombres comunes
        int("123" in row["password"] or "abc" in row["password"].lower() or "809" in row["password"]),  # Secuencias simples
        len(set(row["password"]))  # Variabilidad de caracteres
    ] for _, row in df.iterrows()])

    y = df["strength"].values
    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(y)
    return X, y, label_encoder

# Preprocesar el dataset
X, y, label_encoder = preprocesar_dataset(df)

# Dividir el dataset en entrenamiento y validación
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el modelo de red neuronal
def crear_modelo():
    model = Sequential([
        Dense(64, activation='relu', input_shape=(8,)),  # Capa oculta 1
        BatchNormalization(),
        Dropout(0.3),

        Dense(32, activation='relu'),  # Capa oculta 2
        BatchNormalization(),
        Dropout(0.3),

        Dense(16, activation='relu'),  # Capa oculta 3
        BatchNormalization(),
        Dropout(0.3),

        Dense(3, activation='softmax')  # Capa de salida (3 clases)
    ])

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

# Crear y entrenar el modelo
model = crear_modelo()  # Corregido: usar crear_modelo en lugar de crear_model

# Early Stopping para evitar sobreajuste
early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

# Entrenar el modelo
history = model.fit(
    X_train, y_train,
    epochs=100,
    batch_size=32,
    validation_data=(X_val, y_val),
    callbacks=[early_stopping],
    verbose=1
)

# Guardar el modelo entrenado
model.save("password_strength_model.h5")
print("Modelo entrenado y guardado como 'password_strength_model.h5'.")

# Evaluar el modelo en el conjunto de validación
loss, accuracy = model.evaluate(X_val, y_val, verbose=0)
print(f"Precisión en el conjunto de validación: {accuracy * 100:.2f}%")