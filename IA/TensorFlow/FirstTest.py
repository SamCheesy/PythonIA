import tensorflow as tf
import numpy as np

celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
farenheit  = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

capa = tf.keras
modelo = tf.keras.models.Sequential([capa])
modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss='mean_squared_error'
)

print("Comenzando entrenamiento...")
historial = modelo.fit(celsius, farenheit, epochs=1200, verbose=False)
print("Modelo entrenado.")

numero = float(input("digita un valor en celsius para convertir en farenheit."))
resultado = modelo.predict([numero])
print(f"el resultado es: {str(resultado)} farenheit!")
