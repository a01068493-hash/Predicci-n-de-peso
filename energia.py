# Importar librerías necearias
import numpy as np
import streamlit as st
import pandas as pd

# Insertamos título
st.write(''' # ODS 7: Energía Asequible y No Contaminante''')
# Insertamos texto con formato
st.markdown("""
Esta aplicación utiliza **Machine Learning** para predecir el impacto del nivel del viento en la generación de energía **ODS 7: Energía Asequible y No Contaminante**.
""")
# Insertamos una imagen
st.image("enes.jpg", caption="Eficiencia energética de acuerdo al nivel del viento.")


# Definimos cómo ingresará los datos el usuario
# Usaremos un deslizador
st.sidebar.header("Velocidad del viento")
# Definimos los parámetros de nuestro deslizador:
  # Límite inferior: 24°C. Es el límite inferior donde los arrecifes tropicales suelen estar cómodos
  # Límite superior: 35°C. La mayoría de los corales mueren o se blanquean totalmente mucho antes de llegar a esa temperatura
  # Valor inicial: 28°C. En muchos arrecifes, a partir de los 28.5°C o 29°C comienza el estrés térmico severo
temp_input = st.sidebar.slider("Velocidad del viento en m/s",0,30)

# Cargamos el archivo con los datos (.csv)
df =  pd.read_csv('ene2.csv', encoding='latin-1')
# Seleccionamos las variables
X = df[['Velocidad_Viento_ms']]
y = df['Eficiencia_Energetica_kWh']

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
st.subheader('Eficiencia energetica')
st.write(f'El nivel de energía es: {prediccion:.2f} Wkh')

if prediccion < 500:
        st.success("Eficiencia baja")
elif prediccion < 3000:
        st.warning("Alta eficiencia")
else:
        st.error("Muy alta eficiencia")
