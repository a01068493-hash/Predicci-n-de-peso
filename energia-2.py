
import numpy as np
import streamlit as st
import pandas as pd

st.write(''' ODS 7: Energía Asequible y No Contaminante''')
st.markdown("""
Esta aplicación utiliza **Machine Learning** para predecir el impacto de la radiación del sol en la generación de energía **ODS 7: Energía Asequible y No Contaminante**.
""")

st.image("sol.jpg", caption="Eficiencia energética generada en función de la radiación del sol.")
st.sidebar.header("Intensidad de la Radiación Solar")
temp_input = st.sidebar.slider("Intensidad de la Radiación Solar(W/m2)",0,1120)

df =  pd.read_csv('eneg2.csv', encoding='latin-1')
X = df[['VAR_2']]
y = df['VAR_4']

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)
LR = LinearRegression()
LR.fit(X_train,y_train)

b1 = LR.coef_
b0 = LR.intercept_
prediccion = b0 + b1[0]*temp_input

st.subheader('Eficiencia energética')
st.write(f'El nivel de energía es: {prediccion:.2f} Wkh')

if prediccion < 360:
        st.error("Eficiencia baja")
elif prediccion < 410:
        st.warning("Eficiencia moderada")
else:
        st.succes("Muy alta eficiencia")
