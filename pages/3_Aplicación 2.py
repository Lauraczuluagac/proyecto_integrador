import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Crea un conjunto de datos de ejemplo
import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

# Crea un diagrama de dispersión
sns.scatterplot(x='sepal_length', y='sepal_width', data=data, hue='species')

# Agrega etiquetas y título
plt.xlabel('Longitud del Sépalo')
plt.ylabel('Ancho del Sépalo')
plt.title('Diagrama de Dispersión de Longitud del Sépalo vs. Ancho del Sépalo')

# Muestra el gráfico
plt.show()

st.header("Aplicacón 2")