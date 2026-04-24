# Importar librerías necearias
import numpy as np
import streamlit as st
import pandas as pd

# Insertamos título
st.write(''' # ODS 13: Acción por el clima ''')
# Insertamos texto con formato
st.markdown("""
Esta aplicación utiliza **Machine Learning** para predecir el cambio climatico con el paso de los años, alineado con el **ODS 3: Acción por el clima**.
""")
# Insertamos una imagen
st.image("clima.jpg", caption="El impacto de nuestras acciones reflejado en el cambio climatico con el paso del tiempo")

#st.header('Datos personales')

# Definimos cómo ingresará los datos el usuario
# Usaremos un deslizador
st.header("Año")
# Definimos los parámetros de nuestro deslizador:
  # Límite inferior: 24°C. Es el límite inferior donde los arrecifes tropicales suelen estar cómodos
  # Límite superior: 35°C. La mayoría de los corales mueren o se blanquean totalmente mucho antes de llegar a esa temperatura
  # Valor inicial: 28°C. En muchos arrecifes, a partir de los 28.5°C o 29°C comienza el estrés térmico severo
temp_input = st.number_input("Año", 1880.0, 2026.0, 2020.0)

# Cargamos el archivo con los datos (.csv)
df =  pd.read_csv('Temperatura.csv', encoding='latin-1')
# Seleccionamos las variables
X = df[['anio']]
y = df['temperatura']

# Creamos y entrenamos el modelo
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)
LR = LinearRegression()
LR.fit(X_train,y_train)

# Hacemos la predicción con el modelo y la temperatura seleccionada por el usuario
b1 = LR.coef_
b0 = LR.intercept_
prediccion = b0 + b1[0]*temp_input

# Presentamos loa resultados
st.subheader('Temperatura')
st.write(f'La temperatura de ese año es {prediccion:.2f}°C')
